import streamlit as st  # Importa la librería Streamlit con el alias st.
inicio = st.Page("inicio.py", title="Inicio", icon="🏠", default=True)  # Define la página inicial con título, ícono y estado predeterminado.
api = st.Page("api.py", title="Grado API", icon="🛢️")  # Define la página de cálculo con un título e ícono personalizados.
pagina = st.navigation([inicio, api])  # Organiza las páginas dentro del menú automático de Streamlit.
pagina.run()  # Ejecuta únicamente la página seleccionada por el usuario.

