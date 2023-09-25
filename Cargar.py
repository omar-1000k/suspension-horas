from io import BytesIO
# from openpyxl import load_workbook
import streamlit as st
# import pandas as pd
from diferencia_horas import DiferenciaHoras

st.set_page_config("OLBOX")
st.title("Horas de suspención")
# st.header("Este es el encabezado")

def cargar_archivo():
    uploaded_file = st.file_uploader("Seleciona un Archivo",type=["xlsx"],label_visibility="collapsed")
    if uploaded_file is not None:
        # To read file as bytes:
        # bytes_data = uploaded_file.name
        # st.write(bytes_data)
        
        # wb = load_workbook(uploaded_file, read_only=False)

        # Can be used wherever a "file-like" object is accepted:
        df = DiferenciaHoras(uploaded_file)
        st.write(df)

        csv = df.to_csv(index=False).encode('utf-8')

        st.download_button(
        label="Descarga datos a CSV",
        data=csv,
        file_name='dif_horas.csv',
        mime='text/csv')
        
