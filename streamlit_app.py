import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Load your "WorldPopulation2023" dataset
world_population_data = pd.read_csv('WorldPopulation2023.csv')

# Create a Streamlit app
st.title('World Population 2023 Visualization')

# Add a slider for selecting the population range
population_slider = st.slider('Select Population Range', min_value=0, max_value=world_population_data['Population2023'].max(), value=(0, world_population_data['Population2023'].max()))

# Filter the data based on the selected population range
filtered_data = world_population_data[(world_population_data['Population2023'] >= population_slider[0]) & (world_population_data['Population2023'] <= population_slider[1])]

# Create a bar chart with Matplotlib
fig, ax = plt.subplots()
ax.bar(filtered_data['Country'], filtered_data['Population2023'])
ax.set_xlabel('Country')
ax.set_ylabel('Population 2023')
ax.set_title('Population of Countries in 2023')
plt.xticks(rotation=90)  # Rotate country names for better readability

# Display the chart in the Streamlit app
st.pyplot(fig)
