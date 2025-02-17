import streamlit as st
import pandas as pd
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('nfl_combine.db')

# Load data
df = pd.read_sql("SELECT * FROM combine_results", conn)
conn.close()

# Streamlit App Layout
st.title("🏈 NFL Combine Dashboard")
st.write("Visualizing the performance metrics of NFL Combine athletes.")

# Filters
positions = df['pos'].unique()
selected_position = st.selectbox("Select Position", positions)
filtered_df = df[df['pos'] == selected_position]

# Display Data
st.dataframe(filtered_df)

# Charts
st.subheader("Performance Metrics")
st.bar_chart(filtered_df[['40yd', 'bench', 'vertical', 'broad_jump']])

# Fastest Players
st.subheader("Top 10 Fastest Players")
st.table(df[['player', 'pos', '40yd']].sort_values(by='40yd').head(10))

# Strongest Players
st.subheader("Top 10 Strongest Players (Bench Press)")
st.table(df[['player', 'pos', 'bench']].sort_values(by='bench', ascending=False).head(10))

