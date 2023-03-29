import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from streamlit_extras.dataframe_explorer import dataframe_explorer
from ipyvizzu import Chart, Data, Config, Style

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
    st.markdown("<h1 style='text-align: center;'>Welcome<br> to Prize Picks Dashboard <br> Data visualization in sports </h1>", unsafe_allow_html=True)

    st.markdown(
    """
    <style>
        div[data-testid="column"]:nth-of-type(1)
        {
            text-align: center;
            height: 500px;
        } 

        div[data-testid="column"]:nth-of-type(2)
        {
            text-align: center;
        }
        div[data-testid="column"]:nth-of-type(3)
        {
            text-align: center;
        } 
    </style>
    """,unsafe_allow_html=True
    )            

    col1, col2, col3 = st.columns(3)
    with col1:
        """
        ## Sports Dashboard
        """
        ch_col1, ch_col2 = st.columns([1, 2])
        ch_col1.image("computer_data.png")
        with ch_col2:
            st.write('Easily View Lines Across Books')
            st.write('Find The Top Picks in Seconds')
            st.write('Display Adjusted Odds Based Various Calculations')
            st.write('Efficiently Build Slips for many DFS sites')

    with col2:
        """
        ## SportsBook Player Props
        """
        ch_col3, ch_col4 = st.columns([1, 2])
        ch_col3.image("clipboard.png")
        with ch_col4:
            st.write('Compare Lines/Odds from Many Books')
            st.write('Easily Filterable')
            st.write('Draftkings, Pinnacle, Betonline, and Bovada')
            st.write('Currently Offered and many more to come')

    with col3:
        """
        ## Player Stats 
        """
        ch_col5, ch_col6 = st.columns([1, 2])
        ch_col5.image("crown.png")
        with ch_col6:
            st.write('Coming Soon')
            st.write('Display Historical Stats')
            st.write('Over/Under Hit Rate')
            st.write('Projected Stats')

# for Dashboard
if selected == 'Prize Pick Dashboard':
    st.sidebar.header('Data filtering metrix:')
    dataset_option = st.sidebar.selectbox('Select sports',('NBA', 'HNL'))

    if dataset_option == 'NBA':
        df_nba = pd.read_excel(xls_file, sheet_name='PrizePicksNBA')
        #st.dataframe(df_nba)
        st.header('NBA Dataset')
        team_name_nba = st.sidebar.multiselect(
            'Select NBA Team',
            options=df_nba['Team Name'].unique().tolist(),
            default=df_nba['Team Name'].unique()
        )

        filtered_nba_df = df_nba[df_nba["Team Name"].isin(team_name_nba)]
        st.dataframe(filtered_nba_df)

    if dataset_option == 'HNL':
        df_nhl = pd.read_excel(xls_file, sheet_name='PrizePicksNHL')
        #st.dataframe(df_nhl)
        st.header('HNL Dataset')
        team_name_nhl = st.sidebar.multiselect(
            'Select NHL Team',
            options=df_nhl['Team Name'].unique().tolist(),
            default=df_nhl['Team Name'].unique()
        )

        filtered_nha_df = df_nhl[df_nhl["Team Name"].isin(team_name_nhl)]
        st.dataframe(filtered_nha_df)
        
# for Subscription
if selected == 'Manage Subscription':
    st.title('Comming soon')