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

# Create a multi-select widget to select multiple countries
selected_countries = st.sidebar.multiselect("Select Countries for Comparison", data["Country"].unique())

# Filter the data based on the selected countries
filtered_data = data[data["Country"].isin(selected_countries)]

# Display a bar chart for the selected countries' population
if not filtered_data.empty:
    st.write("## Population for Selected Countries")
    fig_bar = px.bar(filtered_data, x="Country", y="Population2023", title="Population Comparison")
    st.plotly_chart(fig_bar)
else:
    st.write("No data selected. Please choose one or more countries for comparison.")
