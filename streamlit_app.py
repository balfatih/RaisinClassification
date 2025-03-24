
import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('🚧 Machine Learning Application for Raisin Classification')

st.info("This application was developed for Raisin Classification. ")

with st.expander('Raisin Dataset'):
  st.write('Raw Data')
  df = pd.read_csv('https://raw.githubusercontent.com/balfatih/RaisinClassification/refs/heads/main/Dataset/Raisin_Dataset.csv')
  df

  st.write('**X***')
  X = df.drop('Class', axis=1)
  X

  st.write('**X***')
  y = df.Class
  y

with st.expander("📊 Data Visualization"):
    # Matplotlib figürü oluştur
    fig, ax = plt.subplots()
    sns.histplot(
        data=df,
        x='Area',
        hue='Class',
        kde=True,
        multiple='stack',
        ax=ax  # Grafik nesnesini burada belirtiyoruz
    )
    ax.set_title('Area & Classes', fontsize=15)

    # Streamlit'te grafiği göster
    st.pyplot(fig)

    # Matplotlib figürü oluştur
    fig, ax = plt.subplots()
    sns.histplot(
        data=df,
        x='Perimeter',
        hue='Class',
        kde=True,
        multiple='stack',
        ax=ax  # Grafik nesnesini burada belirtiyoruz
    )
    ax.set_title('Area & Classes', fontsize=15)

    # Streamlit'te grafiği göster
    st.pyplot(fig)
