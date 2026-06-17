
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Airline Passenger Segmentation",
    layout="wide"
)

st.title("✈️ Airline Passenger Segmentation")

st.write("Dashboard Hasil Clustering Penumpang Maskapai")

df = pd.read_csv("df_vif_clean.csv")

st.subheader("Dataset Overview")
st.dataframe(df.head())

st.subheader("Informasi Dataset")
st.write(f"Jumlah Baris: {df.shape[0]}")
st.write(f"Jumlah Kolom: {df.shape[1]}")
