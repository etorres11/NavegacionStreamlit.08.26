import streamlit as st  # Importa Streamlit para construir la calculadora.
st.title("Calculadora API")  # Muestra el título de esta página.
sg = st.number_input("Gravedad específica", value=0.85)  # Solicita la gravedad específica al usuario.
if st.button("Calcular"):  # Comprueba si el usuario presionó el botón Calcular.
    api = (141.5 / sg) - 131.5  # Calcula el grado API mediante la ecuación estándar.
    st.write("Grado API:", round(api, 2))  # Presenta el resultado redondeado a dos decimales.
