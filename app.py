import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

#st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden}
    footer {visibility: hidden}
    header {visibility: hidden}
    </style>
"""
#st.markdown(hide_st_style, unsafe_allow_html=True)
#st.header('Sports Analysis')

#st.title('This is Tanvir')
#nav = st.sidebar.radio("Navigation", ["Home", "Prediction", "Conribute"])
with st.sidebar:
    sselected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)