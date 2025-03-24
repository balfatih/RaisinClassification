
import streamlit as st 
import pandas as pd

st.title('🚧 Machine Learning Application for Raisin Classification')

st.info("This application was developed for Raisin Classification. ")

with st.expander('Raisin Dataset'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/balfatih/RaisinClassification/refs/heads/main/Dataset/Raisin_Dataset.csv')
  df
