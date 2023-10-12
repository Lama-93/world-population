import streamlit as st
import pandas as pd

# Load the dataset from GitHub
@st.cache
def load_data():
    #url = 'https://raw.githubusercontent.com/your-username/your-repository/main/WorldPopulation2023.csv'
    data = pd.read_csv('/Users/lamaissa/Desktop/AUB/Fall 2023/Data Visualization & Communication MSBA325/Assignment 2 Streamlit with pltly Visuals')
    return data

# Load the data
data = load_data()

# Set the title and introductory text for your app
st.title("Interactive World Population Data for 2023")
st.write("Explore and filter world population data for the year 2023.")

# Create a sidebar with filters
st.sidebar.header("Filter Data")

# Filter by Country
selected_country = st.sidebar.selectbox("Select a Country:", data["Country"].unique())

# Filter by Columns
selected_column = st.sidebar.selectbox("Select a Column:", data.columns)

# Filter the data based on user selections
filtered_data = data[data["Country"] == selected_country]

# Display the filtered data
st.write(f"Population data for {selected_country} based on {selected_column}:")
st.write(filtered_data[[selected_column]])

# Optionally, display a plot or visualization based on the filtered data
# Example: You can use Plotly, Matplotlib, or other libraries for data visualization here
# Make sure to add interactivity to the visualization as needed

# Additional interactivity can be added as required
# For example, add more widgets or filters based on your dataset columns
# Create a bar chart based on the filtered data
st.subheader("Visualization of Filtered Data")
fig = px.bar(filtered_data, x="Country", y=selected_column, title=f"{selected_column} for {selected_country}")
st.plotly_chart(fig)
