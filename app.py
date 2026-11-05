#importamos las librerias que utilizaremos para la interfaz
import streamlit as st
import numpy as np
import time
#importamos la logica del juego que hizo el muchacho Andres
from engine import update, N, ON, OFF

# Configuración de la página
st.set_page_config(page_title="Juego de la Vida", layout="centered")

st.title("Juego de la Vida")
st.write("Selecciona las células que quieres activar.")

# Diseño de las célulitas del tablero
st.markdown("""
<style>
.st-key-tablero button {
    width: 100%;
    min-height: 0;
    height: auto;
    aspect-ratio: 1 / 1;
    padding: 0;
    border-radius: 0;
}
 
/* Células vivas */
.st-key-tablero button[kind="primary"] {
    background-color: black !important;
    border: 1px solid #777777;
}

/* Células muertas */
.st-key-tablero button[kind="secondary"] {
    background-color: white !important;
    border: 1px solid #777777;
}

/* Mantener colores al pasar el mouse */
.st-key-tablero button[kind="primary"]:hover {
    background-color: black !important;
}

.st-key-tablero button[kind="secondary"]:hover {
    background-color: white !important;
}

/* Mantener colores durante la animación */
.st-key-tablero button:disabled {
    opacity: 1;
}
</style>
""", unsafe_allow_html=True)

# Guardamos los datos del juego en la sesión de Streamlit para que no se pierdan al actualizar la página
if "tablero" not in st.session_state:
    st.session_state.tablero = np.full((N, N), OFF)

if "generaciones" not in st.session_state:
    st.session_state.generaciones = 0

if "jugando" not in st.session_state:
    st.session_state.jugando = False

# Velocidades del juego 
velocidades = {
    "Normal": 0.7,
    "Rapidillo": 0.3,
    "Velociraptor": 0.08
}

# Cambiar el estado de una célula
def cambiar_celula(i, j):
    if not st.session_state.jugando:
        if st.session_state.tablero[i, j] == OFF:
            st.session_state.tablero[i, j] = ON
        else:
            st.session_state.tablero[i, j] = OFF

# Calcular la siguiente generación 
def siguiente_generacion():
    st.session_state.tablero = update(st.session_state.tablero)
    st.session_state.generaciones += 1

# Iniciar la simulación
def iniciar():
    st.session_state.jugando = True

# Detener la simulación
def detener():
    st.session_state.jugando = False

# Reiniciar el juego
def reiniciar():
    st.session_state.jugando = False
    st.session_state.tablero = np.full((N, N), OFF)
    st.session_state.generaciones = 0

# Mostrar contador de generaciones
st.write("Generación:", st.session_state.generaciones)

# Centrar el tablero
izquierda, centro, derecha = st.columns([1, 3, 1])

with centro:
    with st.container(key="tablero"):

        for i in range(N):
            columnas = st.columns(N, gap=None)

            for j in range(N):
                viva = st.session_state.tablero[i, j] == ON

                columnas[j].button(
                    " ",
                    key=f"celula_{i}_{j}",
                    type="primary" if viva else "secondary",
                    on_click=cambiar_celula,
                    args=(i, j),
                    disabled=st.session_state.jugando,
                    use_container_width=True
                )

# Botones de control pa el tablero
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("Iniciar", on_click=iniciar)

with col2:
    st.button("Detener", on_click=detener)

with col3:
    st.button(
        "Siguiente",
        on_click=siguiente_generacion,
        disabled=st.session_state.jugando
    )

with col4:
    st.button("Reiniciar", on_click=reiniciar)

# Seleccionar velocidad
velocidad = st.selectbox(
    "Velocidad",
    list(velocidades.keys())
)

# Animación del juego :)
if st.session_state.jugando:
    time.sleep(velocidades[velocidad])
    siguiente_generacion()
    st.rerun()
