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

# Read data
xls_file = pd.ExcelFile('PrizePicksDashboard.xlsx')

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", 'Prize Pick Dashboard', 'Manage Subscription'], 
        icons=['house', 'speedometer', 'tags'], menu_icon="cast", default_index=0)
    st.button('Login')

# for Home
if selected == 'Home':
    st.title('This is home page')


# for Dashboard
if selected == 'Prize Pick Dashboard':
    dataset_option = st.sidebar.selectbox('Select Sports',('NBA', 'HNL'))

    if dataset_option == 'NBA':
        df_nba = pd.read_excel(xls_file, sheet_name='PrizePicksNBA')
        st.dataframe(df_nba)

    if dataset_option == 'HNL':
        df_nhl = pd.read_excel(xls_file, sheet_name='PrizePicksNHL')
        st.dataframe(df_nhl)

# for Subscription
if selected == 'Manage Subscription':
    st.title('Comming soon')