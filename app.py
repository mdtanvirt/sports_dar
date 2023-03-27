import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# Hide streamlit default menu and footer from the template
hide_st_style = """
    <style>
    footer {visibility: hidden}
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)
#st.header('Sports Analysis')

#st.title('This is Tanvir')
#nav = st.sidebar.radio("Navigation", ["Home", "Prediction", "Conribute"])
with st.sidebar:
    sselected = option_menu("Main Menu", ["Home", 'Settings'], 
        icons=['house', 'gear'], menu_icon="cast", default_index=0)
    
st.title('Dashboard')
xls_file = pd.ExcelFile('PrizePicksDashboard.xlsx')
df_nba = pd.read_excel(xls_file, sheet_name='PrizePicksNBA')
df_nhl = pd.read_excel(xls_file, sheet_name='PrizePicksNHL')
st.dataframe(df_nba)  
st.dataframe(df_nhl)