import streamlit as st
import pandas as pd
import streamlit as st

# 1 Set the title and introductory text for your app
st.title("Interactive Data Visualizations with World Population for year 2023")
st.write("Explore an interactive bar chart with population data.")

# Load and display the HTML visualization
with open('/Users/lamaissa/Downloads/interactive_bar_chart.html', 'r', encoding='utf-8') as f:
    html = f.read()
st.components.v1.html(html, width=800, height=600)  # Adjust width and height as needed


# 2 Set the title and introductory text for your app
st.write("Explore an interactive scatter plot with population data.")

# Load and display the HTML visualization
with open('/Users/lamaissa/Downloads/3d_scatter_plot5.html', 'r', encoding='utf-8') as f:
    html = f.read()
st.components.v1.html(html, width=800, height=600)  # Adjust width and height as needed


# 3 Set the title and introductory text for your app
st.write("Explore an interactive World map with population data.")

# Load and display the HTML visualization
with open('/Users/lamaissa/Downloads/interactive_choropleth_map.html', 'r', encoding='utf-8') as f:
    html = f.read()
st.components.v1.html(html, width=800, height=600)  # Adjust width and height as needed



# 4 Set the title and introductory text for your app
st.write("Explore an interactive Jupiter table with population data.")

# Load and display the HTML visualization
with open('/Users/lamaissa/Downloads/jupyter-table1.html', 'r', encoding='utf-8') as f:
    html = f.read()
st.components.v1.html(html, width=800, height=600)  # Adjust width and height as n
