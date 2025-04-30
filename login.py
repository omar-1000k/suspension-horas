import streamlit as st
from app.app import principal

if not st.experimental_user.is_logged_in:
    st.image("Puebla.jpg")
    if st.button("Iniciar sesión"):
        st.login("google")
else:
    if st.button("Cerrar sesión"):
        st.logout()
    
    principal()
