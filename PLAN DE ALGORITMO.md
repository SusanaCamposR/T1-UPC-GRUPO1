# 🏗️ Plan de Algoritmos para la Detección de Fisuras en Concreto

## 📌 Descripción del proyecto

Para el desarrollo del proyecto se propone utilizar una **Red Neuronal Convolucional (CNN)** como algoritmo principal y **K-means** como algoritmo complementario de agrupamiento.

La selección de ambos métodos responde a las características del problema planteado y al tipo de datos disponibles en el dataset **SDNET2018**, compuesto por imágenes de superficies de concreto con y sin presencia de fisuras.

El objetivo del proyecto es detectar automáticamente la presencia de fisuras y, posteriormente, establecer una agrupación basada en características cuantitativas asociadas a su espesor, con la finalidad de contribuir a la priorización de la inspección visual de las zonas identificadas.

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

## 📊 2. Algoritmo K-means

Como algoritmo complementario se propone utilizar **K-means**, correspondiente a una técnica de **aprendizaje no supervisado**.

Su función será explorar el agrupamiento de las fisuras detectadas a partir de características cuantitativas previamente extraídas, principalmente aquellas asociadas al **espesor estimado de la fisura**.

### 🚦 Niveles de prioridad

Debido a que el proyecto plantea cuatro niveles de prioridad, se evaluará inicialmente una configuración de:

> ### `K = 4 clústeres`

| Clúster | Nivel de prioridad |
| :-----: | :----------------- |
|    1    | 🟢 Leve            |
|    2    | 🟡 Moderada        |
|    3    | 🟠 Severa          |
|    4    | 🔴 Crítica         |

Posteriormente, los grupos obtenidos podrán compararse con los rangos de espesor definidos en el proyecto para analizar la correspondencia entre los patrones identificados por el algoritmo y las categorías propuestas de prioridad de inspección.

> [!IMPORTANT]
> **K-means no detecta ni mide directamente el espesor de una fisura.**

Antes de aplicar el algoritmo será necesaria una etapa de procesamiento y extracción de características que permita obtener una representación cuantitativa de cada fisura.

De esta manera, **K-means** se utilizará para agrupar las observaciones según su similitud y no como un clasificador supervisado con etiquetas predefinidas.

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
│        CLASIFICACIÓN DE LA IMAGEN       │
│          FISURA / SIN FISURA            │
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
│                 K-MEANS                 │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│     AGRUPAMIENTO POR CARACTERÍSTICAS    │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│     NIVEL DE PRIORIDAD DE INSPECCIÓN    │
└─────────────────────────────────────────┘
```

---

## 🧩 4. Justificación de la selección

La combinación de ambos algoritmos permite abordar dos etapas diferentes y complementarias del problema.

### 🔹 Red Neuronal Convolucional (CNN)

La **CNN** resuelve la tarea principal de detección automática de fisuras mediante técnicas de visión artificial.

### 🔹 Algoritmo K-means

**K-means** permite explorar agrupaciones naturales de las fisuras a partir de características cuantitativas asociadas a su espesor.

En conjunto, la metodología propuesta busca superar una clasificación limitada a:

> **Fisura / No fisura**

y proporcionar información adicional que contribuya a establecer un:

> ### Índice de Prioridad de Inspección Visual (IPIV)

El **IPIV** estará orientado a dirigir al equipo técnico hacia las zonas que requieren una revisión prioritaria.

---

## 🎯 5. Objetivo propuesto

> **Desarrollar una propuesta de modelo de visión artificial para detectar fisuras visibles en superficies de concreto utilizando el dataset SDNET2018, mediante una Red Neuronal Convolucional (CNN), y agrupar las fisuras detectadas según características cuantitativas asociadas a su espesor mediante el algoritmo K-means, con la finalidad de establecer niveles de prioridad para la preinspección y el mantenimiento estructural.**

---

## 🛠️ Tecnologías y algoritmos propuestos

* **Python**
* **Redes Neuronales Convolucionales (CNN)**
* **K-means**
* **Visión artificial**
* **Machine Learning**
* **Dataset SDNET2018**

---

## 📚 Dataset

El proyecto utilizará el dataset **SDNET2018**, compuesto por imágenes de superficies de concreto que incluyen muestras con y sin presencia de fisuras.

---

## 👷 Área de aplicación

**Ingeniería Civil | Ingeniería Estructural | Inteligencia Artificial | Inspección de estructuras**
