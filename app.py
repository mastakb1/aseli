import streamlit as st
import pandas as pd
import plotly.express as px
from awDb import get_db_data

count_customer = get_db_data("""
SELECT dg.City, COUNT(dc.CustomerID) AS CustomerCount
FROM dimcustomer dc
JOIN dimgeography dg ON dc.GeographyKey = dg.GeographyKey
GROUP BY dg.City;
""")

st.header('Line Chart of Customer Count per City')
line_fig = px.line(customer_data_df, x='City', y='CustomerCount', title='Customer Count per City')
st.plotly_chart(line_fig)
