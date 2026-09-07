import streamlit as st  # Importa Streamlit para trabajar con widgets y estado de sesión.
st.title("Ingreso de datos")  # Muestra el título de la página actual.
if "sg" not in st.session_state: st.session_state.sg = 0.85  # Crea sg en session_state solamente si todavía no existe.
st.session_state.sg = st.number_input("Gravedad específica", value=st.session_state.sg)  # Actualiza y conserva el valor de sg en la sesión.
if st.button("Calcular en otra página"):  # Detecta si el usuario desea continuar hacia el resultado.
    st.switch_page("api.py")  # Cambia de página sin perder el dato almacenado en session_state.
