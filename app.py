import pandas as pd
import streamlit as st
import plotly.express as px


# run this code type in terminal ( streamlit run app.py )

# Set the title of the Streamlit app
st.title('Sales Data Dashboard')

# Read the CSV file into a DataFrame
df = pd.read_csv("C:\\Users\\Mega Computers\\Desktop\\nw plot\\sales_data.csv")

# Create a Streamlit sidebar with a selectbox for Store Location
selected_location = st.sidebar.selectbox('Select Store Location', df['Store Location'].unique())

# Filter the DataFrame based on the selected Store Location
filtered_df = df[df['Store Location'] == selected_location]

# Display the filtered DataFrame in Streamlit
st.write(filtered_df)

# Create pie chart using Plotly Express
st.subheader('Pie Chart \n Product Id mentioned in coloures')
fig_pie = px.pie(filtered_df, names='Product Id')
st.plotly_chart(fig_pie)

# Create line chart using Plotly Express
st.subheader('Line Chart')
fig_line = px.line(filtered_df, x='Date', y='Sale')
st.plotly_chart(fig_line)

# Create histogram chart using Plotly Express
st.subheader('Histogram')
fig_hist = px.histogram(filtered_df, x='Sale Price')
st.plotly_chart(fig_hist)

# Create bar chart using Plotly Express
st.subheader('Bar Chart')
fig_bar = px.bar(filtered_df, x='Product Id', y='Price Sold')
st.plotly_chart(fig_bar)




