import streamlit as st

def generarMenu():
    with st.sidebar:
        st.page_link('pages/appPrincipal.py',label="Inicio", icon="🏚️")
        st.page_link('pages/1_pagina_A.py',label="Tablero A", icon="📄")
        st.page_link('pages/2_pagina_B.py',label="Tablero B", icon="📄")
        st.page_link('pages/pagina_C.py',label="Tablero C", icon="📄")
