import streamlit as st  # Importa Streamlit para recuperar el estado de sesión.
st.title("Resultado")  # Muestra el título de la página de resultados.
sg = st.session_state.get("sg", 0.85)  # Recupera sg guardado o utiliza 0.85 si todavía no existe.
api = (141.5 / sg) - 131.5  # Calcula el grado API con el valor conservado entre páginas.
st.metric("Grado API", f"{api:.2f} °API")  # Presenta el resultado mediante un widget métrico.
st.write("SG conservada:", sg)  # Confirma visualmente el valor que viajó entre páginas.
if st.button("Modificar dato"):  # Comprueba si el usuario quiere regresar a editar el valor.
    st.switch_page("inicio.py")  # Regresa a la página de ingreso manteniendo session_state.
