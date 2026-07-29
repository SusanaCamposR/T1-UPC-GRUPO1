<div align="center">

<!-- Encabezado Estilo Revista / Journal -->
<p align="left" style="font-family: sans-serif; font-size: 14px; margin-bottom: 5px;">
  <strong>APLICACIONES DE IA EN ESTRUCTURAS</strong> &nbsp;|&nbsp; <em>UPC - TAREA 3</em>
</p>
<hr size="2" color="#000000" style="margin-top: 0; margin-bottom: 25px;" />

<!-- Título Principal (Grande y Centrado) -->
<h1 align="center" style="border: none; font-size: 28px; font-weight: normal; margin-bottom: 20px;">
  Detección de Fisuras en Concreto mediante Redes Neuronales Convolucionales (CNN) y Estimación de Espesor
</h1>

<br />

<!-- Integrantes y Afiliación -->
<p align="center">
  <strong>Susana Abigail Campos Rodríguez</strong> &nbsp;|&nbsp; <strong>Carlos Teodoro Barreda Guzmán</strong><br />
  <em>Universidad Peruana de Ciencias Aplicadas (UPC)</em><br />
  <small><code>u202510001@upc.edu.pe</code> &nbsp;|&nbsp; <code>u202510002@upc.edu.pe</code></small>
</p>

<p align="center" style="margin-top: 10px;">&amp;</p>

<p align="center">
  <strong>Jaime Jesus Ramírez Elera</strong> &nbsp;|&nbsp; <strong>Renzo Salleres Untiveros</strong><br />
  <em>Universidad Peruana de Ciencias Aplicadas (UPC)</em><br />
  <small><code>u202510003@upc.edu.pe</code> &nbsp;|&nbsp; <code>u202510004@upc.edu.pe</code></small>
</p>

</div>

<br />
<hr />
<br />






















<div align="center">

<!-- Encabezado Estilo Revista / Journal -->
<p align="left" style="font-family: sans-serif; font-size: 14px; margin-bottom: 5px;">
  <strong>APLICACIONES DE IA EN ESTRUCTURAS</strong> &nbsp;|&nbsp; <em>UPC - TAREA 3</em>
</p>
<hr size="2" color="#000000" style="margin-top: 0; margin-bottom: 25px;" />

<!-- Título Principal (Grande y Centrado) -->
<h1 align="center" style="border: none; font-size: 28px; font-weight: normal; margin-bottom: 20px;">
  Detección de Fisuras en Concreto mediante Redes Neuronales Convolucionales (CNN) y Estimación de Espesor
</h1>

<br />

<!-- Integrantes y Afiliación -->
<p align="center">
  <strong>Susana Abigail Campos Rodríguez &nbsp;|&nbsp; Carlos Teodoro Barreda Guzmán</strong><br />
  <em>Universidad Peruana de Ciencias Aplicadas (UPC)</em><br />
  <small><code>e202524364@upc.edu.pe</code></small>
</p>

<p align="center" style="margin-top: 10px;">&amp;</p>

<p align="center">
  <strong>Jaime Jesus Ramírez Elera &nbsp;|&nbsp; Renzo Salleres Untiveros</strong><br />
  <em>Universidad Peruana de Ciencias Aplicadas (UPC)</em><br />
  <small><code>e202524364@upc.edu.pe</code></small>
</p>

</div>

<br />
<hr />
<br />














<div align="center">

# Detección de Fisuras en Concreto mediante Redes Neuronales Convolucionales (CNN) y Estimación de Espesor

**APLICACIONES DE IA EN ESTRUCTURAS**

<br>

| **Integrantes del Grupo** | **Afiliación y Contacto** |
| :--- | :--- |
| **Susana Abigail Campos Rodríguez** | *e202524364@upc.edu.pe*|
| **Carlos Teodoro Barreda Guzmán** | *e202524364@upc.edu.pe* |
| **Jaime Jesus Ramírez Elera** | *E202526653@upc.edu.pe* |
| **Renzo Salleres Untiveros** | *e202524364@upc.edu.pe* |

</div>

---
> ### **Resumen (Abstract)**
> <p align="justify">
> La evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, la durabilidad y la funcionalidad de las edificaciones e infraestructuras civiles. Entre las patologías más frecuentes se encuentran las fisuras, las cuales pueden originarse por fenómenos de retracción, sobrecargas, acciones sísmicas, corrosión del acero de refuerzo o deterioro por agentes ambientales. La detección temprana de estas discontinuidades permite planificar intervenciones oportunas, optimizar los costos de mantenimiento y prolongar la vida útil de las estructuras. En este trabajo se desarrolla un modelo utilizando el conjunto de datos <strong>SDNET2018</strong>, <strong>TensorFlow/Keras</strong> y una <strong>CNN</strong> para la clasificación binaria de imágenes con y sin fisuras, evaluando su desempeño mediante <em>Accuracy</em>, <em>Precision</em>, <em>Recall</em>, <em>F1-Score</em> y <em>AUC</em>. Adicionalmente, se implementa un procedimiento heurístico basado en procesamiento digital de imágenes para estimar el espesor de las fisuras detectadas.
> </p>
> 
> **Palabras Clave (Keywords)** — *Concreto armado, Detección de fisuras, Redes Neuronales Convolucionales (CNN), Procesamiento Digital de Imágenes, SDNET2018.*

---

# Evaluación del Estado de Estructuras de Concreto Armado

## 1. Introducción

<div style="display: flex; gap: 40px;">
  <div style="flex: 1;">
    <h3>Importancia y Contexto General</h3>
    <p>La evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, durabilidad y funcionalidad de las edificaciones e infraestructuras civiles.</p>
    <p>Entre las patologías más frecuentes se encuentran las fisuras, cuya aparición puede estar asociada a fenómenos de retracción, cargas excesivas, acciones sísmicas, procesos de corrosión del acero de refuerzo o deterioro por agentes ambientales agresivos.</p>
  </div>
  <div style="flex: 1;">
    <h3>Objetivos y Alcance Diagnóstico</h3>
    <p>El propósito del diagnóstico estructural es identificar de manera precisa el origen y severidad de los daños presentes, evaluando la capacidad resistente remanente de los elementos de concreto reforzado.</p>
    <p>Una oportuna caracterización permite tomar decisiones informadas sobre las técnicas de reparación, rehabilitación o reforzamiento requeridas, previniendo fallas catastróficas y maximizando la vida útil de la edificación.</p>
  </div>
</div>

---

## 2. Metodología

A continuación se detalla el procedimiento técnico para la inspección y diagnóstico de la estructura:

### Fase 1: Recopilación de Información e Inspección Visual
Se realiza la revisión de planos *as-built*, memoria de cálculo y antecedentes de la obra, seguida de un levantamiento minucioso de daños visibles (fisuras, desprendimientos, eflorescencias y corrosión).

> **[Imagen 1: Diagrama de Flujo del Procedimiento Metodológico]**  
> 🔗 *[Haz clic aquí para subir o ver la Imagen 1 del archivo Word](URL_DE_TU_IMAGEN_1)*

---

### Fase 2: Ensayos No Destructivos y Destructivos
Ejecución de pruebas *in situ* para caracterizar la calidad del concreto y la disposición del acero de refuerzo:

* **Esclerometría (Índice de rebote):** Estimación de la uniformidad de la resistencia superficial del concreto.
* **Ultrasonido:** Medición de la velocidad de pulso ultrasónico para detectar oquedades y evaluar compacidad.
* **Pacometría (Scanner / Localizador de acero):** Localización del acero de refuerzo y medición del recubrimiento.
* **Extracción de Testigos Cilíndricos:** Ensayos de compresión en laboratorio para corroborar resistencia $f'_c$.

> **[Imagen 2: Esquema de Ensayos No Destructivos / Inspección de Campo]**  
> 🔗 *[Haz clic aquí para subir o ver la Imagen 2 del archivo Word](URL_DE_TU_IMAGEN_2)*

---

### Fase 3: Modelación y Evaluación de Resultados
Integración de las propiedades reales obtenidas en campo y laboratorio dentro del modelo analítico para determinar el nivel de seguridad estructural frente a la normativa vigente.
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
