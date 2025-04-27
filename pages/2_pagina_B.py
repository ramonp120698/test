import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utilidades as util
util.generarMenu()
st.header('Página B')
