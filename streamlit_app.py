import streamlit as st
import pandas as pd
import streamlit as st

import streamlit as st

# Set the title and introductory text for your app
st.title("Interactive Data Visualizations")
st.write("Explore two related visualizations with interactive features.")

# Create a dropdown to select a visualization
selected_visualization = st.selectbox("Select a Visualization", ["Visualization 1", "Visualization 2"])

# Define the HTML files for the visualizations
visualization_files = {
    "Visualization 1": "visualization1.html",
    "Visualization 2": "visualization2.html"
}

# Load and display the selected HTML visualization
if selected_visualization in visualization_files:
    with open(visualization_files[selected_visualization], "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, width=800, height=600)  # Adjust width and height as needed

# Optional: Add interactive elements specific to each visualization, such as filters or controls

# Example: If you have filters for Visualization 1
if selected_visualization == "Visualization 1":
    selected_category = st.selectbox("Select a Category:", ["Category 1", "Category 2", "Category 3"])
    # Add code to update Visualization 1 based on the selected category

# Example: If you have filters for Visualization 2
if selected_visualization == "Visualization 2":
    selected_data_type = st.selectbox("Select Data Type:", ["Data Type A", "Data Type B"])
    # Add code to update Visualization 2 based on the selected data type
