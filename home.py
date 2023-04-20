import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(page_title="Home")
df=pd.read_csv('open_pubs2.csv')

st.sidebar.success("navigate pages ^ ")
st.title("Open Pubs near me")
st.subheader('Dataset')
st.dataframe(df)

st.subheader('Covariance in dataset')
st.dataframe(df.cov())

st.subheader('Satistical Analysis')    
st.dataframe(df.describe())

st.subheader('Correlation')  
st.dataframe(df.corr())

st.subheader('Visualization of pubs under each authority')
img = Image.open("EDA.png") 
st.image(img, width=700)