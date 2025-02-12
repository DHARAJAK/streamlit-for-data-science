import streamlit as st
import pandas as pd
import plotly.express as px

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Fransisco using a dataset kindly provided by SF DPW"""
)
st.subheader("Plotly Chart")
trees_df = pd.read_csv("trees.csv")
st.write(trees_df.head())
fig = px.histogram(trees_df["dbh"])
st.plotly_chart(fig)
