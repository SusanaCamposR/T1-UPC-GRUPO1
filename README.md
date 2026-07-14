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

## 📈 2. Resultados del Análisis Exploratorio (EDA)

Luego de ejecutar nuestro pipeline sobre el volumen total de datos, se obtuvieron las siguientes métricas de control de calidad:

### 📋 Cuadro de Control y Valores Nulos
| Métrica Evaluada | Cantidad Registrada | Observación / Estado |
| :--- | :---: | :--- |
| **Imágenes Originales Válidas** | *[Coloca aquí el total]* | Listas para el preprocesamiento |
| **Imágenes Corruptas Detectadas** | *[Coloca aquí el total]* | Removidas del conjunto activo |
| **Valores Nulos Detectados (Missing)**| `0` | Base de datos limpia sin vacíos |

### 🗂️ Distribución de Imágenes por Estado (Balance de Clases)
| Estado de la Superficie | Código de Carpeta | N° de Imágenes | Porcentaje (%) |
| :--- | :---: | :---: | :---: |
| 🔴 **Con Grieta (Cracked)** | CD / CW / CP | *[Tus datos]* | *[%]* |
| 🟢 **Sin Grieta (Uncracked)** | UD / UW / UP | *[Tus datos]* | *[%]* |

### 🏗️ Segmentación por Elemento Estructural
| Elemento Estructural | Con Grieta (1) | Sin Grieta (0) | Total por Elemento |
| :--- | :---: | :---: | :---: |
| 🌉 **Tablero de Puente (Deck)** | *[Dato CD]* | *[Dato UD]* | *[Suma]* |
| 🧱 **Muro (Wall)** | *[Dato CW]* | *[Dato UW]* | *[Suma]* |
| 🛣️ **Pavimento (Pavement)** | *[Dato CP]* | *[Dato UP]* | *[Suma]* |

---

## 🖼️ 3. Reportes Gráficos del Dataset

*Los siguientes diagramas estadísticos fueron generados automáticamente mediante `Matplotlib` y reflejan las proporciones estructurales del dataset:*

| Distribución por Carpetas | Balance de Clases (Estado) | Análisis por Elemento |
| :---: | :---: | :---: |
| ![Carpetas](./grafico_imagenes_por_carpeta.png) | ![Estado](./grafico_estado_grieta.png) | ![Elementos](./grafico_elemento_estado.png) |

*(Nota: Asegúrate de arrastrar y soltar los archivos `.png` de tus gráficos dentro de la carpeta de GitHub para que las imágenes de arriba carguen correctamente).*

---

## 🐍 4. Código Fuente de la Implementación (Python)

<details>
<summary>👁️ Clic aquí para desplegar el script completo de limpieza</summary>

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

# [Aquí va el código python completo que ya tienes para que el profesor vea tu sustento técnico.
# ==============================================================
# PROYECTO: DETECCIÓN DE FISURAS EN SUPERFICIES DE CONCRETO
# PLAN DE ALGORITMOS: CNN + K-MEANS
# DATASET: SDNET2018
# ==============================================================

# Códigos ANSI para dar formato y color al texto en la terminal
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
BLANCO = "\033[97m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


# ==============================================================
# FUNCIONES DE PRESENTACIÓN
# ==============================================================

def mostrar_titulo(titulo):
    """Muestra el título principal del proyecto."""
    print("\n" + AZUL + NEGRITA + "═" * 72)
    print(titulo.center(72))
    print("═" * 72 + RESET)


def mostrar_seccion(numero, titulo, contenido):
    """Muestra cada sección del plan de algoritmos."""
    print(
        f"\n{CIAN}{NEGRITA}"
        f"{'─' * 72}\n"
        f"{numero}. {titulo}\n"
        f"{'─' * 72}"
        f"{RESET}"
    )
    print(contenido.strip())


def mostrar_lista(titulo, elementos):
    """Muestra una lista de elementos."""
    print(f"\n{AMARILLO}{NEGRITA}{titulo}:{RESET}")

    for elemento in elementos:
        print(f"  • {elemento}")


# ==============================================================
# TÍTULO DEL PROYECTO
# ==============================================================

mostrar_titulo(
    "PLAN DE ALGORITMOS: CNN + K-MEANS"
)

print(f"""
{BLANCO}
Para el desarrollo del proyecto se propone utilizar una Red Neuronal
Convolucional (CNN) como algoritmo principal y K-means como algoritmo
complementario de agrupamiento.

La selección de ambos métodos responde a las características del problema
planteado y al tipo de datos disponibles en el dataset SDNET2018, compuesto
por imágenes de superficies de concreto con y sin presencia de fisuras.

El objetivo del proyecto es detectar automáticamente la presencia de fisuras
y, posteriormente, establecer una agrupación basada en características
cuantitativas asociadas a su espesor, con la finalidad de contribuir a la
priorización de la inspección visual de las zonas identificadas.
{RESET}
""")


# ==============================================================
# 1. RED NEURONAL CONVOLUCIONAL (CNN)
# ==============================================================

mostrar_seccion(
    1,
    "RED NEURONAL CONVOLUCIONAL (CNN)",
    """
La Red Neuronal Convolucional (CNN) será utilizada como modelo principal
de aprendizaje supervisado para la clasificación binaria de las imágenes
en dos categorías:

    ✓ Con fisura (Cracked)
    ✓ Sin fisura (Uncracked)

Este algoritmo resulta adecuado debido a su capacidad para procesar imágenes
y aprender automáticamente características visuales relevantes.
"""
)

mostrar_lista(
    "Características visuales consideradas",
    [
        "Bordes",
        "Texturas",
        "Contornos",
        "Formas",
        "Patrones asociados con la presencia de fisuras"
    ]
)

mostrar_lista(
    "Variables de entrada",
    [
        "Valores de intensidad de los píxeles RGB",
        "Textura superficial",
        "Bordes y contornos",
        "Forma y orientación de las fisuras",
        "Contraste",
        "Iluminación",
        "Ruido visual"
    ]
)

print(
    f"\n{VERDE}{NEGRITA}"
    "VARIABLE DE SALIDA:"
    f"{RESET} Presencia o ausencia de fisura."
)

print("""
La elección de una CNN se justifica porque las fisuras presentan patrones
espaciales y geométricos que pueden variar en forma, orientación y apariencia.

Asimismo, las imágenes del dataset SDNET2018 contienen condiciones visuales
complejas, como sombras, rugosidad superficial, bordes, agujeros y residuos
de fondo.

Por ello, se requiere un modelo capaz de aprender características relevantes
directamente a partir de las imágenes y generalizar ante diferentes
condiciones de inspección.
""")


# ==============================================================
# 2. ALGORITMO K-MEANS
# ==============================================================

mostrar_seccion(
    2,
    "ALGORITMO K-MEANS",
    """
Como algoritmo complementario se propone utilizar K-means, correspondiente
a una técnica de aprendizaje no supervisado.

Su función será explorar el agrupamiento de las fisuras detectadas a partir
de características cuantitativas previamente extraídas, principalmente
aquellas asociadas al espesor estimado de la fisura.
"""
)

mostrar_lista(
    "Niveles de prioridad propuestos",
    [
        "Nivel 1 → LEVE",
        "Nivel 2 → MODERADA",
        "Nivel 3 → SEVERA",
        "Nivel 4 → CRÍTICA"
    ]
)

print(
    f"\n{VERDE}{NEGRITA}"
    "CONFIGURACIÓN INICIAL:"
    f"{RESET} K = 4 clústeres"
)

print("""
Posteriormente, los grupos obtenidos podrán compararse con los rangos de
espesor definidos en el proyecto para analizar la correspondencia entre
los patrones identificados por el algoritmo y las categorías propuestas
de prioridad de inspección.
""")

print(
    f"{AMARILLO}{NEGRITA}"
    "IMPORTANTE:"
    f"{RESET}"
)

print("""
K-means no detecta ni mide directamente el espesor de una fisura.

Antes de aplicar el algoritmo será necesaria una etapa de procesamiento
y extracción de características que permita obtener una representación
cuantitativa de cada fisura.

De esta manera, K-means se utilizará para agrupar las observaciones según
su similitud y no como un clasificador supervisado con etiquetas predefinidas.
""")


# ==============================================================
# 3. FLUJO GENERAL PROPUESTO
# ==============================================================

mostrar_seccion(
    3,
    "FLUJO GENERAL PROPUESTO",
    """
┌─────────────────────────────────────────┐
│          IMAGEN DE CONCRETO             │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│            PREPROCESAMIENTO             │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│     RED NEURONAL CONVOLUCIONAL (CNN)    │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│   CLASIFICACIÓN DE LA IMAGEN            │
│      CON FISURA / SIN FISURA            │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│  EXTRACCIÓN DE CARACTERÍSTICAS          │
│          DE LA FISURA                   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│               K-MEANS                   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│   AGRUPAMIENTO POR CARACTERÍSTICAS      │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ NIVEL DE PRIORIDAD DE INSPECCIÓN        │
└─────────────────────────────────────────┘
"""
)


# ==============================================================
# 4. JUSTIFICACIÓN DE LA SELECCIÓN
# ==============================================================

mostrar_seccion(
    4,
    "JUSTIFICACIÓN DE LA SELECCIÓN",
    """
La combinación de ambos algoritmos permite abordar dos etapas diferentes
y complementarias del problema.

CNN:
Resuelve la tarea principal de detección automática de fisuras mediante
visión artificial.

K-MEANS:
Permite explorar agrupaciones naturales de las fisuras a partir de
características cuantitativas asociadas a su espesor.

En conjunto, la metodología propuesta busca superar una clasificación
limitada a "fisura/no fisura" y proporcionar información adicional que
contribuya a establecer un Índice de Prioridad de Inspección Visual (IPIV).

El IPIV permitirá orientar al equipo técnico hacia las zonas que requieren
una revisión prioritaria.
"""
)



