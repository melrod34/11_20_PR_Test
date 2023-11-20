import streamlit as st
import pandas as pd

baseball_df = pd.read_csv('UNCWBaseballc.csv')

st.dataframe(baseball_df)