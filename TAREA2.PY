# ============================================================
# TAREA 2: ANÁLISIS EXPLORATORIO Y LIMPIEZA DE SDNET2018
# ============================================================

from pathlib import Path
from PIL import Image, UnidentifiedImageError
import pandas as pd
import matplotlib.pyplot as plt
import random
import shutil


# ============================================================
# 1. CONFIGURACIÓN
# ============================================================

# CAMBIAR ESTA RUTA POR LA UBICACIÓN REAL DE TU CARPETA
RUTA_DATASET = Path(
    r"E:\SDNET2018"
)

# Carpeta donde se guardará el dataset limpio
RUTA_LIMPIA = RUTA_DATASET.parent / "SDNET2018_LIMPIO"

# Tamaño uniforme para las imágenes limpias
ANCHO_OBJETIVO = 256
ALTO_OBJETIVO = 256

# Extensiones que serán reconocidas como imágenes
EXTENSIONES_VALIDAS = {".jpg", ".jpeg", ".png"}


# ============================================================
# 2. DEFINICIÓN DE LAS CARPETAS Y ETIQUETAS
# ============================================================

# Formato:
# "nombre de la subcarpeta": ("tipo de elemento", "estado", etiqueta)

CLASES = {
    "CD": ("Deck", "Con grieta", 1),
    "UD": ("Deck", "Sin grieta", 0),

    "CW": ("Muro", "Con grieta", 1),
    "UW": ("Muro", "Sin grieta", 0),

    "CP": ("Pavimento", "Con grieta", 1),
    "UP": ("Pavimento", "Sin grieta", 0)
}

CARPETAS = {
    "CD": RUTA_DATASET / "DECK" / "CD",
    "UD": RUTA_DATASET / "DECK" / "UD",

    "CW": RUTA_DATASET / "MURO" / "CW",
    "UW": RUTA_DATASET / "MURO" / "UW",

    "CP": RUTA_DATASET / "PAVIMENTO" / "CP",
    "UP": RUTA_DATASET / "PAVIMENTO" / "UP"
}


# ============================================================
# 3. VERIFICACIÓN DE LA ESTRUCTURA DE CARPETAS
# ============================================================

print("=" * 60)
print("VERIFICACIÓN DE CARPETAS")
print("=" * 60)

carpetas_faltantes = []

for codigo, ruta in CARPETAS.items():

    if ruta.exists():
        print(f"Correcto: {codigo} -> {ruta}")

    else:
        print(f"NO SE ENCONTRÓ: {codigo} -> {ruta}")
        carpetas_faltantes.append(ruta)

if carpetas_faltantes:
    print("\nRevisa la ruta del dataset o los nombres de las carpetas.")
    raise SystemExit

print("\nTodas las carpetas fueron encontradas correctamente.")


# ============================================================
# 4. LECTURA Y VERIFICACIÓN DE LAS IMÁGENES
# ============================================================

registros = []
imagenes_corruptas = []

print("\n" + "=" * 60)
print("LEYENDO Y VERIFICANDO IMÁGENES")
print("=" * 60)

for codigo_clase, carpeta in CARPETAS.items():

    elemento, estado, etiqueta = CLASES[codigo_clase]

    archivos = [
        archivo
        for archivo in carpeta.iterdir()
        if archivo.is_file()
        and archivo.suffix.lower() in EXTENSIONES_VALIDAS
    ]

    print(f"\nProcesando {codigo_clase}: {len(archivos)} archivos")

    for numero, ruta_imagen in enumerate(archivos, start=1):

        try:
            # Verificación inicial
            with Image.open(ruta_imagen) as imagen:
                imagen.verify()

            # Se vuelve a abrir porque verify() cierra la imagen
            with Image.open(ruta_imagen) as imagen:

                ancho, alto = imagen.size
                formato = imagen.format
                modo_color = imagen.mode

            tamaño_bytes = ruta_imagen.stat().st_size

            registros.append({
                "archivo": ruta_imagen.name,
                "ruta": str(ruta_imagen),
                "carpeta": codigo_clase,
                "elemento": elemento,
                "estado": estado,
                "etiqueta": etiqueta,
                "ancho_px": ancho,
                "alto_px": alto,
                "formato": formato,
                "modo_color": modo_color,
                "tamaño_bytes": tamaño_bytes,
                "imagen_valida": True
            })

        except (
            UnidentifiedImageError,
            OSError,
            ValueError
        ) as error:

            print(f"Imagen corrupta: {ruta_imagen.name}")

            imagenes_corruptas.append({
                "archivo": ruta_imagen.name,
                "ruta": str(ruta_imagen),
                "carpeta": codigo_clase,
                "error": str(error)
            })

        if numero % 1000 == 0:
            print(f"  {numero} imágenes revisadas...")


# ============================================================
# 5. CREACIÓN DEL DATAFRAME
# ============================================================

df = pd.DataFrame(registros)

if df.empty:
    print("No se encontraron imágenes válidas.")
    raise SystemExit

print("\n" + "=" * 60)
print("RESUMEN GENERAL DEL DATASET")
print("=" * 60)

print(f"Total de imágenes válidas: {len(df)}")
print(f"Total de imágenes corruptas: {len(imagenes_corruptas)}")

print("\nPrimeras filas del inventario:")
print(df.head())


# ============================================================
# 6. VERIFICACIÓN DE VALORES NULOS
# ============================================================

print("\n" + "=" * 60)
print("VALORES NULOS")
print("=" * 60)

valores_nulos = df.isnull().sum()

print(valores_nulos)

total_nulos = valores_nulos.sum()

if total_nulos == 0:
    print("\nNo se encontraron valores nulos.")
else:
    print(f"\nSe encontraron {total_nulos} valores nulos.")


# ============================================================
# 7. DISTRIBUCIÓN POR CARPETAS
# ============================================================

print("\n" + "=" * 60)
print("CANTIDAD DE IMÁGENES POR CARPETA")
print("=" * 60)

conteo_carpetas = df["carpeta"].value_counts().sort_index()

print(conteo_carpetas)


# ============================================================
# 8. DISTRIBUCIÓN CON GRIETA Y SIN GRIETA
# ============================================================

print("\n" + "=" * 60)
print("DISTRIBUCIÓN POR ESTADO")
print("=" * 60)

conteo_estado = df["estado"].value_counts()

print(conteo_estado)


# ============================================================
# 9. DISTRIBUCIÓN POR ELEMENTO ESTRUCTURAL
# ============================================================

print("\n" + "=" * 60)
print("DISTRIBUCIÓN POR ELEMENTO")
print("=" * 60)

tabla_elementos = pd.crosstab(
    df["elemento"],
    df["estado"]
)

print(tabla_elementos)


# ============================================================
# 10. RESOLUCIONES DE LAS IMÁGENES
# ============================================================

print("\n" + "=" * 60)
print("RESOLUCIONES ENCONTRADAS")
print("=" * 60)

resoluciones = (
    df.groupby(["ancho_px", "alto_px"])
    .size()
    .reset_index(name="cantidad")
    .sort_values("cantidad", ascending=False)
)

print(resoluciones)


# ============================================================
# 11. FORMATOS Y MODOS DE COLOR
# ============================================================

print("\n" + "=" * 60)
print("FORMATOS DE IMAGEN")
print("=" * 60)

print(df["formato"].value_counts())

print("\n" + "=" * 60)
print("MODOS DE COLOR")
print("=" * 60)

print(df["modo_color"].value_counts())


# ============================================================
# 12. ESTADÍSTICAS DEL TAMAÑO DE LOS ARCHIVOS
# ============================================================

df["tamaño_kb"] = df["tamaño_bytes"] / 1024

print("\n" + "=" * 60)
print("ESTADÍSTICAS DEL TAMAÑO DE ARCHIVOS EN KB")
print("=" * 60)

print(df["tamaño_kb"].describe())


# ============================================================
# 13. GRÁFICO DE IMÁGENES POR CARPETA
# ============================================================

plt.figure(figsize=(9, 5))

conteo_carpetas.plot(kind="bar")

plt.title("Cantidad de imágenes por carpeta")
plt.xlabel("Carpeta")
plt.ylabel("Número de imágenes")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    RUTA_DATASET / "grafico_imagenes_por_carpeta.png",
    dpi=300
)

plt.show()


# ============================================================
# 14. GRÁFICO CON GRIETA Y SIN GRIETA
# ============================================================

plt.figure(figsize=(7, 5))

conteo_estado.plot(kind="bar")

plt.title("Distribución de imágenes por estado")
plt.xlabel("Estado")
plt.ylabel("Número de imágenes")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    RUTA_DATASET / "grafico_estado_grieta.png",
    dpi=300
)

plt.show()


# ============================================================
# 15. GRÁFICO POR ELEMENTO Y ESTADO
# ============================================================

tabla_elementos.plot(
    kind="bar",
    figsize=(9, 5)
)

plt.title("Distribución por elemento estructural")
plt.xlabel("Elemento estructural")
plt.ylabel("Número de imágenes")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    RUTA_DATASET / "grafico_elemento_estado.png",
    dpi=300
)

plt.show()


# ============================================================
# 16. VISUALIZACIÓN DE IMÁGENES DE EJEMPLO
# ============================================================

def mostrar_ejemplos(dataframe, cantidad=12):
    """
    Muestra una selección aleatoria de imágenes válidas.
    """

    cantidad_real = min(cantidad, len(dataframe))

    muestra = dataframe.sample(
        n=cantidad_real,
        random_state=42
    )

    columnas = 4
    filas = (cantidad_real + columnas - 1) // columnas

    figura, ejes = plt.subplots(
        filas,
        columnas,
        figsize=(14, filas * 3)
    )

    ejes = ejes.flatten()

    for eje, (_, fila) in zip(ejes, muestra.iterrows()):

        try:
            with Image.open(fila["ruta"]) as imagen:
                imagen_rgb = imagen.convert("RGB")

            eje.imshow(imagen_rgb)

            eje.set_title(
                f'{fila["carpeta"]}\n{fila["estado"]}'
            )

            eje.axis("off")

        except OSError:
            eje.axis("off")

    # Apaga los espacios sobrantes
    for eje in ejes[cantidad_real:]:
        eje.axis("off")

    plt.suptitle(
        "Ejemplos aleatorios del dataset SDNET2018",
        fontsize=15
    )

    plt.tight_layout()

    plt.savefig(
        RUTA_DATASET / "muestra_imagenes.png",
        dpi=300
    )

    plt.show()


mostrar_ejemplos(df, cantidad=12)


# ============================================================
# 17. GUARDAR EL INVENTARIO EN CSV
# ============================================================

ruta_csv = RUTA_DATASET / "inventario_sdnet2018.csv"

df.to_csv(
    ruta_csv,
    index=False,
    encoding="utf-8-sig"
)

print(f"\nInventario guardado en:\n{ruta_csv}")


# ============================================================
# 18. GUARDAR REPORTE DE IMÁGENES CORRUPTAS
# ============================================================

if imagenes_corruptas:

    df_corruptas = pd.DataFrame(imagenes_corruptas)

    ruta_corruptas = (
        RUTA_DATASET / "imagenes_corruptas.csv"
    )

    df_corruptas.to_csv(
        ruta_corruptas,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        f"Reporte de imágenes corruptas guardado en:\n"
        f"{ruta_corruptas}"
    )

else:
    print("No se encontraron imágenes corruptas.")


# ============================================================
# 19. LIMPIEZA Y NORMALIZACIÓN DEL DATASET
# ============================================================

print("\n" + "=" * 60)
print("CREANDO DATASET LIMPIO")
print("=" * 60)

# Borra una versión anterior para evitar duplicaciones
if RUTA_LIMPIA.exists():
    shutil.rmtree(RUTA_LIMPIA)

RUTA_LIMPIA.mkdir(parents=True, exist_ok=True)

imagenes_limpiadas = 0
errores_limpieza = []

for indice, fila in df.iterrows():

    ruta_original = Path(fila["ruta"])

    # Conserva la misma estructura de carpetas
    ruta_relativa = ruta_original.relative_to(RUTA_DATASET)

    ruta_destino = RUTA_LIMPIA / ruta_relativa

    ruta_destino.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    try:
        with Image.open(ruta_original) as imagen:

            # Convierte todas las imágenes a tres canales RGB
            imagen = imagen.convert("RGB")

            # Uniformiza todas las imágenes a 256 x 256 píxeles
            imagen = imagen.resize(
                (ANCHO_OBJETIVO, ALTO_OBJETIVO)
            )

            # Guarda la imagen limpia
            imagen.save(
                ruta_destino,
                format="JPEG",
                quality=95
            )

        imagenes_limpiadas += 1

    except (
        UnidentifiedImageError,
        OSError,
        ValueError
    ) as error:

        errores_limpieza.append({
            "archivo": ruta_original.name,
            "ruta": str(ruta_original),
            "error": str(error)
        })

    if (indice + 1) % 1000 == 0:
        print(
            f"{indice + 1} imágenes procesadas..."
        )


# ============================================================
# 20. RESULTADOS FINALES
# ============================================================

print("\n" + "=" * 60)
print("RESULTADOS FINALES")
print("=" * 60)

print(f"Imágenes originales válidas: {len(df)}")
print(f"Imágenes corruptas detectadas: {len(imagenes_corruptas)}")
print(f"Imágenes limpiadas: {imagenes_limpiadas}")
print(f"Errores durante la limpieza: {len(errores_limpieza)}")

print(
    f"\nEl dataset limpio fue guardado en:\n"
    f"{RUTA_LIMPIA}"
)

print(
    "\nLas imágenes limpias tienen:"
    f"\n- Resolución: {ANCHO_OBJETIVO} x {ALTO_OBJETIVO} píxeles"
    "\n- Modo de color: RGB"
    "\n- Formato: JPEG"
)

print("\nProceso terminado correctamente.")