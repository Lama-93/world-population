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
# Add a slider for selecting the population range
population_slider = st.slider('Select Population Range', min_value=WorldPopulation2023['Population2023'].min(), max_value=WorldPopulation2023['Population2023'].max(), value=(0, WorldPopulation2023['Population2023'].max()))

# Filter the data based on the selected population range
filtered_data = WorldPopulation2023[(WorldPopulation2023['Population2023'] >= population_slider[0]) & (WorldPopulation2023['population'] <= population_slider[1])]

# Create the suicide rate map for the selected year
def create_suicide_rate_map(filtered_data):
    # Create the choropleth map
    fig_map = px.choropleth(
        filtered_data,
        locations="country",
        locationmode='country names',
        color="Population2023",
        hover_name="country",
        projection="natural earth",
        title="Population Rate by Country",
        color_continuous_scale=px.colors.sequential.Viridis,
        labels={'WorldPopulation2023': 'Population2023'},
    )

    fig_map.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")

    return fig_map

# Display the map in the Streamlit app
fig = create_suicide_rate_map(filtered_data)
st.plotly_chart(fig)
