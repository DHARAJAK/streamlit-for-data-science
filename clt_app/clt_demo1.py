import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Ilustrating the Central Limit Theorem with Streamlit")
st.subheader("An App By Tyler Richards")
st.write(
    (
        "This app simulates a thousand coin flips using the chance of heads input below,"
        "and then samples with replacement from that population and plots histogram of the ,"
        "means of the samples, in order to Illustrate the Central Limit Theorem"
    )
)

st.markdown(
    """
               :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text."""
)

perc_heads = st.number_input(
    label="Chance of coins landing on heads", min_value=0.0, max_value=0.5
)
graph_title = st.text_input(label="Graph Title")
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = []
for i in range(0, 1000):
    list_of_means.append(np.random.choice(binom_dist, 100, replace=True).mean())

fig1, ax1 = plt.subplots()
ax1 = plt.hist(list_of_means, range=[0, 1])
plt.title(graph_title)
st.pyplot(fig1)
