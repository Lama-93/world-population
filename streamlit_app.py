import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv("WorldPopulation2023.csv")
    return data

data = load_data()

# Set the title of your app
st.title("World Population 2023 Data Visualization")

# Display the dataset (optional)
st.dataframe(data)

# Create a filter to select a country
selected_country = st.sidebar.selectbox("Select a Country", data["Country"].unique())

# Filter the data based on the selected country
filtered_data = data[data["Country"] == selected_country]

# Display a bar chart for the selected country's population
st.write("## Population for Selected Country")
fig_bar = px.bar(filtered_data, x="Country", y="Population2023", title=f"Population for {selected_country}")
st.plotly_chart(fig_bar)
