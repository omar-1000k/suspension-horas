import streamlit as st
from app.app import principal

if not st.user.is_logged_in:
    st.image("Puebla.jpg")
    if st.button("Iniciar sesión"):
        st.login()
else:
    if st.button("Cerrar sesión"):
        st.logout()
    
    principal()