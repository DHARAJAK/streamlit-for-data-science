import streamlit as st
import pandas as pd
import altair as alt
import seaborn as sns

st.title("Palmer's Penguins")
st.markdown("Use this streamlit app to make your own scatter plot")


penguin_file = st.file_uploader("Select Your local Penguins CSV(defualt)")
if penguin_file is not None:
    penguin_df = pd.read_csv(penguin_file)
else:
    penguin_df = pd.read_csv("penguins.csv")


selected_x_var = st.selectbox(
    "What do you want the x variable to be ?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)

selected_y_var = st.selectbox(
    "what about the y?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)

selected_gender = st.selectbox(
    "What gender do you want to filter for?",
    ["all penguins", "male penguins", "female penguins"],
)

if selected_gender == "male penguins":
    penguin_df = penguin_df[penguin_df["sex"] == "male"]
elif selected_gender == "female penguins":
    penguin_df = penguin_df[penguin_df["sex"] == "female"]
else:
    pass


# sns.set_style("darkgrid")
# markers = {"Adelie": "X", "Gentoo": "s", "Chinstrap": "o"}

alt_chart = (
    alt.Chart(penguin_df, title="Scatterplot of Palmer's Penguins")
    .mark_circle()
    .encode(x=selected_x_var, y=selected_y_var, color="species")
    .interactive()
)

st.altair_chart(alt_chart, use_container_width=True)
