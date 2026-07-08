**UNIVERSIDAD PERUANA DE CIENCIAS APLICADAS**

APLICACIONES DE IA EN ESTRUCTURAS ![Universidad Peruana de Ciencias Aplicadas - Wikipedia, la enciclopedia libre]

**INFORME DE TRABAJO N° 1**

Definición del Problema, Datos y Repositorio

Presentado por:

**Susana Abigail Campos Rodríguez**

**Carlos Teodoro Barreda Guzmán**

**Jaime Jesus Ramìrez Elera**

**Renzo Salleres Untiveros**

**TRABAJO N°1**

**DEFINICIÓN DEL PROBLEMA, DATOS Y REPOSITORIO**

- **Descripción del problema de ingeniería estructural a resolver.**

La infraestructura de concreto, presente en puentes, pavimentos, muros y edificaciones, está expuesta continuamente a cargas mecánicas, variaciones climáticas y procesos de deterioro que pueden generar fisuras superficiales. La identificación temprana de estas fisuras es fundamental para prevenir daños mayores y planificar intervenciones de mantenimiento oportunas. Sin embargo, las inspecciones tradicionales dependen de evaluaciones visuales realizadas por especialistas, lo que puede demandar una gran cantidad de tiempo, recursos y personal técnico, especialmente en infraestructuras de gran extensión. Frente a esta problemática, el presente proyecto propone el uso de técnicas de Machine Learning Supervisado y visión artificial para automatizar la detección de fisuras en superficies de concreto mediante el análisis de imágenes del dataset SDNET2018, contribuyendo a mejorar la eficiencia y objetividad de los procesos de inspección estructural

- **Objetivo:**

Desarrollar una propuesta de modelo supervisado de visión artificial para detectar fisuras visibles en concreto usando el dataset SDNET2018, con énfasis en su posible uso como herramienta de preinspección en mantenimiento estructural. Se propone clasificar las imágenes agrupándolas en función del espesor de la fisura encontrada, usando uno de los algoritmos enseñados en clases (K-means, DBScan, Kernel PCA). La asignación del tipo de fisura (leve, mediana o moderada) será en función del espesor de las mismas.

- **Datos:**

SDNET2018 es un conjunto de datos anotado para entrenamiento, validación y comparación de algoritmos de inteligencia artificial orientados a la detección de fisuras en concreto. Según la página oficial del dataset en DigitalCommons@USU, contiene más de 56,000 imágenes de superficies de concreto con y sin fisuras, incluyendo tableros de puentes, muros y pavimentos.

El dataset fue publicado por autores asociados a Utah State University y se presenta como un recurso para el desarrollo de algoritmos de detección de fisuras mediante redes neuronales convolucionales. La página del dataset indica que las imágenes incluyen obstáculos o condiciones visuales como sombras, rugosidad superficial, bordes, agujeros y residuos de fondo, lo cual permite entrenar modelos en un escenario menos idealizado.

| Elemento                  | Descripción                                                                                                                             |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Nombre                    | SDNET2018: Concrete Crack Image Dataset                                                                                                 |
| Fuente                    | DigitalCommons@USU: <https://digitalcommons.usu.edu/all_datasets/48/>                                                                   |
| Tipo de datos             | Imágenes JPEG clasificadas en presencia o ausencia de fisura.                                                                           |
| Escenarios                | Tableros de puente, muros y pavimentos de concreto.                                                                                     |
| Resolución de subimágenes | 256 x 256 píxeles, según la descripción del dataset.                                                                                    |
| Variable objetivo         | imagen con fisura o imagen sin fisura.                                                                                                  |
| Variables observables     | Patrones visuales de grietas, textura, sombras, bordes, rugosidad y fondo.                                                              |
| Uso en el proyecto        | Entrenamiento y evaluación de una CNN(Convolutional Neural Network o Red Neuronal Convolucional) para clasificación visual supervisada. |

**Enfoque original del grupo: índice de prioridad para inspección**

Para diferenciar esta propuesta de otros grupos que usen el mismo dataset, se propone no limitarse a entregar un clasificador "fisura/no fisura". El aporte particular será un Índice de Prioridad de Inspección Visual (IPIV) en base al espesor de la fisura, que ordene las imágenes según la probabilidad estimada de fisura. Este índice puede servir para decidir qué zonas revisará primero el equipo técnico.

**Clasificación propuesta según espesor de fisura**

| **Categoría**   | **Espesor estimado de fisura** | **Nivel de prioridad** |
| --------------- | ------------------------------ | ---------------------- |
| Fisura leve     | 0.06 mm - 1 mm                 | Baja                   |
| Fisura moderada | \>1 mm - 5 mm                  | Media                  |
| Fisura severa   | \>5 mm - 15 mm                 | Alta                   |
| Fisura crítica  | \>15 mm - 25 mm                | Muy alta               |

- **Marco VDS:**

El marco Veridical Data Science, propuesto por Bin Yu y Rebecca Barter, emplea los principios de Predictability, Computability y Stability para evaluar la confianza y relevancia de los resultados en ciencia de datos. En este proyecto se aplicará de la siguiente manera:

| Principio PCS  | Aplicación en este proyecto                                                                                            | Justificación                                                                                                  |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Predictability | Evaluar la capacidad del modelo para identificar correctamente imágenes con fisuras.                                   | En inspección estructural, un falso negativo puede retrasar la revisión de una zona dañada.                    |
| Computability  | Usar modelos entrenables en Python y ejecutables en Google Colab o equipos con recursos moderados.                     | El modelo debe ser viable para estudiantes o instituciones sin infraestructura computacional avanzada.         |
| Stability      | Comparar resultados por tipo de superficie: puente, muro y pavimento; además, probar semillas y particiones distintas. | Un modelo confiable no debe funcionar solo en un subconjunto fácil ni depender de una única división de datos. |
