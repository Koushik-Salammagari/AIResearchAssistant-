import streamlit as st
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import About, Account, Home


import time 

st.set_page_config(page_title = "Summer")


st.title('AI-Research-Assistance')

st.subheader("Hi I am summer: Your research help Assistant ")

row1 = st.columns(3)
row2 = st.columns(3)

grid =[col.container(height= 200) for col in row1 + row2]

class MultiApp:

    def __init__(self):
        self.apps = []
    
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="SummerAI",
                options=['Home', 'About', 'Account'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},

                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

            if app == 'Home':
                Home.app()
            if app == "About":
                About.app()
            if app == "Account":
                Account.app()
            
    run()

# if __name__ == "__main__":
#     run()

    
                





