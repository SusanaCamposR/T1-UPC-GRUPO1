# SDNET2018 - Detección de Fisuras mediante Redes Neuronales Convolucionales (CNN)

## Descripción

Este proyecto implementa un flujo completo para la detección automática de fisuras en elementos de concreto utilizando el dataset **SDNET2018** y una Red Neuronal Convolucional (CNN) desarrollada con TensorFlow/Keras.

El proyecto contempla desde el análisis exploratorio del dataset hasta la predicción de nuevas imágenes y la estimación del espesor de las fisuras detectadas.

---

# Objetivos

- Analizar la estructura del dataset SDNET2018.
- Detectar imágenes corruptas.
- Normalizar todas las imágenes.
- Construir un inventario completo del dataset.
- Entrenar una CNN para clasificación binaria.
- Evaluar el modelo mediante métricas de desempeño.
- Detectar fisuras en imágenes nuevas.
- Estimar geométricamente el espesor de las fisuras.

---

# Dataset

Se utiliza el dataset público:

**SDNET2018**

Clasificación:

- Deck (Puentes)
- Wall (Muros)
- Pavement (Pavimentos)

Cada categoría contiene imágenes:

- Con fisura
- Sin fisura

---

# Tecnologías utilizadas

- Python 3.x
- TensorFlow / Keras
- OpenCV
- NumPy
- Pandas
- Matplotlib
- Pillow (PIL)
- Scikit-Learn
- Scikit-Image

---

# Flujo del proyecto

## 1. Verificación del dataset

El programa verifica automáticamente:

- Existencia de carpetas
- Integridad del dataset
- Imágenes corruptas

---

## 2. Análisis Exploratorio (EDA)

Se obtiene información como:

- Número de imágenes
- Distribución por clases
- Distribución por elemento estructural
- Resoluciones
- Formatos
- Tamaños
- Modos de color

También genera gráficos automáticos.

---

## 3. Limpieza del dataset

Todas las imágenes son convertidas a:

- RGB
- JPEG
- 256×256 píxeles

Las imágenes limpias se almacenan en un nuevo directorio.

---

## 4. División del dataset

Se realiza una división estratificada:

- 70% Entrenamiento
- 15% Validación
- 15% Prueba

---

## 5. Balanceo de clases

Se calculan automáticamente los pesos mediante:

```python
compute_class_weight()
```

para reducir el efecto del desbalance entre imágenes con y sin fisuras.

---

## 6. Aumento de datos (Data Augmentation)

Durante el entrenamiento se aplican:

- Rotaciones
- Zoom
- Cambios de contraste
- Volteo horizontal
- Volteo vertical

---

## 7. Arquitectura CNN

La red está compuesta por:

- Conv2D
- BatchNormalization
- MaxPooling
- GlobalAveragePooling
- Dropout
- Capa Sigmoid

La salida corresponde a una clasificación binaria:

- 0 → Sin fisura
- 1 → Con fisura

---

## 8. Entrenamiento

Se utilizan:

- EarlyStopping
- ModelCheckpoint
- ReduceLROnPlateau
- CSVLogger

para evitar sobreajuste y conservar el mejor modelo.

---

## 9. Evaluación

El proyecto calcula automáticamente:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Además genera:

- Matriz de confusión
- Reporte de clasificación

---

## 10. Predicción

El sistema permite analizar imágenes nuevas indicando:

- Probabilidad de fisura
- Clase predicha
- Imagen superpuesta
- Segmentación

---

## 11. Segmentación de fisuras

Se implementa una segmentación heurística utilizando:

- CLAHE
- Black-Hat Morphology
- Otsu Threshold
- Operaciones morfológicas
- Eliminación de ruido

---

## 12. Medición del espesor

Para cada fisura detectada se estima:

- Espesor promedio
- Espesor mediano
- Espesor máximo
- Percentil 95

Los resultados se entregan inicialmente en píxeles y pueden convertirse a milímetros mediante una calibración física.

---

# Archivos generados

Durante la ejecución se crean automáticamente:

```
inventario_sdnet2018.csv

imagenes_corruptas.csv

modelo_cnn_sdnet2018.keras

mejor_modelo_cnn_sdnet2018.keras

metricas_finales.json

reporte_clasificacion.txt

predicciones_prueba.csv

espesores_fisuras.csv

historial_entrenamiento.csv

matriz_confusion.png

historial_loss.png

historial_accuracy.png

historial_recall.png

historial_auc.png

superposiciones_fisuras/
```

---

# Estructura del proyecto

```
Proyecto/

│
├── SDNET2018/
│
├── SDNET2018_LIMPIO/
│
├── RESULTADOS_TAREA3/
│
├── TAREA3_SDNET2018.py
│
└── README.md
```

---

# Requisitos

Instalar dependencias:

```bash
pip install tensorflow
pip install opencv-python
pip install pillow
pip install pandas
pip install matplotlib
pip install numpy
pip install scikit-image
pip install scikit-learn
```

o mediante:

```bash
pip install -r requirements.txt
```

---

# Ejecución

Modificar primero la ruta del dataset:

```python
RUTA_DATASET = Path(r"D:\SDNET2018")
```

Posteriormente ejecutar:

```bash
python TAREA3_SDNET2018.py
```

---

# Resultados

El modelo produce:

- Clasificación automática de fisuras.
- Métricas de desempeño.
- Segmentación aproximada de las grietas.
- Estimación del espesor.
- Visualizaciones y reportes para el análisis de resultados.

---

# Autores
Susana Campos Rodriguez.
Carlos .
Renzo.
Jaime Jesús Ramírez Elera.

Ingeniero Civil

Especialización en Ingeniería Estructural

---

# Licencia

Proyecto desarrollado con fines académicos e investigación utilizando el dataset público SDNET2018.
