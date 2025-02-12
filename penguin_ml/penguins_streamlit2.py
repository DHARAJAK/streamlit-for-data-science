import streamlit as st
import seaborn as sns

import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Penguin Classifier")
st.write(
    """
This app uses 6 inputs to predict the species of a penguin using a model build on the Palmer's Penguins dataset.
         Use the form below to get started!"""
)

penguin_file = st.file_uploader("Upload your own penguin data")

if penguin_file is None:
    rf_pickle = open("random_forest_penguin.pkl", "rb")
    map_pickle = open("output_penguin.pkl", "rb")
    rfc = pickle.load(rf_pickle)
    unique_penguin_mapping = pickle.load(map_pickle)
    rf_pickle.close()
    map_pickle.close()
    penguin_df = pd.read_csv("penguins.csv")
else:
    penguin_df = pd.read_csv(penguin_file)
    penguin_df = penguin_df.dropna()
    output = penguin_df["species"]
    features = penguin_df[
        [
            "island",
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
            "sex",
        ]
    ]
    features = pd.get_dummies(features)
    output, unique_penguin_mapping = pd.factorize(output)
    x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=0.8)
    rfc = RandomForestClassifier(random_state=15)
    rfc.fit(x_train, y_train)
    y_pred = rfc.predict(x_test)
    score = round(accuracy_score(y_pred, y_test), 2)
    st.write(
        f"""We trained a Random Forest model on these data,
        it has a score of {score}! Use the
        inputs below to try out the model"""
    )

with st.form("user_inputs"):
    island = st.selectbox("Island", options=["Biscoe", "Dream", "Torgersen"])
    sex = st.selectbox("Sex", options=["Male", "Female"])
    bill_length = st.number_input("Bill length (mm)", min_value=0)
    bill_depth = st.number_input("Bill depth (mm)", min_value=0)
    flipper_length = st.number_input("Flipper length (mm)", min_value=0)
    body_mass = st.number_input("Body mass (g)", min_value=0)
    st.form_submit_button("Predict")

island_biscoe, island_dream, island_torgersen = 0, 0, 0
if island == "Biscoe":
    island_biscoe = 1
elif island == "Dream":
    island_dream = 1
elif island == "Torgersen":
    island_torgersen = 1

sex_female, sex_male = 0, 0

if sex == "Female":
    sex_female = 1
elif sex == "Male":
    sex_male = 1

new_prediction = rfc.predict(
    [
        [
            bill_length,
            bill_length,
            flipper_length,
            body_mass,
            island_biscoe,
            island_dream,
            island_torgersen,
            sex_female,
            sex_male,
        ]
    ]
)

prediction_species = unique_penguin_mapping[new_prediction[0]]

st.write(f"The predicted species is {prediction_species}")

st.image("feature_importance.png")

st.write(
    """Below are the histograms for each
continuous variable separated by penguin
species. The vertical line represents
your the inputted value."""
)

fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_length_mm"], hue=penguin_df["species"], kde=True)
plt.axvline(bill_length)
plt.title("Bill Length by species")
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["bill_depth_mm"], hue=penguin_df["species"], kde=True)
plt.axvline(bill_depth)
plt.title("Bill Depth by species")
st.pyplot(ax)
fig, ax = plt.subplots()
ax = sns.displot(x=penguin_df["flipper_length_mm"], hue=penguin_df["species"], kde=True)
plt.axvline(flipper_length)
plt.title("Flipper Length by species")
st.pyplot(ax)
