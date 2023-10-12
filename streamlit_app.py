import streamlit as st
import pandas as pd

# Load the dataset from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/Lama-93/world-population/main/WorldPopulation2023.csv'
    data = pd.read_csv(url)
    return data

# Load the data
data = load_data()

# Set the title and introductory text for your app
st.title("Interactive World Population Data for 2023")
st.write("Explore world population data for the year 2023 on a map.")

# Create a slider for population
min_population = st.slider("Minimum Population", int(data["Population2023"].min()), int(data["Population2023"].max()), int(data["Population2023"].min()))
max_population = st.slider("Maximum Population", min_population, int(data["Population2023"].max()), int(data["Population2023"].max()))

# Filter the data based on the selected population range
filtered_data = data[(data["Population2023"] >= min_population) & (data["Population2023"] <= max_population)]

# Create a map based on the filtered data
st.subheader("Map of Countries by Population")
fig = px.scatter_geo(filtered_data, locations="Country", locationmode="country names", text="Country", size="Population2023", projection="natural earth")
fig.update_geos(showcoastlines=True, coastlinecolor="Black")
fig.update_layout(geo=dict(showland=True, landcolor="rgb(217, 217, 217)"))
st.plotly_chart(fig)
