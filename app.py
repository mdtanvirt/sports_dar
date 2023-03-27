import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

#st.title('This is Tanvir')
nav = st.sidebar.radio("Navigation", ["Home", "Prediction", "Conribute"])