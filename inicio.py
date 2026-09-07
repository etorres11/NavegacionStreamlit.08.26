import streamlit as st  # Importa Streamlit para crear la interfaz de inicio.
st.title("Inicio")  # Muestra el encabezado principal.
st.write("Ahora la navegación puede activarse desde Python.")  # Introduce el propósito de st.switch_page.
if st.button("Abrir calculadora"):  # Comprueba si el usuario presionó el botón.
    st.switch_page("api.py")  # Cambia programáticamente desde Inicio hacia la página api.py.
