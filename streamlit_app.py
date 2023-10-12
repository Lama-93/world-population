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
min_population = st.slider("Minimum Population", int(data["Population2023"].min()), int(data["Population2023"].max()), int(data["Population2023"].min()))
max_population = st.slider("Maximum Population", min_population, int(data["Population2023"].max()), int(data["Population2023"].max()))

# Filter the data based on the selected population range
filtered_data = data[(data["Population2023"] >= min_population) & (data["Population2023"] <= max_population)]

# Create a bar chart based on the filtered data
st.subheader("Population by Country")
fig = px.bar(
    filtered_data,
    x="Country",
    y="Population2023",
    title=f"Population by Country in 2023",
    labels={'Population2023': 'Population'},
)

fig.update_xaxes(title_text="Country")
fig.update_yaxes(title_text="Population")

# Display the bar chart
st.plotly_chart(fig)
