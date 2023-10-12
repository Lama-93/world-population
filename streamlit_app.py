import streamlit as st
import pandas as pd
import plotly.express as px

# Load your world population dataset for 2023
# Replace 'world_population_2023.csv' with your dataset file
data = pd.read_csv('world_population_2023.csv')

# Create a Streamlit app
st.title('World Population 2023 Data Visualization')

# Add a slider for selecting the population
population_slider = st.slider('Select Population Range', min_value=0, max_value=data['population'].max(), value=(0, data['population'].max()))

# Filter the data based on the selected population range
filtered_data = data[(data['population'] >= population_slider[0]) & (data['population'] <= population_slider[1])]

# Display a table with the filtered data
st.write("Filtered Data:")
st.write(filtered_data)

# Create a scatter plot using Plotly Express
fig = px.scatter(filtered_data, x='country', y='population', title='World Population 2023')
st.plotly_chart(fig)
