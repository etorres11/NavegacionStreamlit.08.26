import streamlit as st  # Importa Streamlit para crear elementos de interfaz.
st.title("Inicio")  # Muestra el título de la página de inicio.
st.write("También podemos crear enlaces visibles hacia otras páginas.")  # Explica el propósito del ejemplo.
st.page_link("api.py", label="Ir a la calculadora API", icon="🛢️")  # Crea un enlace visible que lleva a la página api.py.
