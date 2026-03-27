import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("literacy.csv")

# Actual column name
col = "adult_literacy_rate__population_15plus_years__both_sexes__pct__lr_ag15t99"

# Convert to numeric
df[col] = pd.to_numeric(df[col], errors='coerce')

# Drop missing values
df = df.dropna(subset=[col])

# Get Top 10 countries
top_countries = (
    df.groupby('entity')[col]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .index
)

# Filter data
filtered_df = df[df['entity'].isin(top_countries)]

# Streamlit title
st.title("📊 Literacy Rate Dashboard")

# Plot
fig, ax = plt.subplots(figsize=(10,6))

for country in top_countries:
    country_data = filtered_df[filtered_df['entity'] == country]
    ax.plot(country_data['year'], country_data[col], label=country)

ax.set_xlabel("Year")
ax.set_ylabel("Literacy Rate (%)")
ax.set_title("Top 10 Countries Literacy Trend")
ax.legend()

st.pyplot(fig)