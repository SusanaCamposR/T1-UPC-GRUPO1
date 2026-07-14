# 📑 INFORME DE TRABAJO N° 2
### **Tema:** Análisis Exploratorio y Plan Algorítmico

**Presentado por:**
* 👤 **Susana Abigail Campos Rodríguez**
* 👤 **Carlos Teodoro Barreda Guzmán**
* 👤 **Jaime Jesus Ramírez Elera**
* 👤 **Renzo Salleres Untiveros**

---

# 📊 TAREA 2: ANÁLISIS EXPLORATORIO Y PLAN ALGORÍTMICO

## **I. Análisis Exploratorio de Datos (EDA)
### **Objetivo:** Verificar la calidad de los datos y definir los modelos de ML/IA a implementar.

El desarrollo de esta etapa se centra en el **Análisis Exploratorio de Datos (EDA)**, la limpieza de las imágenes, el manejo de valores nulos y la visualización inicial de la data utilizando librerías fundamentales de Python como `Pandas`, `Matplotlib` y `PIL`.

---

## 🛠️ 1.1. Limpieza y Preprocesamiento

Para automatizar la auditoría de calidad del dataset **SDNET2018**, se implementó un script en Python que realiza las siguientes funciones:
1. **Verificación de Estructura:** Comprobación de la existencia de las subcarpetas del dataset (`DECK`, `MURO`, `PAVIMENTO`).
2. **Validación de Integridad:** Apertura de cada imagen mediante `PIL` para detectar y descartar archivos corruptos (`UnidentifiedImageError`).
3. **Mapeo de Etiquetas:** Clasificación binaria (0: Sin grieta, 1: Con grieta) y segmentación por elemento estructural.
4. **Normalización Visual:** Conversión forzada a tres canales **RGB** y reescalado uniforme a una resolución de **256 x 256 píxeles**.

> ⚠️ **Nota de Infraestructura:** El script genera un nuevo directorio optimizado llamado `SDNET2018_LIMPIO`, aislando los datos corruptos y guardando un inventario consolidado en un archivo `.csv` para asegurar la **Computabilidad** del modelo.

---

## 📈 1.2. Resultados del Análisis Exploratorio (EDA)

Luego de ejecutar nuestro pipeline sobre el volumen total de datos, se obtuvieron las siguientes métricas de control de calidad:

### 📋 Cuadro de Control y Valores Nulos
| Métrica Evaluada | Cantidad Registrada | Observación / Estado |
| :--- | :---: | :--- |
| **Imágenes Originales Válidas** | *[56092]* | Listas para el preprocesamiento |
| **Imágenes Corruptas Detectadas** | *[0]* | Removidas del conjunto activo |
| **Valores Nulos Detectados (Missing)**| `0` | Base de datos limpia sin vacíos |

### 🗂️ Distribución de Imágenes por Estado (Balance de Clases)
| Estado de la Superficie | Código de Carpeta | N° de Imágenes | Porcentaje (%) |
| :--- | :---: | :---: | :---: |
| 🔴 **Con Grieta (Cracked)** | CD / CW / CP | *[8484]* | *[84.87%]* |
| 🟢 **Sin Grieta (Uncracked)** | UD / UW / UP | *[47608]* | *[15.13%]* |

### 🏗️ Segmentación por Elemento Estructural
| Elemento Estructural | Con Grieta (1) | Sin Grieta (0) | Total por Elemento |
| :--- | :---: | :---: | :---: |
| 🌉 **Tablero de Puente (Deck)** | *[2025]* | *[11595]* | *[13620]* |
| 🧱 **Muro (Wall)** | *[2608]* | *[21726]* | *[24334]* |
| 🛣️ **Pavimento (Pavement)** | *[3851]* | *[14287]* | *[18138]* |

---

## 🖼️ 1.3. Reportes Gráficos del Dataset

*Los siguientes diagramas estadísticos fueron generados automáticamente mediante `Matplotlib` y reflejan las proporciones estructurales del dataset:*

| Distribución por Carpetas | Balance de Clases (Estado) | Análisis por Elemento |
| :---: | :---: | :---: |
| ![Carpetas](./grafico_imagenes_por_carpeta.png) | ![Estado](./grafico_estado_grieta.png) | ![Elementos](./grafico_elemento_estado.png) |

*(Nota: Asegúrate de arrastrar y soltar los archivos `.png` de tus gráficos dentro de la carpeta de GitHub para que las imágenes de arriba carguen correctamente).*

## 🖼️ 1.4. Reportes Gráficos del Dataset

---

  
## **II. 🏗️ Plan de Algoritmos para la Detección de Fisuras en Concreto

## 📌 Descripción del proyecto

Para el desarrollo del proyecto se propone utilizar una **Red Neuronal Convolucional (CNN)** como algoritmo principal.
La selección de este método responde a las características del problema planteado y al tipo de datos disponibles en el dataset **SDNET2018**, compuesto por imágenes de superficies de concreto con y sin presencia de fisuras.

El objetivo del proyecto es detectar automáticamente la presencia de fisuras, con la finalidad de contribuir a la priorización de la inspección visual de las zonas identificadas.

---

## 🧠 1. Red Neuronal Convolucional (CNN)

La **Red Neuronal Convolucional (CNN)** será utilizada como modelo principal de **aprendizaje supervisado** para la clasificación binaria de las imágenes en dos categorías:

* 🔴 **Con fisura (`Cracked`)**
* 🟢 **Sin fisura (`Uncracked`)**

Este algoritmo resulta adecuado debido a su capacidad para procesar imágenes y aprender automáticamente características visuales relevantes, tales como:

* Bordes.
* Texturas.
* Contornos.
* Formas.
* Patrones asociados con la presencia de fisuras.

### 📥 Variables de entrada

Las variables de entrada estarán constituidas por la información visual contenida en las imágenes, incluyendo:

* Valores de intensidad de los píxeles RGB.
* Textura superficial.
* Bordes y contornos.
* Forma y orientación de las fisuras.
* Contraste.
* Iluminación.
* Ruido visual.

### 📤 Variable de salida

> **Presencia o ausencia de fisura.**

### 🔍 Justificación del uso de CNN

La elección de una **CNN** se justifica porque las fisuras presentan patrones espaciales y geométricos que pueden variar en forma, orientación y apariencia.

Asimismo, las imágenes del dataset **SDNET2018** contienen condiciones visuales complejas, como sombras, rugosidad superficial, bordes, agujeros y residuos de fondo.

Por ello, se requiere un modelo capaz de aprender características relevantes directamente a partir de las imágenes y generalizar ante diferentes condiciones de inspección.

---

## 🔄 3. Flujo general propuesto

```text
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
│      EXTRACCIÓN DE CARACTERÍSTICAS      │
│              DE LA FISURA               │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│     AGRUPAMIENTO POR CARACTERÍSTICAS    │
└────────────────────-────────────────────┘

```

---

## 🧩 4. Justificación de la selección

Este algoritmo permite abordar todo el problema.

### 🔹 Red Neuronal Convolucional (CNN)

La **CNN** resuelve la tarea principal de detección automática de fisuras mediante técnicas de visión artificial.

La metodología propuesta busca superar una clasificación limitada a:

> **Fisura / No fisura**


---

## 🎯 5. Objetivo propuesto

> **Desarrollar una propuesta de modelo de visión artificial para detectar fisuras visibles en superficies de concreto utilizando el dataset SDNET2018, mediante una Red Neuronal Convolucional (CNN).**

---

## 🛠️ Tecnologías y algoritmos propuestos

* **Python**
* **Redes Neuronales Convolucionales (CNN)**
* **Visión artificial**
* **Machine Learning**
* **Dataset SDNET2018**

---

## 📚 Dataset

El proyecto utilizará el dataset **SDNET2018**, compuesto por imágenes de superficies de concreto que incluyen muestras con y sin presencia de fisuras.

---

## 👷 Área de aplicación

**Ingeniería Civil | Ingeniería Estructural | Inteligencia Artificial | Inspección de estructuras**
