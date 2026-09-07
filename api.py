import streamlit as st  # Importa Streamlit para construir la calculadora.
st.title("Calculadora API")  # Muestra el título principal de la página.
sg = st.number_input("Gravedad específica", value=0.85)  # Permite ingresar la gravedad específica.
if st.button("Calcular"):  # Ejecuta el cálculo cuando el botón es presionado.
    api = (141.5 / sg) - 131.5  # Calcula el grado API a partir del valor ingresado.
    st.success(f"{api:.2f} °API")  # Presenta el resultado calculado.
if st.button("Regresar"):  # Comprueba si el usuario desea volver al inicio.
    st.switch_page("inicio.py")  # Cambia programáticamente hacia la página de inicio.
