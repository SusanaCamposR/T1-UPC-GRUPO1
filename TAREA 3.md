<div align="center">

# Detección de Fisuras en Concreto mediante Redes Neuronales Convolucionales (CNN) y Estimación de Espesor

**IEEE TRANSACTIONS ON CIVIL & STRUCTURAL ARTIFICIAL INTELLIGENCE**

<br>

| **Integrantes del Grupo** | **Afiliación y Contacto** |
| :--- | :--- |
| 👤 **Susana Abigail Campos Rodríguez** | Escuela Profesional de Ingeniería Civil / Sistemas |
| 👤 **Carlos Teodoro Barreda Guzmán** | Universidad Nacional del Santa |
| 👤 **Jaime Jesus Ramírez Elera** | Nuevo Chimbote, Ancash, Perú |
| 👤 **Renzo Salleres Untiveros** | *Proyecto de Inspección Estructural Inteligente* |

</div>

---

> ### **Resumen (Abstract)**
> La evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, la durabilidad y la funcionalidad de las edificaciones e infraestructuras civiles. Entre las patologías más frecuentes se encuentran las fisuras, las cuales pueden originarse por fenómenos de retracción, sobrecargas, acciones sísmicas, corrosión del acero de refuerzo o deterioro por agentes ambientales. La detección temprana de estas discontinuidades permite planificar intervenciones oportunas, optimizar los costos de mantenimiento y prolongar la vida útil de las estructuras. En este trabajo se desarrolla un modelo utilizando el conjunto de datos **SDNET2018**, **TensorFlow/Keras** y una **CNN** para la clasificación binaria de imágenes con y sin fisuras, evaluando su desempeño mediante *Accuracy*, *Precision*, *Recall*, *F1-Score* y *AUC*. Adicionalmente, se implementa un procedimiento heurístico basado en procesamiento digital de imágenes para estimar el espesor de las fisuras detectadas.
>
> **Palabras Clave (Keywords) —** *Concreto armado, Detección de fisuras, Redes Neuronales Convolucionales (CNN), Procesamiento Digital de Imágenes, SDNET2018.*

---

## I. INTRODUCCIÓN

La evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, durabilidad y funcionalidad de las edificaciones e infraestructuras civiles. Entre las patologías más frecuentes se encuentran las fisuras, cuya aparición puede estar asociada a fenómenos de retracción, cargas excesivas, acciones sísmicas, procesos de corrosión del acero de refuerzo o deterioro por agentes ambientales. La detección temprana de estas discontinuidades permite planificar intervenciones oportunas, optimizar los costos de mantenimiento y prolongar la vida útil de las estructuras [[1](#referencias)].

Tradicionalmente, la identificación de fisuras se realiza mediante inspecciones visuales efectuadas por especialistas. Aunque este procedimiento continúa siendo ampliamente utilizado, presenta limitaciones debido a que depende de la experiencia del inspector, requiere una considerable inversión de tiempo y puede verse afectado por la subjetividad inherente al proceso de observación. En respuesta a estas limitaciones, los avances en inteligencia artificial y visión por computadora han impulsado el desarrollo de métodos automatizados capaces de analizar imágenes digitales e identificar patrones asociados al deterioro estructural, incrementando la rapidez y objetividad de las inspecciones [[2](#referencias)].

Dentro de las técnicas de aprendizaje profundo, las Redes Neuronales Convolucionales (CNN) han demostrado un desempeño sobresaliente en tareas de clasificación de imágenes gracias a su capacidad para aprender automáticamente características relevantes. En este trabajo se desarrolla un modelo utilizando el conjunto de datos **SDNET2018**, **TensorFlow/Keras** y una **CNN** para la clasificación binaria de imágenes con y sin fisuras, evaluando su desempeño mediante *Accuracy*, *Precision*, *Recall*, *F1-Score* y *AUC* [[3](#referencias)–[6](#referencias)].

Adicionalmente, se implementa un procedimiento heurístico basado en procesamiento digital de imágenes para estimar el espesor de las fisuras detectadas. Finalmente, se busca demostrar la viabilidad del empleo de herramientas de inteligencia artificial como apoyo a las inspecciones estructurales, contribuyendo al desarrollo de metodologías más objetivas, rápidas y reproducibles para la evaluación del estado de estructuras de concreto.

---

## II. METODOLOGÍA

La metodología desarrollada comprende una secuencia de etapas orientadas al desarrollo de un sistema automatizado para la detección de fisuras en concreto mediante Redes Neuronales Convolucionales (CNN) utilizando el conjunto de datos **SDNET2018** obtenidos de la Utah State University.

### A. Selección del conjunto de datos
Se utilizó el dataset **SDNET2018**, conformado por aproximadamente 56,000 imágenes de muros, pavimentos y losas de puente clasificadas en imágenes con fisura y sin fisura.

### B. Preprocesamiento
Se verificó la integridad de las imágenes (eliminación de archivos corruptos), se normalizó el tamaño a $256 \times 256$ píxeles y el espacio de color a RGB, generándose un dataset limpio para el entrenamiento.

### C. División del conjunto de datos
Se realizó una partición estratificada distribuida en:
* **70%** para Entrenamiento (*Train*)
* **15%** para Validación (*Validation*)
* **15%** para Prueba (*Test*)

### D. Arquitectura CNN
La red implementada incorpora cuatro bloques convolucionales con *Batch Normalization*, *MaxPooling*, *Global Average Pooling*, *Dropout* y una capa de salida con activación *Sigmoid* para clasificación binaria.

### E. Entrenamiento
Se empleó **TensorFlow/Keras** con el optimizador **Adam**, tamaño de lote (*batch size*) de **32**, aumentación de datos (*Data Augmentation*), `class_weight`, `EarlyStopping`, `ModelCheckpoint` y `ReduceLROnPlateau`.

### F. Estimación del espesor
Las imágenes clasificadas como fisuradas fueron procesadas mediante escala de grises, CLAHE, Black-Hat, umbralización de Otsu, operaciones morfológicas, esqueletización y transformada de distancia para estimar el espesor en píxeles.

---

## III. RESULTADOS Y DISCUSIÓN

A continuación se resumen las métricas de rendimiento obtenidas por el modelo en el conjunto de prueba:

<div align="center">

**TABLA I**  
*Métricas de Evaluación del Modelo CNN en el Conjunto de Prueba*

| Métrica | Valor Obtenido | Estado / Meta |
| :--- | :---: | :---: |
| **Accuracy** | **0.93** | Satisfactorio |
| **Precision** | **0.91** | Elevada Precisión |
| **Recall** | **0.88** | Alta Detección |
| **F1-Score** | **0.89** | Balance Óptimo |
| **AUC** | **0.98** | Excelente Separabilidad |

</div>

<br>

### Evolución de Métricas durante el Entrenamiento

<div align="center">
  <img src="RESULTADOS_TAREA3/historial_auc.png" alt="Historial AUC" width="45%"/>
  <img src="RESULTADOS_TAREA3/historial_recall.png" alt="Historial Recall" width="45%"/>
  <p><i>Fig. 1. Curvas de evolución de la métrica AUC (izquierda) y Recall (derecha) en los conjuntos de entrenamiento y validación.</i></p>
</div>

---

## IV. CONCLUSIONES

El modelo convolucional propuesto demostró una alta efectividad en la detección automática de fisuras sobre superficies de concreto. La integración de técnicas de procesamiento digital de imágenes permitió estimar el grosor de las discontinuidades detectadas, proporcionando un marco integral para la evaluación no destructiva y automatizada de infraestructuras civiles.

---

## REFERENCIAS

<a id="referencias"></a>

1. D. Watt, *Building Pathology: Principles and Practice*, 2nd ed. Blackwell Publishing, 2007.
2. R. C. Gonzalez y R. E. Woods, *Digital Image Processing*, 4th ed. Pearson, 2018.
3. Y. LeCun, Y. Bengio, y G. Hinton, "Deep learning," *Nature*, vol. 521, no. 7553, pp. 436–444, 2015.
4. I. Goodfellow, Y. Bengio, y A. Courville, *Deep Learning*. MIT Press, 2016.
5. S. Dorafshan, R. J. Thomas, y M. Maguire, "SDNET2018: An annotated image dataset for non-contact concrete crack detection using deep convolutional neural networks," *Data in Brief*, vol. 21, pp. 1664–1668, 2018.
6. M. Abadi *et al.*, "TensorFlow: Large-scale machine learning on heterogeneous systems," 2016. [En línea]. Disponible: https://www.tensorflow.org/
