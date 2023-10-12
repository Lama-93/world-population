import streamlit as st
import pandas as pd
import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the world population data
data = pd.read_csv("WorldPopulation2023.csv")

# Set the title and introductory text for your app
st.title("World Population Visualization for 2023")
st.write("Explore the population of different continents for the year 2023.")

# Add an explanation
st.write("This visualization displays the population of continents based on the data for the year 2023.")

# Create a dropdown to select a continent
selected_continent = st.selectbox("Select a Continent:", data["Country"].unique())

# Filter the data based on the selected continent
filtered_data = data[data["Country"] == selected_continent]

# Create a bar chart
fig = px.bar(filtered_data, x="YearlyChange", y="Population2023", title=f"Population of {selected_continent} in 2023")
fig.update_xaxes(title="Yearly Change")
fig.update_yaxes(title="Population 2023")

# Display the bar chart
st.plotly_chart(fig)

