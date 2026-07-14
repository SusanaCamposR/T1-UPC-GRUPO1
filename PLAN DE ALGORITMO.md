# ==============================================================
# PROYECTO: DETECCIÓN DE FISURAS EN SUPERFICIES DE CONCRETO
# PLAN DE ALGORITMOS: CNN + K-MEANS
# DATASET: SDNET2018
# ==============================================================

# Códigos ANSI para dar formato y color al texto en la terminal
AZUL = "\033[94m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
CIAN = "\033[96m"
BLANCO = "\033[97m"
NEGRITA = "\033[1m"
RESET = "\033[0m"


# ==============================================================
# FUNCIONES DE PRESENTACIÓN
# ==============================================================

def mostrar_titulo(titulo):
    """Muestra el título principal del proyecto."""
    print("\n" + AZUL + NEGRITA + "═" * 72)
    print(titulo.center(72))
    print("═" * 72 + RESET)


def mostrar_seccion(numero, titulo, contenido):
    """Muestra cada sección del plan de algoritmos."""
    print(
        f"\n{CIAN}{NEGRITA}"
        f"{'─' * 72}\n"
        f"{numero}. {titulo}\n"
        f"{'─' * 72}"
        f"{RESET}"
    )
    print(contenido.strip())


def mostrar_lista(titulo, elementos):
    """Muestra una lista de elementos."""
    print(f"\n{AMARILLO}{NEGRITA}{titulo}:{RESET}")

    for elemento in elementos:
        print(f"  • {elemento}")


# ==============================================================
# TÍTULO DEL PROYECTO
# ==============================================================

mostrar_titulo(
    "PLAN DE ALGORITMOS: CNN + K-MEANS"
)

print(f"""
{BLANCO}
Para el desarrollo del proyecto se propone utilizar una Red Neuronal
Convolucional (CNN) como algoritmo principal y K-means como algoritmo
complementario de agrupamiento.

La selección de ambos métodos responde a las características del problema
planteado y al tipo de datos disponibles en el dataset SDNET2018, compuesto
por imágenes de superficies de concreto con y sin presencia de fisuras.

El objetivo del proyecto es detectar automáticamente la presencia de fisuras
y, posteriormente, establecer una agrupación basada en características
cuantitativas asociadas a su espesor, con la finalidad de contribuir a la
priorización de la inspección visual de las zonas identificadas.
{RESET}
""")


# ==============================================================
# 1. RED NEURONAL CONVOLUCIONAL (CNN)
# ==============================================================

mostrar_seccion(
    1,
    "RED NEURONAL CONVOLUCIONAL (CNN)",
    """
La Red Neuronal Convolucional (CNN) será utilizada como modelo principal
de aprendizaje supervisado para la clasificación binaria de las imágenes
en dos categorías:

    ✓ Con fisura (Cracked)
    ✓ Sin fisura (Uncracked)

Este algoritmo resulta adecuado debido a su capacidad para procesar imágenes
y aprender automáticamente características visuales relevantes.
"""
)

mostrar_lista(
    "Características visuales consideradas",
    [
        "Bordes",
        "Texturas",
        "Contornos",
        "Formas",
        "Patrones asociados con la presencia de fisuras"
    ]
)

mostrar_lista(
    "Variables de entrada",
    [
        "Valores de intensidad de los píxeles RGB",
        "Textura superficial",
        "Bordes y contornos",
        "Forma y orientación de las fisuras",
        "Contraste",
        "Iluminación",
        "Ruido visual"
    ]
)

print(
    f"\n{VERDE}{NEGRITA}"
    "VARIABLE DE SALIDA:"
    f"{RESET} Presencia o ausencia de fisura."
)

print("""
La elección de una CNN se justifica porque las fisuras presentan patrones
espaciales y geométricos que pueden variar en forma, orientación y apariencia.

Asimismo, las imágenes del dataset SDNET2018 contienen condiciones visuales
complejas, como sombras, rugosidad superficial, bordes, agujeros y residuos
de fondo.

Por ello, se requiere un modelo capaz de aprender características relevantes
directamente a partir de las imágenes y generalizar ante diferentes
condiciones de inspección.
""")


# ==============================================================
# 2. ALGORITMO K-MEANS
# ==============================================================

mostrar_seccion(
    2,
    "ALGORITMO K-MEANS",
    """
Como algoritmo complementario se propone utilizar K-means, correspondiente
a una técnica de aprendizaje no supervisado.

Su función será explorar el agrupamiento de las fisuras detectadas a partir
de características cuantitativas previamente extraídas, principalmente
aquellas asociadas al espesor estimado de la fisura.
"""
)

mostrar_lista(
    "Niveles de prioridad propuestos",
    [
        "Nivel 1 → LEVE",
        "Nivel 2 → MODERADA",
        "Nivel 3 → SEVERA",
        "Nivel 4 → CRÍTICA"
    ]
)

print(
    f"\n{VERDE}{NEGRITA}"
    "CONFIGURACIÓN INICIAL:"
    f"{RESET} K = 4 clústeres"
)

print("""
Posteriormente, los grupos obtenidos podrán compararse con los rangos de
espesor definidos en el proyecto para analizar la correspondencia entre
los patrones identificados por el algoritmo y las categorías propuestas
de prioridad de inspección.
""")

print(
    f"{AMARILLO}{NEGRITA}"
    "IMPORTANTE:"
    f"{RESET}"
)

print("""
K-means no detecta ni mide directamente el espesor de una fisura.

Antes de aplicar el algoritmo será necesaria una etapa de procesamiento
y extracción de características que permita obtener una representación
cuantitativa de cada fisura.

De esta manera, K-means se utilizará para agrupar las observaciones según
su similitud y no como un clasificador supervisado con etiquetas predefinidas.
""")


# ==============================================================
# 3. FLUJO GENERAL PROPUESTO
# ==============================================================

mostrar_seccion(
    3,
    "FLUJO GENERAL PROPUESTO",
    """
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
│   CLASIFICACIÓN DE LA IMAGEN            │
│      CON FISURA / SIN FISURA            │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│  EXTRACCIÓN DE CARACTERÍSTICAS          │
│          DE LA FISURA                   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│               K-MEANS                   │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│   AGRUPAMIENTO POR CARACTERÍSTICAS      │
└────────────────────┬────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────┐
│ NIVEL DE PRIORIDAD DE INSPECCIÓN        │
└─────────────────────────────────────────┘
"""
)


# ==============================================================
# 4. JUSTIFICACIÓN DE LA SELECCIÓN
# ==============================================================

mostrar_seccion(
    4,
    "JUSTIFICACIÓN DE LA SELECCIÓN",
    """
La combinación de ambos algoritmos permite abordar dos etapas diferentes
y complementarias del problema.

CNN:
Resuelve la tarea principal de detección automática de fisuras mediante
visión artificial.

K-MEANS:
Permite explorar agrupaciones naturales de las fisuras a partir de
características cuantitativas asociadas a su espesor.

En conjunto, la metodología propuesta busca superar una clasificación
limitada a "fisura/no fisura" y proporcionar información adicional que
contribuya a establecer un Índice de Prioridad de Inspección Visual (IPIV).

El IPIV permitirá orientar al equipo técnico hacia las zonas que requieren
una revisión prioritaria.
"""
)
