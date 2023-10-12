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

# Create a multi-select widget to select multiple countries
selected_countries = st.sidebar.multiselect("Select Countries for Comparison", data["Country"].unique())

# Add a button to download the dataset
if st.sidebar.button("Download Dataset"):
    st.markdown(get_table_download_link(data), unsafe_allow_html=True)

# Display a title and description for the bar chart
st.markdown("## Population Comparison")
st.markdown("This bar chart shows the population of the selected countries for comparison.")
# Filter the data based on the selected countries
filtered_data = data[data["Country"].isin(selected_countries)]

# Display a bar chart for the selected countries' population
if not filtered_data.empty:
    fig_bar = px.bar(filtered_data, x="Country", y="Population2023", title="Population Comparison")
    st.plotly_chart(fig_bar)
else:
    st.write("No data selected. Please choose one or more countries for comparison.")

# Get unique median age values from the dataset
median_age_values = np.sort(data["MedianAge"].unique())

# Create a slider for selecting median age
selected_median_age = st.slider("Select Median Age", min_value=int(min(median_age_values)), max_value=int(max(median_age_values)), value=int(min(median_age_values))

# Display a title and description for the choropleth map
st.write("## Median Age Choropleth Map")
st.write("This choropleth map displays the median age of countries with colors indicating the median age.")
# Round the selected median age to the nearest integer
selected_median_age = int(selected_median_age)

# Filter the data based on the selected median age
filtered_data = data[data["MedianAge"] == selected_median_age]

# Display a choropleth map with median age data
fig_map = px.choropleth(
    filtered_data,
    locations="Country",
    locationmode="country names",
    color="MedianAge",
    title=f"World Population Median Age in {selected_median_age}",
    hover_name="Country",
    color_continuous_scale=px.colors.sequential.Plasma
)

fig_map.update_geos(
    showcoastlines=True,
    coastlinecolor="Black"
)

st.plotly_chart(fig_map)

# Function to create a downloadable link for the dataset
def get_table_download_link(data):
    csv = data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="world_population_data.csv">Download Dataset</a>'
    return href
