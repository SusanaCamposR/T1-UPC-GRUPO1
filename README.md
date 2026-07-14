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
