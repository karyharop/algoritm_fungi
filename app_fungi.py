import streamlit as st
import joblib 
import numpy as np

# 1. Cargamos las herramientas que congelamos en el paso anterior
model = joblib.load('modelo_hongos.pkl')
le = joblib.load('encoder_hongos.pkl')

# 2. Diseñamos la interfaz (¡Cero HTML, solo lógica!)
st.title("🍄 Clasificador Inteligente de Hongos")
st.write("¡WELCOME! Selecciona las características del hongo para que el algoritmo lo analice.")

st.divider() # Una línea visual muy elegante para separar secciones

# 3. Creamos los menús desplegables para el usuario (aquí es donde hay que agregar las 10 características)
olor_usuario = st.selectbox("¿A qué huele el hongo?", ["Almendras", "Anís", "Pescado", "No huele"])
forma_sombrero = st.selectbox("Forma del sombrero:", ["Campana", "Plano", "Convexo"])
color_laminas = st.selectbox("Color de las láminas:", ["Morado", "Amarillo", "Blanco", "Rosa"])

st.divider()

# 4. El botón mágico de acción
if st.button("Analizar Muestra 🔬"):
    # Aquí dentro ocurrirá la magia:
    # Convertiremos lo que elija el usuario a números y el árbol dará su veredicto
    
    # De momento te dejo un adelanto visual de cómo se verá el resultado:
    st.success("¡Análisis completado! El algoritmo dice: ¡COMESTIBLE! 🥗")