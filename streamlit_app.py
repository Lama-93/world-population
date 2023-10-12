import pandas as pd
import streamlit as st
import folium

# Load your "WorldPopulation2023" dataset
world_population_data = pd.read_csv('WorldPopulation2023.csv')

# Create a Streamlit app
st.title('World Population 2023 Map')

# Add a slider for selecting the population range
population_slider = st.slider('Select Population Range', min_value=0, max_value=world_population_data['Population2023'].max(), value=(0, world_population_data['Population2023'].max()))

# Filter the data based on the selected population range
filtered_data = world_population_data[(world_population_data['Population2023'] >= population_slider[0]) & (world_population_data['Population2023'] <= population_slider[1])]

# Create a folium map
m = folium.Map(location=[0, 0], zoom_start=2)

# Add markers for each country
for _, row in filtered_data.iterrows():
    folium.Marker([row['Latitude'], row['Longitude']], popup=f"{row['Country']} - {row['Population2023']}").add_to(m)

# Display the map in the Streamlit app
st.markdown(m._repr_html_(), unsafe_allow_html=True)
