import streamlit as st
import pandas as pd

# Load the dataset from GitHub
@st.cache
def load_data():
    url = 'https://raw.githubusercontent.com/Lama-93/world-population/main/WorldPopulation2023.csv'
    data = pd.read_csv(url)
    return data

# Load the data
data = load_data()

# Set the title and introductory text for your app
st.title("Interactive World Population Data for 2023")
st.write("Explore and filter world population data for the year 2023.")

# Create a sidebar with filters
st.sidebar.header("Filter Data")

# Sort Option
sort_by_population = st.sidebar.checkbox("Sort by Population")

# Filter by Country
selected_country = st.sidebar.selectbox("Select a Country:", data["Country"].unique())

# Filter by Columns
selected_column = st.sidebar.selectbox("Select a Column:", data.columns)

# Filter and Sort the data based on user selections
if sort_by_population:
    filtered_data = data.sort_values(by="Population2023", ascending=False)
else:
    filtered_data = data

filtered_data = filtered_data[filtered_data["Country"] == selected_country]

# Display the filtered data
st.write(f"Population data for {selected_country} based on {selected_column}:")
st.write(filtered_data[[selected_column]])

# Create a bar chart based on the filtered data
st.subheader("Visualization of Filtered Data")
fig = px.bar(filtered_data, x="Country", y=selected_column, title=f"{selected_column} for {selected_country}")
st.plotly_chart(fig)
