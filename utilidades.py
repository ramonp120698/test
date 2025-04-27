import streamlit as st

def generarMenu():
    with st.sidebar:
        st.page_link('appPrincipal.py',label="Home", icon="🏚️")
        st.page_link('pages/1_pagina_A.py',label="TAKA", icon="📄")
        st.page_link('pages/2_pagina_B.py',label="BYGA", icon="📄")
        st.page_link('pages/pagina_C.py',label="A-Champs", icon="📄")
