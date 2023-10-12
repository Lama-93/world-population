import streamlit as st
import pandas as pd
import plotly.express as px
import random
import numpy as np

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

# Create a filter to select a random set of 3 countries for comparison
default_countries = random.sample(data["Country"].unique().tolist(), 3)
selected_countries = st.sidebar.multiselect("Select Countries for Comparison", data["Country"].unique(), default=default_countries)

# Filter the data based on the selected countries
filtered_data = data[data["Country"].isin(selected_countries)]

# Display a bar chart for the selected countries' population
if not filtered_data.empty:
    st.write("## Population for Selected Countries")
    fig_bar = px.bar(filtered_data, x="Country", y="Population2023", title="Population Comparison")
    st.plotly_chart(fig_bar)
else:
    st.write("No data selected. Please choose one or more countries for comparison.")




# Get unique median age values from the dataset
median_age_values = np.sort(data["MedianAge"].unique())

# Create a slider for selecting median age
selected_median_age = st.slider("Select Median Age", min_value=int(min(median_age_values)), max_value=int(max(median_age_values)), value=int(min(median_age_values)))

# Round the selected median age to the nearest integer
selected_median_age = int(selected_median_age)

# Filter the data based on the selected median age
filtered_data = data[data["MedianAge"] == selected_median_age]

# Create a choropleth map with median age data
st.write("## World Population Choropleth Map by Median Age")
fig_map = px.choropleth(
    filtered_data,
    locations="Country",
    locationmode="country names",
    color="MedianAge",
    title=f"World Population Median Age in {selected_median_age}",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma,
)

fig_map.update_geos(
    showcoastlines=True,
    coastlinecolor="Black",
)

st.plotly_chart(fig_map)
