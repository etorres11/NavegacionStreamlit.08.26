import streamlit as st  # Importa Streamlit para construir la página de cálculo.
st.title("Calculadora API")  # Muestra el título de la calculadora.
sg = st.number_input("Gravedad específica", value=0.85)  # Solicita el valor de gravedad específica.
if st.button("Calcular"):  # Detecta el clic en el botón Calcular.
    api = (141.5 / sg) - 131.5  # Obtiene el grado API utilizando la fórmula estándar.
    st.success(f"{api:.2f} °API")  # Muestra el resultado calculado.
st.page_link("inicio.py", label="Volver al inicio", icon="🏠")  # Crea un enlace visible para regresar a la página inicial.
