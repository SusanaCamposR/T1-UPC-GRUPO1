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
  <small><code>E202524364@upc.edu.pe</code> &nbsp;|&nbsp; <code>E202524396@upc.edu.pe</code></small>
</p>

<p align="center" style="margin-top: 10px;">&amp;</p>

<p align="center">
  <strong>Jaime Jesus Ramírez Elera</strong> &nbsp;|&nbsp; <strong>Renzo Salleres Untiveros</strong><br />
  <em>Universidad Peruana de Ciencias Aplicadas (UPC)</em><br />
  <small><code>E202526653@upc.edu.pe</code> &nbsp;|&nbsp; <code>E202523955@upc.edu.pe</code></small>
</p>
</div>
<hr />

---
> ### **Resumen (Abstract)**
> <p align="justify">
> La evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, la durabilidad y la funcionalidad de las edificaciones e infraestructuras civiles. Entre las patologías más frecuentes se encuentran las fisuras, las cuales pueden originarse por fenómenos de retracción, sobrecargas, acciones sísmicas, corrosión del acero de refuerzo o deterioro por agentes ambientales. La detección temprana de estas discontinuidades permite planificar intervenciones oportunas, optimizar los costos de mantenimiento y prolongar la vida útil de las estructuras. En este trabajo se desarrolla un modelo utilizando el conjunto de datos <strong>SDNET2018</strong>, <strong>TensorFlow/Keras</strong> y una <strong>CNN</strong> para la clasificación binaria de imágenes con y sin fisuras, evaluando su desempeño mediante <em>Accuracy</em>, <em>Precision</em>, <em>Recall</em>, <em>F1-Score</em> y <em>AUC</em>. Adicionalmente, se implementa un procedimiento heurístico basado en procesamiento digital de imágenes para estimar el espesor de las fisuras detectadas.
> </p>
> 
> **Palabras Clave (Keywords)** — *Concreto armado, Detección de fisuras, Redes Neuronales Convolucionales (CNN), Procesamiento Digital de Imágenes, SDNET2018.*

---
<h2 align="left">I. INTRODUCCIÓN</h2>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #e1e4e8;">
  <tr>
    <td width="50%" valign="top" style="border: 1px solid #e1e4e8; padding: 12px 16px;">
      <p align="justify" style="text-align: justify; margin-top: 0;">
        La evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, la durabilidad y la funcionalidad de las edificaciones e infraestructuras civiles. Entre las patologías más frecuentes se encuentran las fisuras, las cuales pueden originarse por fenómenos de retracción, sobrecargas, acciones sísmicas, corrosión del acero de refuerzo o deterioro ocasionado por agentes ambientales. La detección temprana de estas discontinuidades permite planificar intervenciones oportunas, optimizar los costos de mantenimiento y prolongar la vida útil de las estructuras (Watt, 2007).
      </p>
      <p align="justify" style="text-align: justify; margin-bottom: 0;">
        Tradicionalmente, la identificación de fisuras se realiza mediante inspecciones visuales efectuadas por especialistas. Aunque este procedimiento continúa siendo ampliamente utilizado, presenta limitaciones debido a que depende de la experiencia del inspector, requiere una considerable inversión de tiempo y puede verse afectado por la subjetividad inherente al proceso de observación. En respuesta a estas limitaciones, los avances en inteligencia artificial y visión por computadora han impulsado el desarrollo de métodos automatizados capaces de analizar imágenes digitales e identificar patrones asociados al deterioro estructural, incrementando la rapidez y objetividad de las inspecciones (Gonzalez & Woods, 2018).
      </p>
    </td>
    <td width="50%" valign="top" style="border: 1px solid #e1e4e8; padding: 12px 16px;">
      <p align="justify" style="text-align: justify; margin-top: 0;">
        Dentro de las técnicas de aprendizaje profundo, las Redes Neuronales Convolucionales (CNN) han demostrado un desempeño sobresaliente en tareas de clasificación de imágenes gracias a su capacidad para aprender automáticamente características relevantes. En este trabajo se desarrolla un modelo utilizando el conjunto de datos SDNET2018, TensorFlow/Keras y una CNN para la clasificación binaria de imágenes con y sin fisuras, evaluando su desempeño mediante <em>Accuracy</em>, <em>Precision</em>, <em>Recall</em>, <em>F1-Score</em> y <em>AUC</em> (LeCun et al., 2015; Goodfellow et al., 2016; Dorafshan et al., 2018; Abadi et al., 2016).
      </p>
      <p align="justify" style="text-align: justify; margin-bottom: 0;">
        Adicionalmente, se implementa un procedimiento heurístico basado en procesamiento digital de imágenes para estimar el espesor de las fisuras detectadas. Finalmente, se busca demostrar la viabilidad del empleo de herramientas de inteligencia artificial como apoyo a las inspecciones estructurales, contribuyendo al desarrollo de metodologías más objetivas, rápidas y reproducibles para la evaluación del estado de estructuras de concreto.
      </p>
    </td>
  </tr>
</table>

<br />

<h3 align="left">REFERENCIAS</h3>

<div style="font-size: 0.95em; line-height: 1.5;">
  <p align="justify" style="text-align: justify; padding-left: 2em; text-indent: -2em; margin-bottom: 12px;">
    Abadi, M., et al. (2016). <em>TensorFlow: Large-Scale Machine Learning on Heterogeneous Systems</em>. <a href="https://www.tensorflow.org/">https://www.tensorflow.org/</a>
  </p>
  <p align="justify" style="text-align: justify; padding-left: 2em; text-indent: -2em; margin-bottom: 12px;">
    Dorafshan, S., Thomas, R. J., & Maguire, M. (2018). SDNET2018: An annotated image dataset for non-contact concrete crack detection using deep convolutional neural networks. <em>Data in Brief</em>, 21, 1664–1668.
  </p>
  <p align="justify" style="text-align: justify; padding-left: 2em; text-indent: -2em; margin-bottom: 12px;">
    Gonzalez, R. C., & Woods, R. E. (2018). <em>Digital Image Processing</em> (4th ed.). Pearson.
  </p>
  <p align="justify" style="text-align: justify; padding-left: 2em; text-indent: -2em; margin-bottom: 12px;">
    Goodfellow, I., Bengio, Y., & Courville, A. (2016). <em>Deep Learning</em>. MIT Press.
  </p>
  <p align="justify" style="text-align: justify; padding-left: 2em; text-indent: -2em; margin-bottom: 12px;">
    LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep learning. <em>Nature</em>, 521(7553), 436–444.
  </p>
  <p align="justify" style="text-align: justify; padding-left: 2em; text-indent: -2em; margin-bottom: 12px;">
    Watt, D. (2007). <em>Building Pathology: Principles and Practice</em> (2nd ed.). Blackwell Publishing.
  </p>
</div>
---

<h2 align="left">II. METODOLOGÍA</h2>

<p align="justify" style="text-align: justify;">
  La metodología desarrollada comprende una secuencia de etapas orientadas al desarrollo de un sistema automatizado para la detección de fisuras en concreto mediante Redes Neuronales Convolucionales (CNN) utilizando el conjunto de datos SDNET2018 obtenido de la Utah State University[cite: 2]. El procedimiento incluye la preparación del conjunto de datos, el preprocesamiento de imágenes, el entrenamiento del modelo, la evaluación mediante métricas de clasificación y la estimación del espesor de fisuras mediante procesamiento digital de imágenes[cite: 2].
</p>

<table style="width: 100%; border-collapse: collapse; border: 1px solid #e1e4e8;">
  <tr>
    <td width="50%" valign="top" style="border: 1px solid #e1e4e8; padding: 14px 16px;">
      
      <h3 align="left" style="margin-top: 0;">1. Selección del Conjunto de Datos</h3>
      <p align="justify" style="text-align: justify;">
        Se utilizó el dataset público SDNET2018, conformado por aproximadamente 56 000 imágenes de muros, pavimentos y losas de puente clasificadas en imágenes con fisura y sin fisura[cite: 2]. Este repositorio destaca por su alta variabilidad en condiciones de iluminación, textura superficial y presencia de ruido en condiciones reales de obra[cite: 2].
      </p>

      <p align="center" style="text-align: center; margin: 15px 0;">
        <img src="Figura_1_Flujo_General.png" alt="Figura 1. Selección del conjunto de datos" width="100%" />
        <br />
        <small><strong>Figura 1.</strong> Selección y características del conjunto de datos SDNET2018[cite: 2].</small>
      </p>

      <h3 align="left">2. Preprocesamiento de Imágenes</h3>
      <p align="justify" style="text-align: justify;">
        Se verificó la integridad de las imágenes eliminando archivos corruptos o defectuosos[cite: 2]. Se normalizó la resolución espacial a 256×256 píxeles y se estandarizó el espacio de color en formato RGB, garantizando un dataset limpio y homogéneo para la fase de entrenamiento[cite: 2].
      </p>

      <h3 align="left">3. División del Conjunto de Datos</h3>
      <p align="justify" style="text-align: justify;">
        Se realizó una partición estratificada conservando la distribución original de clases en tres subconjuntos[cite: 2]: 70 % para entrenamiento (39 200 imágenes), 15 % para validación (8 400 imágenes) y 15 % para prueba (8 400 imágenes)[cite: 2].
      </p>

      <p align="center" style="text-align: center; margin: 15px 0;">
        <img src="Figura_2_Division.png" alt="Figura 2. División del conjunto de datos" width="100%" />
        <br />
        <small><strong>Figura 2.</strong> Proporciones de división del conjunto de datos[cite: 2].</small>
      </p>

      <p align="center" style="text-align: center; margin: 15px 0;">
        <img src="Figura 3_Figura_3_CNN.png" alt="Figura 3. Flujo de partición" width="100%" />
        <br />
        <small><strong>Figura 3.</strong> Flujo detallado de la partición estratificada[cite: 2].</small>
      </p>

    </td>
    <td width="50%" valign="top" style="border: 1px solid #e1e4e8; padding: 14px 16px;">

      <h3 align="left" style="margin-top: 0;">4. Arquitectura de la Red Neuronal (CNN)</h3>
      <p align="justify" style="text-align: justify;">
        La red propuesta incorpora cuatro bloques convolucionales secuenciales equipados con Batch Normalization, funciones de activación ReLU y submuestreo MaxPooling2D[cite: 2]. Posteriormente, se integra una capa de agregación Global Average Pooling, regularización mediante Dropout (0.5) y una capa densa final con activación Sigmoide para la clasificación binaria ($0 \le p \le 1$)[cite: 2].
      </p>

      <p align="center" style="text-align: center; margin: 15px 0;">
        <img src="Figura_4_Espesor.png" alt="Figura 4. Arquitectura CNN" width="100%" />
        <br />
        <small><strong>Figura 4.</strong> Arquitectura de la Red Neuronal Convolucional (CNN)[cite: 2].</small>
      </p>

      <h3 align="left">5. Entrenamiento del Modelo</h3>
      <p align="justify" style="text-align: justify;">
        El entrenamiento se ejecutó sobre la plataforma TensorFlow/Keras haciendo uso del optimizador Adam y un tamaño de lote (<em>batch size</em>) de 32 imágenes[cite: 2]. Se aplicaron técnicas de aumento de datos (<em>data augmentation</em>), ponderación de clases (<code>class_weight</code>) para mitigar el desbalance, así como las retrollamadas <code>EarlyStopping</code>, <code>ModelCheckpoint</code> y <code>ReduceLROnPlateau</code> para optimizar la convergencia[cite: 2].
      </p>

      <h3 align="left">6. Evaluación del Desempeño</h3>
      <p align="justify" style="text-align: justify;">
        La capacidad predictiva del modelo fue evaluada en el conjunto de prueba independiente mediante la matriz de confusión y métricas estándar de clasificación: <em>Accuracy</em>, <em>Precision</em>, <em>Recall</em>, <em>F1-Score</em> y área bajo la curva (<em>AUC</em>)[cite: 2].
      </p>

      <h3 align="left">7. Estimación del Espesor de Fisuras</h3>
      <p align="justify" style="text-align: justify;">
        Las imágenes clasificadas como "con fisura" son sometidas a un pipeline de procesamiento digital de imágenes[cite: 2]: conversión a escala de grises, ecualización adaptativa de histograma (CLAHE), filtro Top-Hat/Black-Hat, umbralización de Otsu, operaciones morfológicas, esqueletización y transformada de distancia[cite: 2].
      </p>
      <p align="justify" style="text-align: justify; margin-bottom: 0;">
        El sistema genera un archivo final que reporta el espesor de las fisuras en píxeles[cite: 2]. Se destaca que la salida se presenta en píxeles debido a la ausencia de un patrón físico de escala dentro de las tomas[cite: 2]. Aunque estudios similares sobre este dataset estiman una distancia de captura aproximada de 60 cm, la conversión a dimensiones métricas exactas requeriría una confirmación formal de los parámetros ópticos de adquisición[cite: 2].
      </p>

    </td>
  </tr>
</table>

<br />














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
