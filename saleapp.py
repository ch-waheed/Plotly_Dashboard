# # Create a bar chart showing total sales per store location
# bar_fig = px.bar(df, x="Store Location", y="Sale", color="Store Location", hover_data=["Sale Price", "Price Sold"])
# bar_fig.update_layout(title="Total Sales per Store Location",
#                       xaxis_title="Store Location",
#                       yaxis_title="Total Sale",
#                       showlegend=False)


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\Mega Computers\\Desktop\\nw plot\\sales_data.csv")

# Clean the data
# You can perform data cleaning operations based on your specific requirements.
# Here's an example of dropping duplicate rows and handling missing values.
df = df.drop_duplicates()  # Drop duplicate rows
df = df.dropna()  # Drop rows with missing values

# Create the Streamlit dashboard
st.title("Sales Data Dashboard")

# Display the cleaned dataset
st.subheader("Cleaned Dataset")
st.dataframe(df)

# Perform data analysis and visualization
# Here's an example of using Plotly Express to create a bar chart of sales by store location.
sales_by_location = df.groupby("Store Location")["Sale"].sum().reset_index()
fig = px.bar(sales_by_location, x="Store Location", y="Sale", title="Total Sales by Store Location")
st.plotly_chart(fig)

# Create interactive components
# Here's an example of adding a selectbox to filter the data by product ID.
product_ids = df["Product ID"].unique()
selected_product_id = st.selectbox("Select Product ID", product_ids)

filtered_df = df[df["Product ID"] == selected_product_id]
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Add additional visualizations or components based on your requirements.

