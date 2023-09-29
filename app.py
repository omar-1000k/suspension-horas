import streamlit as st
from streamlit_option_menu import option_menu
from Cargar import cargar_archivo


def principal():

    with st.sidebar:
        choose = option_menu("Menú", ["Carga Archivo"],
                            icons=['person-plus'],
                            menu_icon="house", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "#000000", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#ECECEC"},
            "nav-link-selected": {"background-color": "#ECECEC"},
        }
        )

    if choose == "Carga Archivo":
        cargar_archivo()

principal()