# Aplicaciones de IA en Estructuras
## Trabajo N.° 1 - Definición del Problema, Datos y Repositorio

### Universidad Peruana de Ciencias Aplicadas (UPC)

**Curso:** Aplicaciones de IA en Estructuras

### Integrantes

- Susana Abigail Campos Rodríguez
- Carlos Teodoro Barreda Guzmán
- Jaime Jesús Ramírez Elera
- Renzo Salleres Untiveros

---

# Descripción del Proyecto

La infraestructura de concreto, presente en puentes, pavimentos, muros y edificaciones, está expuesta continuamente a cargas mecánicas, variaciones climáticas y procesos naturales de deterioro. Estas condiciones pueden originar fisuras superficiales que, de no detectarse oportunamente, evolucionan hasta comprometer la seguridad y el desempeño estructural.

Actualmente, la inspección de estas fisuras depende principalmente de evaluaciones visuales realizadas por especialistas, lo que implica elevados costos, mayor tiempo de inspección y una importante dependencia del criterio humano.

Como alternativa, este proyecto propone el uso de técnicas de Inteligencia Artificial, Visión Artificial y Machine Learning Supervisado para automatizar la detección de fisuras en superficies de concreto mediante el análisis de imágenes pertenecientes al dataset SDNET2018.

El objetivo es desarrollar una herramienta de apoyo para la preinspección estructural, permitiendo optimizar los procesos de mantenimiento preventivo y mejorar la toma de decisiones durante las inspecciones.

---

# Objetivo General

Desarrollar un modelo basado en Visión Artificial capaz de detectar automáticamente fisuras visibles en superficies de concreto utilizando el dataset SDNET2018.

Adicionalmente, se propone clasificar las imágenes según el espesor estimado de la fisura y generar un Índice de Prioridad de Inspección Visual (IPIV) que facilite la programación de inspecciones técnicas.

---

# Dataset

Se utilizará el dataset **SDNET2018 (Concrete Crack Image Dataset)**.

Características principales:

- Más de 56 000 imágenes.
- Imágenes con y sin fisuras.
- Formato JPEG.
- Resolución de 256 × 256 píxeles.
- Incluye imágenes de:
  - Puentes
  - Muros
  - Pavimentos

El conjunto de datos contiene diferentes condiciones reales como:

- Sombras
- Cambios de iluminación
- Rugosidad superficial
- Bordes
- Agujeros
- Residuos

Estas características permiten entrenar modelos más robustos para escenarios reales de inspección.

---

# Variables del Proyecto

## Variable dependiente

- Presencia de fisura
    - Con fisura (1)
    - Sin fisura (0)

## Variables independientes

- Intensidad RGB
- Textura superficial
- Bordes y contornos
- Forma de la fisura
- Orientación
- Contraste
- Iluminación
- Ruido visual

---

# Aporte del Proyecto

A diferencia de otros modelos que únicamente clasifican imágenes como "Fisura" o "No Fisura", esta propuesta incorpora un **Índice de Prioridad de Inspección Visual (IPIV)**.

Este índice permitirá ordenar automáticamente las zonas inspeccionadas según el nivel de riesgo asociado a la fisura detectada, facilitando la planificación del mantenimiento estructural.

### Clasificación propuesta

| Espesor | Nivel |
|----------|--------|
| 0.06 – 1 mm | Baja |
| >1 – 5 mm | Media |
| >5 – 15 mm | Alta |
| >15 – 25 mm | Muy Alta |

---

# Marco Metodológico

El desarrollo seguirá el marco **PCS (Predictability, Computability & Stability)** propuesto por Bin Yu y Rebecca Barter.

## Predictability

Evaluar la capacidad del modelo para detectar correctamente la presencia de fisuras.

## Computability

Garantizar que el modelo pueda entrenarse utilizando recursos computacionales moderados.

## Stability

Verificar que el modelo mantenga resultados consistentes sobre diferentes tipos de superficies y distintas particiones del conjunto de datos.

---

# Tecnologías a utilizar

- Python
- OpenCV
- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-Learn

---

# Estado del Proyecto

🟡 Planeamiento

- [x] Definición del problema
- [x] Selección del dataset
- [ ] Preprocesamiento
- [ ] Entrenamiento
- [ ] Evaluación
- [ ] Implementación del IPIV
- [ ] Resultados finales

---

# Repositorio

Este repositorio documenta el desarrollo completo del proyecto correspondiente al curso **Aplicaciones de IA en Estructuras**, desde la definición del problema hasta la implementación y evaluación del modelo de Inteligencia Artificial.
