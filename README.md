# 🏛️ Universidad Peruana de Ciencias Aplicadas
## **Curso:** Aplicaciones de IA en Estructuras

---

# 📑 INFORME DE TRABAJO N° 1
### **Tema:** Definición del Problema, Datos y Repositorio

**Presentado por:**
* 👤 **Susana Abigail Campos Rodríguez**
* 👤 **Carlos Teodoro Barreda Guzmán**
* 👤 **Jaime Jesus Ramírez Elera**
* 👤 **Renzo Salleres Untiveros**

---

## 🔍 1. Definición del Problema
### **Descripción del problema de ingeniería estructural a resolver**

La infraestructura de concreto, presente en puentes, pavimentos, muros y edificaciones, está expuesta continuamente a cargas mecánicas, variaciones climáticas y procesos de deterioro que pueden generar fisuras superficiales. La identificación temprana de estas fisuras es fundamental para prevenir daños mayores y planificar intervenciones de mantenimiento oportunas.

Sin embargo, las inspecciones tradicionales dependen de evaluaciones visuales realizadas por especialistas, lo que puede demandar una gran cantidad de tiempo, recursos y personal técnico, especialmente en infraestructuras de gran extensión.

> 💡 **Propuesta del Proyecto:** > Frente a esta problemática, el presente proyecto propone el uso de técnicas de **Machine Learning Supervisado** y **visión artificial** para automatizar la detección de fisuras en superficies de concreto mediante el análisis de imágenes del dataset **SDNET2018**, contribuyendo a mejorar la eficiencia y objetividad de los procesos de inspección estructural.

### 🎯 Objetivo del Proyecto
Desarrollar una propuesta de modelo supervisado de visión artificial para detectar fisuras visibles en concreto usando el dataset SDNET2018, con énfasis en su posible uso como herramienta de preinspección en mantenimiento estructural.

* **Agrupamiento por espesor:** Se propone clasificar las imágenes agrupándolas en función del espesor de la fisura encontrada, usando uno de los algoritmos enseñados en clase (`K-means`, `DBScan` o `Kernel PCA`).
* **Asignación de severidad:** La asignación del tipo de fisura (**leve, mediana o moderada**) será en función del espesor de las mismas.

---

## 📊 2. Datos del Proyecto (Dataset)

El dataset **SDNET2018** es un conjunto de datos anotado para entrenamiento, validación y comparación de algoritmos de inteligencia artificial orientados a la detección de fisuras en concreto. 

Según la página oficial del dataset en *DigitalCommons@USU*, contiene más de **56,000 imágenes** de superficies de concreto con y sin fisuras. Fue publicado por autores asociados a *Utah State University* para el desarrollo de algoritmos mediante redes neuronales convolucionales (CNN). Las imágenes incluyen obstáculos reales como sombras, rugosidad superficial, bordes, agujeros y residuos de fondo.

### 📋 Ficha Técnica del Dataset

| Elemento | Descripción |
| :--- | :--- |
| **Nombre** | SDNET2018: Concrete Crack Image Dataset |
| **Fuente** | DigitalCommons@USU: [Enlace al Dataset](https://digitalcommons.usu.edu/all_datasets/48/) |
| **Tipo de datos** | Imágenes JPEG clasificadas en presencia o ausencia de fisura. |
| **Escenarios** | Tableros de puente, muros y pavimentos de concreto. |
| **Resolución** | 256 x 256 píxeles, según la descripción del dataset. |
| **Uso en el proyecto** | Entrenamiento y evaluación de una **CNN** (*Convolutional Neural Network*) para clasificación visual supervisada. |

---

## 🔀 3. Variables del Modelo

### 🔴 Variable Dependiente
* **Presencia de fisura en la superficie de concreto:** Es una variable categórica binaria que indica si una imagen pertenece a la clase `Cracked` (con fisura) o `Uncracked` (sin fisura). Esta es la variable principal que la CNN intentará predecir.

| Tipo de Variable | Nombre | Descripción |
| :--- | :--- | :--- |
| **Dependiente Principal** | Presencia de fisura | Con fisura (1) / Sin fisura (0) |
| **Dependiente Secundaria** | IPIV | Índice de Prioridad de Inspección Visual calculado a partir de la salida del modelo. |

### 🟢 Variables Independientes
Son las características visuales y numéricas que la red neuronal extraerá automáticamente de cada imagen:

| Variable Independiente | Descripción |
| :--- | :--- |
| **Intensidad de píxeles RGB** | Valores numéricos de color presentes en cada imagen. |
| **Textura superficial** | Patrones visuales de la superficie de concreto. |
| **Bordes y contornos** | Discontinuidades detectadas automáticamente por la CNN. |
| **Forma y orientación** | Características geométricas de posibles grietas. |
| **Contraste e iluminación** | Variaciones de brillo, sombras y condiciones de captura. |
| **Ruido visual** | Presencia de suciedad, bordes, agujeros o rugosidad superficial. |

---

## 🚀 4. Enfoque Original: Índice de Prioridad (IPIV)

Para diferenciar esta propuesta de otros grupos, el proyecto no se limitará a entregar un clasificador binario estándar. 

El aporte particular será el diseño de un **Índice de Prioridad de Inspección Visual (IPIV)** basado en el espesor estimado de la fisura. Este índice ordenará las imágenes según el nivel de urgencia, sirviendo como herramienta de toma de decisiones para los equipos técnicos en campo.

### 📐 Clasificación Propuesta según Espesor

| Categoría | Espesor Estimado de Fisura | Nivel de Prioridad |
| :--- | :--- | :--- |
| 🟢 **Fisura leve** | 0.06 mm – 1 mm | Baja |
| 🟡 **Fisura moderada** | >1 mm – 5 mm | Media |
| 🟠 **Fisura severa** | >5 mm – 15 mm | Alta |
| 🔴 **Fisura crítica** | >15 mm – 25 mm | Muy alta |

---

## ⚖️ 5. Marco VDS (Veridical Data Science) - Principios PCS

El proyecto se alinea bajo el marco regulatorio **VDS** (*Predictability, Computability, Stability*) propuesto por Yu & Barter (2024) para garantizar la confianza de la solución:

| Principio PCS | Aplicación en este Proyecto | Justificación |
| :--- | :--- | :--- |
| **Predictability** (Predictibilidad) | Evaluar la capacidad del modelo para identificar correctamente imágenes con fisuras. | En inspección estructural, un falso negativo puede retrasar catastróficamente la revisión de una zona dañada. |
| **Computability** (Computabilidad) | Usar modelos entrenables y ejecutables en equipos con recursos moderados. | El modelo debe ser viable para estudiantes o instituciones sin infraestructura computacional avanzada (computación en la nube accesible). |
| **Stability** (Estabilidad) | Comparar resultados por tipo de superficie (puente, muro y pavimento), además de probar distintas semillas y particiones. | Un modelo confiable no debe funcionar solo en un subconjunto "fácil" ni depender de una única división de datos. |

## 📚 6. Referencias Bibliográficas

* 📖 **Yu, B., & Barter, R. (2024).** *Veridical Data Science: The PCS Framework.* MIT Press. https://vdsbook.com/
* 📊 **Maguire, M., Dorafshan, S., & Thomas, R. J. (2018).** *SDNET2018: A concrete crack image dataset for machine learning applications.* Utah State University. https://doi.org/10.15142/T3TD19



# 📑 INFORME DE TRABAJO N° 2
### **Tema:** Análisis Exploratorio y Plan Algorítmico

**Presentado por:**
* 👤 **Susana Abigail Campos Rodríguez**
* 👤 **Carlos Teodoro Barreda Guzmán**
* 👤 **Jaime Jesus Ramírez Elera**
* 👤 **Renzo Salleres Untiveros**

---
---

# 📊 TAREA 2: ANÁLISIS EXPLORATORIO Y PLAN ALGORÍTMICO
### **Objetivo:** Verificar la calidad de los datos y definir los modelos de ML/IA a implementar.

El desarrollo de esta etapa se centra en el **Análisis Exploratorio de Datos (EDA)**, la limpieza de las imágenes, el manejo de valores nulos y la visualización inicial de la data utilizando librerías fundamentales de Python como `Pandas`, `Matplotlib` y `PIL`.

---

## 🛠️ 1. Pipeline de Limpieza y Preprocesamiento

Para automatizar la auditoría de calidad del dataset **SDNET2018**, se implementó un script en Python que realiza las siguientes funciones:
1. **Verificación de Estructura:** Comprobación de la existencia de las subcarpetas del dataset (`DECK`, `MURO`, `PAVIMENTO`).
2. **Validación de Integridad:** Apertura de cada imagen mediante `PIL` para detectar y descartar archivos corruptos (`UnidentifiedImageError`).
3. **Mapeo de Etiquetas:** Clasificación binaria (0: Sin grieta, 1: Con grieta) y segmentación por elemento estructural.
4. **Normalización Visual:** Conversión forzada a tres canales **RGB** y reescalado uniforme a una resolución de **256 x 256 píxeles**.

> ⚠️ **Nota de Infraestructura:** El script genera un nuevo directorio optimizado llamado `SDNET2018_LIMPIO`, aislando los datos corruptos y guardando un inventario consolidado en un archivo `.csv` para asegurar la **Computabilidad** del modelo.

---

## 🐍 2. Código Fuente de la Implementación (Python)

A continuación, se presenta el script completo utilizado para la limpieza, análisis estadístico y generación de gráficos descriptivos del dataset:

```python
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
RUTA_DATASET = Path(r"D:\SDNET2018")
RUTA_LIMPIA = RUTA_DATASET.parent / "SDNET2018_LIMPIO"

ANCHO_OBJETIVO = 256
ALTO_OBJETIVO = 256
EXTENSIONES_VALIDAS = {".jpg", ".jpeg", ".png"}

# Mapeo de subcarpetas y etiquetas estructurales
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
# 2. VERIFICACIÓN DE LA ESTRUCTURA DE CARPETAS
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
# 3. LECTURA Y VERIFICACIÓN DE LAS IMÁGENES
# ============================================================
registros = []
imagenes_corruptas = []

print("\n" + "=" * 60)
print("LEYENDO Y VERIFICANDO IMÁGENES")
print("=" * 60)

for codigo_clase, carpeta in CARPETAS.items():
    elemento, estado, etiqueta = CLASES[codigo_clase]
    archivos = [
        archivo for archivo in carpeta.iterdir()
        if archivo.is_file() and archivo.suffix.lower() in EXTENSIONES_VALIDAS
    ]
    
    print(f"\nProcesando {codigo_clase}: {len(archivos)} archivos")
    
    for numero, ruta_imagen in enumerate(archivos, start=1):
        try:
            with Image.open(ruta_imagen) as imagen:
                imagen.verify()
            
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
        except (UnidentifiedImageError, OSError, ValueError) as error:
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
# 4. ANÁLISIS EXPLORATORIO DE DATOS (EDA)
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

# Verificación de Nulos
valores_nulos = df.isnull().sum()
print("\nValores nulos por columna:\n", valores_nulos)

# Distribuciones Estadísticas
conteo_carpetas = df["carpeta"].value_counts().sort_index()
conteo_estado = df["estado"].value_counts()
tabla_elementos = pd.crosstab(df["elemento"], df["estado"])
resoluciones = df.groupby(["ancho_px", "alto_px"]).size().reset_index(name="cantidad")

df["tamaño_kb"] = df["tamaño_bytes"] / 1024
print("\nEstadísticas del tamaño de archivos en KB:\n", df["tamaño_kb"].describe())

# ============================================================
# 5. GENERACIÓN DE REPORTES VISUALES
# ============================================================
# Gráfico 1: Imágenes por Carpeta
plt.figure(figsize=(9, 5))
conteo_carpetas.plot(kind="bar")
plt.title("Cantidad de imágenes por carpeta")
plt.xlabel("Carpeta")
plt.ylabel("Número de imágenes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(RUTA_DATASET / "grafico_imagenes_por_carpeta.png", dpi=300)
plt.close()

# Gráfico 2: Distribución por Estado
plt.figure(figsize=(7, 5))
conteo_estado.plot(kind="bar")
plt.title("Distribución de imágenes por estado")
plt.xlabel("Estado")
plt.ylabel("Número de imágenes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(RUTA_DATASET / "grafico_estado_grieta.png", dpi=300)
plt.close()

# Gráfico 3: Elemento vs Estado
tabla_elementos.plot(kind="bar", figsize=(9, 5))
plt.title("Distribución por elemento estructural")
plt.xlabel("Elemento estructural")
plt.ylabel("Número de imágenes")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(RUTA_DATASET / "grafico_elemento_estado.png", dpi=300)
plt.close()

# ============================================================
# 6. EXPORTACIÓN DE INVENTARIOS
# ============================================================
df.to_csv(RUTA_DATASET / "inventario_sdnet2018.csv", index=False, encoding="utf-8-sig")

if imagenes_corruptas:
    pd.DataFrame(imagenes_corruptas).to_csv(
        RUTA_DATASET / "imagenes_corruptas.csv", index=False, encoding="utf-8-sig"
    )

# ============================================================
# 7. PROCESO DE LIMPIEZA Y HOMOGENEIZACIÓN
# ============================================================
print("\n" + "=" * 60)
print("CREANDO DATASET LIMPIO")
print("=" * 60)

if RUTA_LIMPIA.exists():
    shutil.rmtree(RUTA_LIMPIA)
RUTA_LIMPIA.mkdir(parents=True, exist_ok=True)

imagenes_limpiadas = 0
errores_limpieza = []

for indice, fila in df.iterrows():
    ruta_original = Path(fila["ruta"])
    ruta_relativa = ruta_original.relative_to(RUTA_DATASET)
    ruta_destino = RUTA_LIMPIA / ruta_relativa
    
    ruta_destino.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        with Image.open(ruta_original) as imagen:
            imagen = imagen.convert("RGB")
            imagen = imagen.resize((ANCHO_OBJETIVO, ALTO_OBJETIVO))
            imagen.save(ruta_destino, format="JPEG", quality=95)
        imagenes_limpiadas += 1
    except Exception as error:
        errores_limpieza.append({"archivo": ruta_original.name, "error": str(error)})

print("\nProceso terminado correctamente.")



