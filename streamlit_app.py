import streamlit as st
import pandas as pd
import plotly.express as px

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

# Sidebar filters
selected_metrics = st.sidebar.multiselect("Select Metrics", data.columns)

# Filter the data based on user selection
filtered_data = data[selected_metrics]

# Display a bar chart using Plotly Express
st.write("## Bar Chart")
fig_bar = px.bar(filtered_data, x="Country", y="Population2023", title="Population by Country")
st.plotly_chart(fig_bar)

# Display a scatter plot using Plotly Express
st.write("## Scatter Plot")
fig_scatter = px.scatter(filtered_data, x="Fert.Rate", y="MedianAge", color="UrbanPop%", size="WorldShare", hover_name="Density", title="Fertility Rate vs. Median Age")
st.plotly_chart(fig_scatter)
