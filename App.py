import streamlit as st
import pandas as pd
import numpy as np


import time 
st.title('AI-Research-Assistance')

st.subheader("Hi I am summer: Your research help Assistant ")

row1 = st.columns(2)
row2 = st.columns(2)

grid =[col.container(height= 200) for col in row1 + row2]