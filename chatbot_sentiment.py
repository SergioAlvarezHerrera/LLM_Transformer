import streamlit as st
from transformers import pipeline

# Cargar el modelo de análisis de sentimiento
sentiment_pipeline = pipeline("sentiment-analysis")

# Interfaz con Streamlit
st.title("Chatbot de Análisis de Sentimiento 🤖")

# Input del usuario
user_input = st.text_area("Escribe un texto para analizar:")

# Procesar el texto cuando el usuario presiona el botón
if st.button("Analizar Sentimiento"):
    if user_input:
        result = sentiment_pipeline(user_input)[0]
        st.write(f"**Sentimiento:** {result['label']}")
        st.write(f"**Confianza:** {result['score']:.2f}")
    else:
        st.warning("Por favor, escribe un texto para analizar.")

