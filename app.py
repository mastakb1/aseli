import streamlit as st
import pandas as pd
import plotly.express as px
from awDb import get_db_data

# Retrieve data from database
count_customer = get_db_data("""
    SELECT dg.City, COUNT(dc.CustomerKey) AS CustomerCount
    FROM dimcustomer dc
    JOIN dimgeography dg ON dc.GeographyKey = dg.GeographyKey
    GROUP BY dg.City
""")

# Check if data retrieval is successful (optional)
if count_customer is None:
    st.error("Failed to retrieve data from the database.")
else:
    # Create a line chart using Plotly Express
    st.header('Line Chart of Customer Count per City')
    line_fig = px.line(count_customer, x='City', y='CustomerCount', title='Customer Count per City')
    st.plotly_chart(line_fig)

    # Additional description
    st.write("This line chart shows the number of customers per city. It helps visualize the distribution of customers across different cities.")
