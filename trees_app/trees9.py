import streamlit as st
import pandas as pd
import pydeck as pdk

st.title("SF Trees")
st.write(
    """This app analyzes trees in San Francisco using
a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv("trees.csv")
trees_df.dropna(how="any", inplace=True)
sf_initial_view = pdk.ViewState(latitude=37.77, longitude=-122.4, zoom=11, pitch=30)

sp_layer = pdk.Layer(
    "ScatterplotLayer",
    data=trees_df,
    get_position=["longitude", "latitude"],
    get_radius=30,
)

st.pydeck_chart(
    pdk.Deck(
        initial_view_state=sf_initial_view,
        map_style="mapbox://styles/mapbox/light-v9",
        layers=[sp_layer],
    )
)
