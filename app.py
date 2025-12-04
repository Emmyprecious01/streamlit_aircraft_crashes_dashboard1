import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit page config
st.set_page_config(page_title="Aircraft Crashes Analysis", layout="wide", page_icon="✈️")
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: black;
        color: white;
    }
    .st-bf {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load dataset
df = pd.read_csv(r"C:\Users\USER\Desktop\PYTHON PROJECT\aircrahesFullDataUpdated_2024.csv")

# Data Cleaning
df.columns = df.columns.str.strip()
df["Country/Region"] = df["Country/Region"].fillna("Unknown")

# Set Seaborn style for dark background
sns.set_style("darkgrid")
plt.style.use('dark_background')

st.title("Aircraft Crashes Analysis (Charts Only)")

# Total crashes per year
st.subheader("Aircraft Crashes per Year")
crashes_per_year = df["Year"].value_counts().sort_index()
fig1, ax1 = plt.subplots(figsize=(12,6))
crashes_per_year.plot(kind='line', marker='o', ax=ax1)
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Crashes")
st.pyplot(fig1)

# Top 10 countries with most crashes
st.subheader("Top 10 Countries by Number of Aircraft Crashes")
top_countries = df["Country/Region"].value_counts().head(10)
fig2, ax2 = plt.subplots(figsize=(10,5))
sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    hue=top_countries.index,
    legend=False,
    palette="coolwarm",
    ax=ax2
)
st.pyplot(fig2)

# Fatality Analysis
st.subheader("Distribution of Air Fatalities per Crash")
fig3, ax3 = plt.subplots(figsize=(8,5))
sns.histplot(df["Fatalities (air)"], bins=30, kde=True, ax=ax3, color="red")
st.pyplot(fig3)

# Correlation Check
st.subheader("Correlation Heatmap")
fig4, ax4 = plt.subplots(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="Blues", ax=ax4)
st.pyplot(fig4)

# Top 10 aircraft manufacturers by crashes
st.subheader("Top 10 Aircraft Manufacturers by Number of Crashes")
top_manufacturers = df["Aircraft Manufacturer"].value_counts().head(10)
fig5, ax5 = plt.subplots(figsize=(10,5))
sns.barplot(
    x=top_manufacturers.values,
    y=top_manufacturers.index,
    hue=top_manufacturers.index,
    palette="viridis",
    legend=False,
    ax=ax5
)
st.pyplot(fig5)

# Aboard vs Fatalities scatter
st.subheader("Fatalities vs People Aboard")
fig6, ax6 = plt.subplots(figsize=(6,4))
sns.scatterplot(data=df, x="Aboard", y="Fatalities (air)", alpha=0.5, ax=ax6)
st.pyplot(fig6)

# Survival Rate
df["Survival Rate"] = ((df["Aboard"] - df["Fatalities (air)"]) / df["Aboard"]) * 100
fig7, ax7 = plt.subplots(figsize=(8,5))
sns.histplot(df["Survival Rate"], bins=20, color='green', ax=ax7)
st.subheader("Distribution of Survival Rates per Crash")
st.pyplot(fig7)

# Crashes by Month
st.subheader("Crashes by Month")
crashes_by_month = df["Month"].value_counts()
fig8, ax8 = plt.subplots(figsize=(10,5))
sns.barplot(x=crashes_by_month.index, y=crashes_by_month.values, palette="coolwarm", ax=ax8)
ax8.set_xlabel("Month")
ax8.set_ylabel("Number of Crashes")
st.pyplot(fig8)

# Trend of crashes over decades
st.subheader("Aircraft Crashes per Decade")
df["Decade"] = (df["Year"] // 10) * 10
crashes_per_decade = df["Decade"].value_counts().sort_index()
fig9, ax9 = plt.subplots(figsize=(10,6))
crashes_per_decade.plot(kind='bar', color='skyblue', ax=ax9)
ax9.set_xlabel("Decade")
ax9.set_ylabel("Number of Crashes")
st.pyplot(fig9)

# Top 10 Deadliest Crashes
st.subheader("Top 10 Deadliest Crashes")
deadliest = df.sort_values(by="Fatalities (air)", ascending=False).head(10)
st.dataframe(deadliest[["Year", "Aircraft", "Operator", "Location", "Fatalities (air)"]])
