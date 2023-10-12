import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/Lama-93/world-population/main/WorldPopulation2023.csv'
    data = pd.read_csv(url)
    return data

# Load the data
data = load_data()

# Set the title and introductory text for your app
st.title("Population Data Analysis for 2023")
st.write("Explore population data for the year 2023.")

# Create a slider for population
selected_population = st.slider("Select a Population Range", int(data["Population2023"].min()), int(data["Population2023"].max()), (int(data["Population2023"].min()), int(data["Population2023"].max())))

# Filter the data based on the selected population range
filtered_data = data[(data["Population2023"] >= selected_population[0]) & (data["Population2023"] <= selected_population[1])]

# Create a map based on the filtered data
st.subheader("Map of Countries by Population")
fig = px.scatter_geo(
    filtered_data,
    locations="Country",
    locationmode="country names",
    text="Country",
    size="Population2023",
    projection="natural earth",
)

fig.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")

# Display the map
st.plotly_chart(fig)
