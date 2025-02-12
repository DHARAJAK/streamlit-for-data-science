import streamlit as st
import pandas as pd
import altair as alt

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv("trees.csv")
st.write(trees_df)
fig = alt.Chart(trees_df).mark_bar().encode(x="caretaker", y="tree_id")
st.altair_chart(fig)
