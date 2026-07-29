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
RUTA_DATASET = Path(r"D:\SDNET2018")

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

    ruta_destino = (RUTA_LIMPIA / ruta_relativa).with_suffix(".jpg")

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
# ============================================================
# 21. TAREA 3: CONFIGURACIÓN DEL MODELO
# ============================================================
#
# Esta sección completa la implementación del modelo:
# - división estratificada en entrenamiento, validación y prueba;
# - CNN para clasificación binaria;
# - cálculo automático de pesos de clase;
# - entrenamiento con class_weight;
# - métricas, matriz de confusión y reporte;
# - predicción de imágenes nuevas;
# - estimación del espesor de fisura en píxeles;
# - conversión opcional a milímetros si existe calibración.
#
# IMPORTANTE:
# SDNET2018 indica si una imagen tiene o no fisura, pero no incluye
# máscaras de segmentación píxel a píxel ni una escala física fiable.
# Por ello, el espesor calculado aquí es una ESTIMACIÓN EN PÍXELES.
# Solo debe convertirse a milímetros cuando se disponga de una
# calibración real mm/píxel obtenida con una regla, patrón o metadato.

import json
import numpy as np
import cv2
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)
from skimage.morphology import skeletonize


# ----------------------------
# Reproducibilidad
# ----------------------------

SEMILLA = 42

random.seed(SEMILLA)
np.random.seed(SEMILLA)
tf.random.set_seed(SEMILLA)


# ----------------------------
# Hiperparámetros
# ----------------------------

TAMANO_IMAGEN = (256, 256)
TAMANO_LOTE = 32
EPOCAS = 20
TASA_APRENDIZAJE = 1e-3

# Umbral de decisión para clasificar una imagen como fisurada.
UMBRAL_CLASIFICACION = 0.50

# Conversión opcional a milímetros.
# Ejemplo: si 100 píxeles representan 50 mm, usar 0.50.
# Mantener None mientras no exista una calibración física confiable.
MM_POR_PIXEL = None


# ----------------------------
# Carpetas de resultados
# ----------------------------

RUTA_RESULTADOS = RUTA_DATASET.parent / "RESULTADOS_TAREA3"
RUTA_RESULTADOS.mkdir(parents=True, exist_ok=True)

RUTA_MODELO = RUTA_RESULTADOS / "modelo_cnn_sdnet2018.keras"
RUTA_MEJOR_MODELO = RUTA_RESULTADOS / "mejor_modelo_cnn_sdnet2018.keras"


# ============================================================
# 22. CONSTRUIR EL INVENTARIO DEL DATASET LIMPIO
# ============================================================

print("\n" + "=" * 60)
print("PREPARANDO DATOS PARA LA CNN")
print("=" * 60)

df_modelo = df.copy()

df_modelo["ruta_limpia"] = df_modelo["ruta"].apply(
    lambda ruta: str(
        (
            RUTA_LIMPIA
            / Path(ruta).relative_to(RUTA_DATASET)
        ).with_suffix(".jpg")
    )
)

df_modelo = df_modelo[
    df_modelo["ruta_limpia"].apply(lambda ruta: Path(ruta).exists())
].copy()

if df_modelo.empty:
    raise RuntimeError(
        "No se encontraron imágenes en el dataset limpio. "
        "Ejecuta primero las secciones de limpieza."
    )

# Estratificación simultánea por tipo de elemento y clase.
df_modelo["estrato"] = (
    df_modelo["elemento"].astype(str)
    + "_"
    + df_modelo["etiqueta"].astype(str)
)

print(f"Imágenes disponibles para modelado: {len(df_modelo)}")
print("\nDistribución de clases:")
print(df_modelo["etiqueta"].value_counts().sort_index())


# ============================================================
# 23. DIVISIÓN ENTRENAMIENTO / VALIDACIÓN / PRUEBA
# ============================================================

# 70 % entrenamiento, 15 % validación y 15 % prueba.

df_entrenamiento, df_temporal = train_test_split(
    df_modelo,
    test_size=0.30,
    random_state=SEMILLA,
    stratify=df_modelo["estrato"]
)

df_validacion, df_prueba = train_test_split(
    df_temporal,
    test_size=0.50,
    random_state=SEMILLA,
    stratify=df_temporal["estrato"]
)

print("\nTamaños de los subconjuntos:")
print(f"Entrenamiento: {len(df_entrenamiento)}")
print(f"Validación:    {len(df_validacion)}")
print(f"Prueba:        {len(df_prueba)}")

# Guardar las particiones para trazabilidad y reproducibilidad.
df_entrenamiento.to_csv(
    RUTA_RESULTADOS / "particion_entrenamiento.csv",
    index=False,
    encoding="utf-8-sig"
)

df_validacion.to_csv(
    RUTA_RESULTADOS / "particion_validacion.csv",
    index=False,
    encoding="utf-8-sig"
)

df_prueba.to_csv(
    RUTA_RESULTADOS / "particion_prueba.csv",
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# 24. CÁLCULO AUTOMÁTICO DE PESOS DE CLASE
# ============================================================

clases_presentes = np.sort(
    df_entrenamiento["etiqueta"].unique()
)

pesos_calculados = compute_class_weight(
    class_weight="balanced",
    classes=clases_presentes,
    y=df_entrenamiento["etiqueta"].to_numpy()
)

PESOS_CLASE = {
    int(clase): float(peso)
    for clase, peso in zip(clases_presentes, pesos_calculados)
}

print("\nPesos de clase calculados automáticamente:")
print(PESOS_CLASE)

# Con aproximadamente 15 % de imágenes fisuradas, el peso de la
# clase 1 será mayor. Así, equivocarse en una fisura tendrá una
# penalización más alta durante el entrenamiento.

with open(
    RUTA_RESULTADOS / "pesos_clase.json",
    "w",
    encoding="utf-8"
) as archivo_json:
    json.dump(PESOS_CLASE, archivo_json, indent=4)


# ============================================================
# 25. CREACIÓN DE tf.data.Dataset
# ============================================================

AUTOTUNE = tf.data.AUTOTUNE


def cargar_y_preprocesar(ruta, etiqueta):
    """
    Lee una imagen, la convierte a RGB, la redimensiona y normaliza
    sus valores de píxel al intervalo [0, 1].
    """

    contenido = tf.io.read_file(ruta)

    imagen = tf.io.decode_jpeg(
        contenido,
        channels=3
    )

    imagen = tf.image.resize(
        imagen,
        TAMANO_IMAGEN
    )

    imagen = tf.cast(imagen, tf.float32) / 255.0
    etiqueta = tf.cast(etiqueta, tf.float32)

    return imagen, etiqueta


def crear_dataset(dataframe, entrenamiento=False):
    """
    Convierte un DataFrame con rutas y etiquetas en un tf.data.Dataset.
    """

    rutas = dataframe["ruta_limpia"].astype(str).to_numpy()
    etiquetas = dataframe["etiqueta"].astype(np.float32).to_numpy()

    dataset = tf.data.Dataset.from_tensor_slices(
        (rutas, etiquetas)
    )

    if entrenamiento:
        dataset = dataset.shuffle(
            buffer_size=len(dataframe),
            seed=SEMILLA,
            reshuffle_each_iteration=True
        )

    dataset = dataset.map(
        cargar_y_preprocesar,
        num_parallel_calls=AUTOTUNE
    )

    dataset = dataset.batch(TAMANO_LOTE)
    dataset = dataset.prefetch(AUTOTUNE)

    return dataset


ds_entrenamiento = crear_dataset(
    df_entrenamiento,
    entrenamiento=True
)

ds_validacion = crear_dataset(
    df_validacion,
    entrenamiento=False
)

ds_prueba = crear_dataset(
    df_prueba,
    entrenamiento=False
)


# ============================================================
# 26. AUMENTO DE DATOS
# ============================================================

# El aumento se aplica solo durante el entrenamiento.
# No reemplaza los pesos de clase; ambas técnicas cumplen funciones
# distintas y pueden utilizarse conjuntamente.

aumento_datos = tf.keras.Sequential(
    [
        tf.keras.layers.RandomFlip(
            mode="horizontal_and_vertical",
            seed=SEMILLA
        ),
        tf.keras.layers.RandomRotation(
            factor=0.08,
            seed=SEMILLA
        ),
        tf.keras.layers.RandomZoom(
            height_factor=0.10,
            width_factor=0.10,
            seed=SEMILLA
        ),
        tf.keras.layers.RandomContrast(
            factor=0.10,
            seed=SEMILLA
        )
    ],
    name="aumento_datos"
)


# ============================================================
# 27. MODELO CNN
# ============================================================

def construir_modelo_cnn():
    """
    CNN binaria para detectar fisuras.
    Salida sigmoide:
    - valor cercano a 0: sin fisura;
    - valor cercano a 1: con fisura.
    """

    entradas = tf.keras.Input(
        shape=(*TAMANO_IMAGEN, 3),
        name="imagen_entrada"
    )

    x = aumento_datos(entradas)

    x = tf.keras.layers.Conv2D(
        32,
        kernel_size=3,
        padding="same",
        activation="relu"
    )(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPooling2D()(x)

    x = tf.keras.layers.Conv2D(
        64,
        kernel_size=3,
        padding="same",
        activation="relu"
    )(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPooling2D()(x)

    x = tf.keras.layers.Conv2D(
        128,
        kernel_size=3,
        padding="same",
        activation="relu"
    )(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPooling2D()(x)

    x = tf.keras.layers.Conv2D(
        256,
        kernel_size=3,
        padding="same",
        activation="relu"
    )(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPooling2D()(x)

    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.40)(x)

    salidas = tf.keras.layers.Dense(
        1,
        activation="sigmoid",
        name="probabilidad_fisura"
    )(x)

    modelo = tf.keras.Model(
        inputs=entradas,
        outputs=salidas,
        name="CNN_SDNET2018"
    )

    modelo.compile(
        optimizer=tf.keras.optimizers.Adam(
            learning_rate=TASA_APRENDIZAJE
        ),
        loss="binary_crossentropy",
        metrics=[
            tf.keras.metrics.BinaryAccuracy(
                name="accuracy"
            ),
            tf.keras.metrics.Precision(
                name="precision"
            ),
            tf.keras.metrics.Recall(
                name="recall"
            ),
            tf.keras.metrics.AUC(
                name="auc"
            )
        ]
    )

    return modelo


modelo = construir_modelo_cnn()
modelo.summary()


# ============================================================
# 28. ENTRENAMIENTO CON PESOS DE CLASE
# ============================================================

callbacks = [
    tf.keras.callbacks.EarlyStopping(
        monitor="val_auc",
        mode="max",
        patience=5,
        restore_best_weights=True
    ),
    tf.keras.callbacks.ModelCheckpoint(
        filepath=str(RUTA_MEJOR_MODELO),
        monitor="val_auc",
        mode="max",
        save_best_only=True
    ),
    tf.keras.callbacks.ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.5,
        patience=2,
        min_lr=1e-6
    ),
    tf.keras.callbacks.CSVLogger(
        str(RUTA_RESULTADOS / "historial_entrenamiento.csv")
    )
]

print("\n" + "=" * 60)
print("ENTRENAMIENTO DE LA CNN CON PESOS DE CLASE")
print("=" * 60)

historial = modelo.fit(
    ds_entrenamiento,
    validation_data=ds_validacion,
    epochs=EPOCAS,
    class_weight=PESOS_CLASE,
    callbacks=callbacks,
    verbose=1
)

modelo.save(RUTA_MODELO)

print(f"\nModelo final guardado en:\n{RUTA_MODELO}")
print(f"Mejor modelo guardado en:\n{RUTA_MEJOR_MODELO}")


# ============================================================
# 29. GRÁFICOS DEL ENTRENAMIENTO
# ============================================================

def guardar_grafico_historial(
    historia,
    metrica,
    titulo,
    nombre_archivo
):
    """
    Guarda un gráfico de entrenamiento y validación.
    """

    plt.figure(figsize=(8, 5))

    plt.plot(
        historia.history[metrica],
        label=f"Entrenamiento: {metrica}"
    )

    metrica_validacion = f"val_{metrica}"

    if metrica_validacion in historia.history:
        plt.plot(
            historia.history[metrica_validacion],
            label=f"Validación: {metrica}"
        )

    plt.title(titulo)
    plt.xlabel("Época")
    plt.ylabel(metrica)
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()

    plt.savefig(
        RUTA_RESULTADOS / nombre_archivo,
        dpi=300
    )

    plt.close()


guardar_grafico_historial(
    historial,
    "loss",
    "Pérdida durante el entrenamiento",
    "historial_loss.png"
)

guardar_grafico_historial(
    historial,
    "accuracy",
    "Exactitud durante el entrenamiento",
    "historial_accuracy.png"
)

guardar_grafico_historial(
    historial,
    "recall",
    "Sensibilidad durante el entrenamiento",
    "historial_recall.png"
)

guardar_grafico_historial(
    historial,
    "auc",
    "AUC durante el entrenamiento",
    "historial_auc.png"
)


# ============================================================
# 30. EVALUACIÓN FINAL EN EL CONJUNTO DE PRUEBA
# ============================================================

print("\n" + "=" * 60)
print("EVALUACIÓN FINAL")
print("=" * 60)

# Se carga el mejor modelo según AUC de validación.
mejor_modelo = tf.keras.models.load_model(
    RUTA_MEJOR_MODELO
)

probabilidades = mejor_modelo.predict(
    ds_prueba,
    verbose=1
).ravel()

predicciones = (
    probabilidades >= UMBRAL_CLASIFICACION
).astype(int)

etiquetas_reales = (
    df_prueba["etiqueta"]
    .astype(int)
    .to_numpy()
)

exactitud = accuracy_score(
    etiquetas_reales,
    predicciones
)

precision = precision_score(
    etiquetas_reales,
    predicciones,
    zero_division=0
)

sensibilidad = recall_score(
    etiquetas_reales,
    predicciones,
    zero_division=0
)

f1 = f1_score(
    etiquetas_reales,
    predicciones,
    zero_division=0
)

auc = roc_auc_score(
    etiquetas_reales,
    probabilidades
)

metricas_finales = {
    "accuracy": float(exactitud),
    "precision": float(precision),
    "recall_sensibilidad": float(sensibilidad),
    "f1_score": float(f1),
    "roc_auc": float(auc),
    "umbral_clasificacion": float(UMBRAL_CLASIFICACION)
}

print("\nMétricas finales:")
for nombre, valor in metricas_finales.items():
    print(f"{nombre}: {valor:.4f}")

with open(
    RUTA_RESULTADOS / "metricas_finales.json",
    "w",
    encoding="utf-8"
) as archivo_json:
    json.dump(
        metricas_finales,
        archivo_json,
        indent=4
    )

reporte = classification_report(
    etiquetas_reales,
    predicciones,
    target_names=["Sin fisura", "Con fisura"],
    digits=4,
    zero_division=0
)

print("\nReporte de clasificación:")
print(reporte)

with open(
    RUTA_RESULTADOS / "reporte_clasificacion.txt",
    "w",
    encoding="utf-8"
) as archivo_reporte:
    archivo_reporte.write(reporte)


# ============================================================
# 31. MATRIZ DE CONFUSIÓN
# ============================================================

matriz = confusion_matrix(
    etiquetas_reales,
    predicciones
)

print("\nMatriz de confusión:")
print(matriz)

plt.figure(figsize=(6, 5))
plt.imshow(matriz)
plt.title("Matriz de confusión")
plt.colorbar()

marcas = np.arange(2)

plt.xticks(
    marcas,
    ["Sin fisura", "Con fisura"],
    rotation=20
)

plt.yticks(
    marcas,
    ["Sin fisura", "Con fisura"]
)

plt.xlabel("Clase predicha")
plt.ylabel("Clase real")

for fila_matriz in range(matriz.shape[0]):
    for columna_matriz in range(matriz.shape[1]):
        plt.text(
            columna_matriz,
            fila_matriz,
            str(matriz[fila_matriz, columna_matriz]),
            ha="center",
            va="center"
        )

plt.tight_layout()

plt.savefig(
    RUTA_RESULTADOS / "matriz_confusion.png",
    dpi=300
)

plt.close()


# ============================================================
# 32. GUARDAR PREDICCIONES DEL CONJUNTO DE PRUEBA
# ============================================================

df_resultados_prueba = df_prueba.copy()

df_resultados_prueba["probabilidad_fisura"] = probabilidades
df_resultados_prueba["prediccion"] = predicciones
df_resultados_prueba["prediccion_texto"] = np.where(
    predicciones == 1,
    "Con fisura",
    "Sin fisura"
)

df_resultados_prueba["prediccion_correcta"] = (
    df_resultados_prueba["etiqueta"].astype(int)
    == df_resultados_prueba["prediccion"]
)

df_resultados_prueba.to_csv(
    RUTA_RESULTADOS / "predicciones_prueba.csv",
    index=False,
    encoding="utf-8-sig"
)


# ============================================================
# 33. SEGMENTACIÓN HEURÍSTICA DE LA FISURA
# ============================================================

def eliminar_componentes_pequenos(
    mascara,
    area_minima=20
):
    """
    Elimina regiones pequeñas que probablemente correspondan a ruido.
    """

    cantidad,
    etiquetas_componentes,
    estadisticas,
    _ = cv2.connectedComponentsWithStats(
        mascara,
        connectivity=8
    )

    mascara_filtrada = np.zeros_like(mascara)

    for identificador in range(1, cantidad):
        area = estadisticas[
            identificador,
            cv2.CC_STAT_AREA
        ]

        if area >= area_minima:
            mascara_filtrada[
                etiquetas_componentes == identificador
            ] = 255

    return mascara_filtrada


def segmentar_fisura(ruta_imagen):
    """
    Obtiene una máscara aproximada de fisuras oscuras usando:
    1. escala de grises;
    2. CLAHE;
    3. transformación black-hat;
    4. umbral de Otsu;
    5. operaciones morfológicas;
    6. filtrado de componentes pequeños.

    Esta segmentación es heurística, porque SDNET2018 no proporciona
    máscaras reales de fisura.
    """

    imagen_bgr = cv2.imread(str(ruta_imagen))

    if imagen_bgr is None:
        raise ValueError(
            f"No se pudo leer la imagen: {ruta_imagen}"
        )

    gris = cv2.cvtColor(
        imagen_bgr,
        cv2.COLOR_BGR2GRAY
    )

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    gris_mejorado = clahe.apply(gris)

    kernel_blackhat = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (15, 15)
    )

    blackhat = cv2.morphologyEx(
        gris_mejorado,
        cv2.MORPH_BLACKHAT,
        kernel_blackhat
    )

    blackhat = cv2.GaussianBlur(
        blackhat,
        (3, 3),
        0
    )

    _, mascara = cv2.threshold(
        blackhat,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    kernel_apertura = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (3, 3)
    )

    mascara = cv2.morphologyEx(
        mascara,
        cv2.MORPH_OPEN,
        kernel_apertura
    )

    kernel_cierre = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        (3, 3)
    )

    mascara = cv2.morphologyEx(
        mascara,
        cv2.MORPH_CLOSE,
        kernel_cierre
    )

    mascara = eliminar_componentes_pequenos(
        mascara,
        area_minima=20
    )

    return imagen_bgr, mascara


# ============================================================
# 34. MEDICIÓN DEL ESPESOR DE FISURA
# ============================================================

def medir_espesor_fisura(
    mascara,
    mm_por_pixel=60.0/256.0
):
    """
    Calcula el espesor local mediante:
    - transformada de distancia;
    - esqueletización;
    - ancho local = 2 x distancia al borde.

    Devuelve mediana, promedio, percentil 95 y máximo.
    El percentil 95 es generalmente más estable que el máximo.
    """

    mascara_binaria = (
        mascara > 0
    ).astype(np.uint8)

    if mascara_binaria.sum() == 0:
        return {
            "espesor_mediano_px": 0.0,
            "espesor_promedio_px": 0.0,
            "espesor_p95_px": 0.0,
            "espesor_maximo_px": 0.0,
            "espesor_mediano_mm": None,
            "espesor_promedio_mm": None,
            "espesor_p95_mm": None,
            "espesor_maximo_mm": None,
            "pixeles_esqueleto": 0
        }

    distancia = cv2.distanceTransform(
        mascara_binaria,
        cv2.DIST_L2,
        5
    )

    esqueleto = skeletonize(
        mascara_binaria.astype(bool)
    )

    espesores_px = (
        2.0 * distancia[esqueleto]
    )

    espesores_px = espesores_px[
        espesores_px > 0
    ]

    if espesores_px.size == 0:
        return {
            "espesor_mediano_px": 0.0,
            "espesor_promedio_px": 0.0,
            "espesor_p95_px": 0.0,
            "espesor_maximo_px": 0.0,
            "espesor_mediano_mm": None,
            "espesor_promedio_mm": None,
            "espesor_p95_mm": None,
            "espesor_maximo_mm": None,
            "pixeles_esqueleto": 0
        }

    resultados = {
        "espesor_mediano_px": float(
            np.median(espesores_px)
        ),
        "espesor_promedio_px": float(
            np.mean(espesores_px)
        ),
        "espesor_p95_px": float(
            np.percentile(espesores_px, 95)
        ),
        "espesor_maximo_px": float(
            np.max(espesores_px)
        ),
        "pixeles_esqueleto": int(
            espesores_px.size
        )
    }

    if mm_por_pixel is not None:
        resultados.update({
            "espesor_mediano_mm":
                resultados["espesor_mediano_px"]
                * mm_por_pixel,

            "espesor_promedio_mm":
                resultados["espesor_promedio_px"]
                * mm_por_pixel,

            "espesor_p95_mm":
                resultados["espesor_p95_px"]
                * mm_por_pixel,

            "espesor_maximo_mm":
                resultados["espesor_maximo_px"]
                * mm_por_pixel
        })
    else:
        resultados.update({
            "espesor_mediano_mm": None,
            "espesor_promedio_mm": None,
            "espesor_p95_mm": None,
            "espesor_maximo_mm": None
        })

    return resultados


def crear_superposicion(
    imagen_bgr,
    mascara
):
    """
    Crea una imagen de control visual con la máscara superpuesta.
    """

    superposicion = imagen_bgr.copy()

    capa = np.zeros_like(imagen_bgr)
    capa[:, :, 2] = mascara

    superposicion = cv2.addWeighted(
        superposicion,
        0.75,
        capa,
        0.45,
        0
    )

    return superposicion


# ============================================================
# 35. MEDIR ESPESOR EN LAS IMÁGENES PREDICHAS CON FISURA
# ============================================================

print("\n" + "=" * 60)
print("ESTIMACIÓN DEL ESPESOR DE FISURAS")
print("=" * 60)

RUTA_SUPERPOSICIONES = (
    RUTA_RESULTADOS / "superposiciones_fisuras"
)

RUTA_SUPERPOSICIONES.mkdir(
    parents=True,
    exist_ok=True
)

registros_espesor = []

imagenes_predichas_con_fisura = df_resultados_prueba[
    df_resultados_prueba["prediccion"] == 1
].copy()

print(
    "Imágenes de prueba predichas con fisura: "
    f"{len(imagenes_predichas_con_fisura)}"
)

for numero, (_, fila) in enumerate(
    imagenes_predichas_con_fisura.iterrows(),
    start=1
):
    ruta_imagen = Path(fila["ruta_limpia"])

    try:
        imagen_bgr, mascara = segmentar_fisura(
            ruta_imagen
        )

        medicion = medir_espesor_fisura(
            mascara,
            mm_por_pixel=MM_POR_PIXEL
        )

        registro = {
            "archivo": fila["archivo"],
            "ruta_limpia": str(ruta_imagen),
            "elemento": fila["elemento"],
            "etiqueta_real": int(fila["etiqueta"]),
            "prediccion": int(fila["prediccion"]),
            "probabilidad_fisura": float(
                fila["probabilidad_fisura"]
            ),
            **medicion
        }

        registros_espesor.append(registro)

        superposicion = crear_superposicion(
            imagen_bgr,
            mascara
        )

        nombre_salida = (
            f"{numero:05d}_{ruta_imagen.stem}_overlay.jpg"
        )

        cv2.imwrite(
            str(
                RUTA_SUPERPOSICIONES
                / nombre_salida
            ),
            superposicion
        )

    except Exception as error:
        registros_espesor.append({
            "archivo": fila["archivo"],
            "ruta_limpia": str(ruta_imagen),
            "elemento": fila["elemento"],
            "etiqueta_real": int(fila["etiqueta"]),
            "prediccion": int(fila["prediccion"]),
            "probabilidad_fisura": float(
                fila["probabilidad_fisura"]
            ),
            "error": str(error)
        })

    if numero % 100 == 0:
        print(
            f"{numero} imágenes con fisura procesadas..."
        )


df_espesores = pd.DataFrame(registros_espesor)

df_espesores.to_csv(
    RUTA_RESULTADOS / "espesores_fisuras.csv",
    index=False,
    encoding="utf-8-sig"
)

print(
    "\nResultados de espesor guardados en:\n"
    f"{RUTA_RESULTADOS / 'espesores_fisuras.csv'}"
)


# ============================================================
# 36. PREDICCIÓN Y MEDICIÓN DE UNA IMAGEN NUEVA
# ============================================================

def predecir_imagen_nueva(
    ruta_imagen,
    modelo_entrenado,
    umbral=0.50,
    mm_por_pixel=None,
    guardar_resultado=True
):
    """
    Recibe una imagen nueva y devuelve:
    - probabilidad de fisura;
    - clase predicha;
    - espesor estimado si se detecta fisura.
    """

    ruta_imagen = Path(ruta_imagen)

    if not ruta_imagen.exists():
        raise FileNotFoundError(
            f"No existe la imagen: {ruta_imagen}"
        )

    imagen = tf.keras.utils.load_img(
        ruta_imagen,
        target_size=TAMANO_IMAGEN,
        color_mode="rgb"
    )

    arreglo = tf.keras.utils.img_to_array(
        imagen
    ) / 255.0

    arreglo = np.expand_dims(
        arreglo,
        axis=0
    )

    probabilidad = float(
        modelo_entrenado.predict(
            arreglo,
            verbose=0
        )[0][0]
    )

    prediccion = int(
        probabilidad >= umbral
    )

    resultado = {
        "ruta": str(ruta_imagen),
        "probabilidad_fisura": probabilidad,
        "prediccion": prediccion,
        "clase": (
            "Con fisura"
            if prediccion == 1
            else "Sin fisura"
        )
    }

    if prediccion == 1:
        imagen_bgr, mascara = segmentar_fisura(
            ruta_imagen
        )

        medicion = medir_espesor_fisura(
            mascara,
            mm_por_pixel=mm_por_pixel
        )

        resultado.update(medicion)

        if guardar_resultado:
            superposicion = crear_superposicion(
                imagen_bgr,
                mascara
            )

            ruta_salida = (
                RUTA_RESULTADOS
                / f"prediccion_{ruta_imagen.stem}_overlay.jpg"
            )

            cv2.imwrite(
                str(ruta_salida),
                superposicion
            )

            resultado["ruta_superposicion"] = str(
                ruta_salida
            )

    return resultado


# EJEMPLO DE USO DESPUÉS DEL ENTRENAMIENTO:
#
# resultado_nuevo = predecir_imagen_nueva(
#     ruta_imagen=r"D:\MIS_IMAGENES\fisura_01.jpg",
#     modelo_entrenado=mejor_modelo,
#     umbral=UMBRAL_CLASIFICACION,
#     mm_por_pixel=MM_POR_PIXEL
# )
#
# print(resultado_nuevo)


# ============================================================
# 37. RESUMEN FINAL DE ARCHIVOS GENERADOS
# ============================================================

print("\n" + "=" * 60)
print("TAREA 3 COMPLETADA")
print("=" * 60)

print(
    "\nArchivos principales generados:"
    f"\n- Modelo final: {RUTA_MODELO}"
    f"\n- Mejor modelo: {RUTA_MEJOR_MODELO}"
    f"\n- Métricas: {RUTA_RESULTADOS / 'metricas_finales.json'}"
    f"\n- Reporte: {RUTA_RESULTADOS / 'reporte_clasificacion.txt'}"
    f"\n- Predicciones: {RUTA_RESULTADOS / 'predicciones_prueba.csv'}"
    f"\n- Espesores: {RUTA_RESULTADOS / 'espesores_fisuras.csv'}"
    f"\n- Superposiciones: {RUTA_SUPERPOSICIONES}"
)

if MM_POR_PIXEL is None:
    print(
        "\nADVERTENCIA METROLÓGICA:"
        "\nLos espesores se reportan en píxeles."
        "\nPara obtener milímetros debes definir MM_POR_PIXEL"
        "\nmediante una calibración física verificable."
    )

print("\nProceso de Tarea 3 terminado correctamente.")
