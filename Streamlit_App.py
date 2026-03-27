import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Global Literacy & Education Trends")

# Load data
df_literacy = pd.read_csv("literacy.csv")
df_gdp = pd.read_csv("gdp.csv")

# Sidebar
option = st.sidebar.selectbox("Select View", ["Dataset", "EDA", "Insights"])

# -----------------------
# 1️⃣ Dataset View
# -----------------------
if option == "Dataset":
    st.subheader("Literacy Dataset")
    st.dataframe(df_literacy.head(50))

# -----------------------
# 2️⃣ EDA View
# -----------------------
elif option == "EDA":
    st.subheader("Adult Literacy Trend (Top Countries)")

    # Convert numeric
    col = df_literacy.columns[3]
    df_literacy[col] = pd.to_numeric(df_literacy[col], errors='coerce')

    # Top countries
    top_countries = df_literacy.groupby('entity')[col].mean().sort_values(ascending=False).head(5).index

    fig, ax = plt.subplots()
    for country in top_countries:
        temp = df_literacy[df_literacy['entity'] == country]
        ax.plot(temp['year'], temp[col], label=country)

    ax.set_title("Adult Literacy Trend")
    ax.legend()
    st.pyplot(fig)

# -----------------------
# 3️⃣ Insights
# -----------------------
elif option == "Insights":
    st.subheader("Project Insights")

    st.write("""
    - Countries with higher GDP tend to have higher literacy rates.
    - Youth literacy is generally higher than adult literacy.
    - Gender gap in literacy is reducing in many countries.
    """)