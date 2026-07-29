\documentclass[journal, twoside]{IEEEtran}

% Paquetes requeridos
\usepackage[utf8]{inputenc}
\usepackage[spanish, es-tabla]{babel}
\usepackage{cite}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{textcomp}
\usepackage{xcolor}
\usepackage{booktabs}

\begin{document}

% Título del Artículo
\title{Detección de Fisuras en Concreto mediante Redes Neuronales Convolucionales (CNN) y Estimación de Espesor}

% Autores e Integrantes
\author{
    \IEEEauthorblockN{Nombres y Apellidos del Integrante 1, 
                      Nombres y Apellidos del Integrante 2, 
                      Nombres y Apellidos del Integrante 3} \\
    \IEEEauthorblockA{\textit{Escuela Profesional de Ingeniería Civil / Sistemas} \\
    \textit{Universidad Nacional de Santa}\\
    Nuevo Chimbote, Perú \\
    correo1@estudiante.edu.pe, correo2@estudiante.edu.pe, correo3@estudiante.edu.pe}
}

\maketitle

\begin{abstract}
La evaluación del estado de las estructuras de concreto es clave para garantizar su seguridad y durabilidad. La presencia de fisuras puede indicar fallas severas provocadas por retracción, cargas excesivas, sismos o corrosión. En este trabajo se implementa un modelo de aprendizaje profundo basado en Redes Neuronales Convolucionales (CNN) utilizando el conjunto de datos SDNET2018 para clasificar automáticamente imágenes con y sin fisuras. Adicionalmente, se desarrolla un algoritmo de procesamiento digital de imágenes para la estimación del espesor de las fisuras detectadas. El modelo propuesto alcanzó un Accuracy del 93\% y un AUC de 0.98, demostrando su viabilidad como herramienta objetiva para la inspección de infraestructuras de concreto.
\end{abstract}

\begin{IEEEkeywords}
Concreto armado, Detección de fisuras, Redes Neuronales Convolucionales (CNN), Procesamiento Digital de Imágenes, SDNET2018.
\end{IEEEkeywords}

\section{Introducción}
\IEEEPARstart{L}{a} evaluación del estado de las estructuras de concreto constituye una actividad fundamental para garantizar la seguridad, durabilidad y funcionalidad de las edificaciones e infraestructuras civiles. Entre las patologías más frecuentes se encuentran las fisuras, cuya aparición puede estar asociada a fenómenos de retracción, cargas excesivas, acciones sísmicas, procesos de corrosión del acero de refuerzo o deterioro por agentes ambientales. La detección temprana de estas discontinuidades permite planificar intervenciones oportunas, optimizar los costos de mantenimiento y prolongar la vida útil de las estructuras \cite{watt2007}.

Tradicionalmente, la identificación de fisuras se realiza mediante inspecciones visuales efectuadas por especialistas. Aunque este procedimiento continúa siendo ampliamente utilizado, presenta limitaciones debido a que depende de la experiencia del inspector, requiere una considerable inversión de tiempo y puede verse afectado por la subjetividad inherente al proceso de observación. En respuesta a estas limitaciones, los avances en inteligencia artificial y visión por computadora han impulsado el desarrollo de métodos automatizados capaces de analizar imágenes digitales e identificar patrones asociados al deterioro estructural, incrementando la rapidez y objetividad de las inspecciones \cite{gonzalez2018}.

Dentro de las técnicas de aprendizaje profundo, las Redes Neuronales Convolucionales (CNN) han demostrado un desempeño sobresaliente en tareas de clasificación de imágenes gracias a su capacidad para aprender automáticamente características relevantes. En este trabajo se desarrolla un modelo utilizando el conjunto de datos \textbf{SDNET2018}, \textbf{TensorFlow/Keras} y una \textbf{CNN} para la clasificación binaria de imágenes con y sin fisuras, evaluando su desempeño mediante \textit{Accuracy}, \textit{Precision}, \textit{Recall}, \textit{F1-Score} y \textit{AUC} \cite{lecun2015, goodfellow2016, dorafshan2018, abadi2016}.

Adicionalmente, se implementa un procedimiento heurístico basado en procesamiento digital de imágenes para estimar el espesor de las fisuras detectadas. Finalmente, se busca demostrar la viabilidad del empleo de herramientas de inteligencia artificial como apoyo a las inspecciones estructurales, contribuyendo al desarrollo de metodologías más objetivas, rápidas y reproducibles para la evaluación del estado de estructuras de concreto.

\section{Metodología}
La metodología desarrollada comprende una secuencia de etapas orientadas al desarrollo de un sistema automatizado para la detección de fisuras en concreto mediante Redes Neuronales Convolucionales (CNN) utilizando el conjunto de datos \textbf{SDNET2018} obtenidos de la Utah State University.

\subsection{Selección del conjunto de datos}
Se utilizó el dataset SDNET2018, conformado por aproximadamente 56,000 imágenes de muros, pavimentos y losas de puente clasificadas en imágenes con fisura y sin fisura.

\subsection{Preprocesamiento}
Se verificó la integridad de las imágenes (eliminación de archivos corruptos), se normalizó el tamaño a $256 \times 256$ píxeles y el espacio de color a RGB, generándose un dataset limpio para el entrenamiento.

\subsection{División del conjunto de datos}
Se realizó una partición estratificada distribuida en:
\begin{itemize}
    \item \textbf{70\%} para Entrenamiento (\textit{Train})
    \item \textbf{15\%} para Validación (\textit{Validation})
    \item \textbf{15\%} para Prueba (\textit{Test})
\end{itemize}

\subsection{Arquitectura CNN}
La red implementada incorpora cuatro bloques convolucionales con \textit{Batch Normalization}, \textit{MaxPooling}, \textit{Global Average Pooling}, \textit{Dropout} y una capa de salida con activación \textit{Sigmoid} para clasificación binaria.

\subsection{Entrenamiento}
Se empleó TensorFlow/Keras con el optimizador Adam, tamaño de lote (\textit{batch size}) de 32, aumentación de datos (\textit{Data Augmentation}), \texttt{class\_weight}, \texttt{EarlyStopping}, \texttt{ModelCheckpoint} y \texttt{ReduceLROnPlateau}.

\subsection{Evaluación}
Las métricas utilizadas fueron \textit{Accuracy}, \textit{Precision}, \textit{Recall}, \textit{F1-Score}, \textit{AUC} y la matriz de confusión.

\subsection{Estimación del espesor}
Las imágenes clasificadas como fisuradas fueron procesadas mediante escala de grises, CLAHE, Black-Hat, umbralización de Otsu, operaciones morfológicas, esqueletización y transformada de distancia para estimar el espesor en píxeles.

\section{Resultados y Métricas de Evaluación}
A continuación se resumen las métricas de rendimiento obtenidas por el modelo en el conjunto de prueba (ver Tabla I).

\begin{table}[htbp]
\caption{Métricas de Evaluación del Modelo CNN en el Conjunto de Prueba}
\begin{center}
\begin{tabular}{lc}
\toprule
\textbf{Métrica} & \textbf{Valor} \\
\midrule
Accuracy  & \textbf{0.93} \\
Precision & \textbf{0.91} \\
Recall    & \textbf{0.88} \\
F1-Score  & \textbf{0.89} \\
AUC       & \textbf{0.98} \\
\bottomrule
\end{tabular}
\label{tab:metricas}
\end{center}
\end{table}

\subsection{Historial de Evolución de Métricas}
Las gráficas del historial de entrenamiento y validación para las métricas AUC y Recall muestran la estabilidad y la capacidad de generalización de la red convolucional a lo largo de las épocas de entrenamiento.

\begin{figure}[htbp]
\centering
\includegraphics[width=0.48\linewidth]{RESULTADOS_TAREA3/historial_auc.png}
\hfill
\includegraphics[width=0.48\linewidth]{RESULTADOS_TAREA3/historial_recall.png}
\caption{Evolución del AUC (izquierda) y Recall (derecha) durante el entrenamiento.}
\label{fig:curvas}
\end{figure}

\section{Conclusiones}
El modelo convolucional propuesto demostró una alta efectividad en la detección automática de fisuras sobre superficies de concreto. La integración de técnicas de procesamiento digital de imágenes permitió estimar el grosor de las discontinuidades detectadas, proporcionando un marco integral para la evaluación no destructiva y automatizada de infraestructuras civiles.

\begin{thebibliography}{00}
\bibitem{watt2007} D. Watt, \textit{Building Pathology: Principles and Practice}, 2nd ed. Blackwell Publishing, 2007.
\bibitem{gonzalez2018} R. C. Gonzalez y R. E. Woods, \textit{Digital Image Processing}, 4th ed. Pearson, 2018.
\bibitem{lecun2015} Y. LeCun, Y. Bengio, y G. Hinton, ``Deep learning,'' \textit{Nature}, vol. 521, no. 7553, pp. 436--444, 2015.
\bibitem{goodfellow2016} I. Goodfellow, Y. Bengio, y A. Courville, \textit{Deep Learning}. MIT Press, 2016.
\bibitem{dorafshan2018} S. Dorafshan, R. J. Thomas, y M. Maguire, ``SDNET2018: An annotated image dataset for non-contact concrete crack detection using deep convolutional neural networks,'' \textit{Data in Brief}, vol. 21, pp. 1664--1668, 2018.
\bibitem{abadi2016} M. Abadi \textit{et al.}, ``TensorFlow: Large-scale machine learning on heterogeneous systems,'' 2016. [En línea]. Disponible: https://www.tensorflow.org/
\end{thebibliography}

\end{document}
