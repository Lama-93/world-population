import streamlit as st
import pandas as pd
!pip install plotly
import plotly.express as px

# Load the dataset from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/Lama-93/world-population/main/WorldPopulation2023.csv'
    data = pd.read_csv(url)
    return data

# Load the data
data = load_data()
# Create a Streamlit app
st.title('World Population 2023 Map')

# Add a slider for selecting the population range
population_slider = st.slider('Select Population Range', min_value=0, max_value=world_population_data['Population2023'].max(), value=(0, world_population_data['Population2023'].max()))

# Filter the data based on the selected population range
filtered_data = world_population_data[(world_population_data['Population2023'] >= population_slider[0]) & (world_population_data['Population2023'] <= population_slider[1])]

# Create a choropleth map
fig_map = px.choropleth(
    filtered_data,
    locations="Country",  # Replace with the appropriate column name from your dataset
    locationmode='country names',
    color="Population2023",  # Replace with the appropriate column name from your dataset
    hover_name="Country",  # Replace with the appropriate column name from your dataset
    projection="natural earth",
    title="World Population 2023 by Country",
    color_continuous_scale=px.colors.sequential.Viridis,
    labels={'Population2023': 'Population 2023'},
)

fig_map.update_geos(showcoastlines=True, coastlinecolor="Black", showland=True, landcolor="white")

# Display the map in the Streamlit app
st.plotly_chart(fig_map)
