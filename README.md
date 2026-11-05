# Juego-de-la-Vida
Recreando el juego de la vida, creado por el matemático John Horton. Todo gracias al poderoso profe Paco.

# 1. Resumen
Este documento presenta el desarrollo e implementación del Juego de la Vida de John Conway en Python. El proyecto integra una interfaz gráfica interactiva desarrollada en Streamlit, un motor lógico para la evolución del autómata celular.

# 2. Introducción: Problema
El Juego de la Vida es un autómata celular donde el estado futuro de una celda (viva o muerta) se determina a partir de un conjunto de reglas basadas en la cantidad de celdas vecinas vivas. El desafío técnico consiste en modelar eficientemente la matriz del tablero, gestionar el comportamiento de los bordes (toroidal o fijo) y permitir la interacción fluida del usuario en tiempo real.

# 3. Introducción: Objetivos

# Objetivo General
Desarrollar una aplicación interactiva funcional del Juego de la Vida utilizando Python, Streamlit y NumPy, garantizando la calidad del código mediante pruebas automatizadas.

# Objetivos Particulares
* Diseñar la lógica del motor de simulación y el manejo de matrices.
* Implementar una interfaz gráfica en Streamlit para configurar patrones iniciales y controlar la ejecución.
* Establecer un flujo de trabajo colaborativo en GitHub con control de versiones estructurado.

# 4. Solución

Gracias a las tutorias y guías que seguimos para desarrollar el código, el proceso de desarollo no contó con errores mayores o significativos

# 5. Conclusiones

# Conclusiones Generales
El desarrollo del proyecto permitió integrar herramientas de desarrollo colaborativo, desarrollo web rápido y verificación de código en un entorno modular de Python.
El trabajo colaborativo permitio trabajar en conjunto para la resolucion de problemas durante el proyecto, asi como una gestion y organizacion para estructurar el proyecto.

# Conclusiones Particulares
* Andres (Lógica del Juego): [Breve reflexión sobre los retos al implementar las reglas y matrices].
* Erik (Interfaz Gráfica): [Breve reflexión sobre el rendimiento visual y la experiencia de usuario en Streamlit].
* Jose (Integración y Documentación):La gestión del repositorio permitió estructurar una base clara y estandarizada desde el inicio, facilitando el trabajo paralelo del equipo. El uso de ramas dedicadas y la revisión continua de Pull Requests fueron clave para prevenir y resolver conflictos de código de manera ordenada antes de integrar los cambios a la rama principal. Asimismo, mantener la documentación modular y actualizada en tiempo real aseguró la coherencia técnica del proyecto y facilitó la verificabilidad y reproducibilidad del sistema.

# 6. Reproducibilidad

# Requisitos Previos
* Python 3.10 o superior.
* Git.

# Dependencias
Las dependencias requeridas están listadas en `requirements.txt`:
```txt
streamlit
numpy
pytest