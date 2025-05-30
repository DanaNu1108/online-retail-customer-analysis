import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page config
st.set_page_config(page_title="Customer Segmentation Dashboard", layout="wide")

# Title and intro
st.title("🛍️ Customer Segmentation Dashboard")
st.markdown("Explore customer segments based on RFM analysis from the Online Retail dataset.")

# Load data
def load_data():
    df = pd.read_csv("rfm_clusters.csv")
    df['Cluster'] = df['Cluster'].astype(str)  # Ensure cluster is treated as categorical
    return df

rfm = load_data()

# Create tabs for better organization
tab1, tab2, tab3 = st.tabs([
    "📦 Cluster Distribution",
    "📊 RFM Scatter Plots",
    "📈 Interactive Scatter Matrix"
])

# --- Tab 1: Barplot ---
with tab1:
    st.subheader("Customer Distribution by Cluster")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=rfm, x='Cluster', palette='Set2', ax=ax)
    st.pyplot(fig)

# --- Tab 2: Plotly RFM scatterplots ---
with tab2:
    st.subheader("Recency vs Monetary")
    fig1 = px.scatter(
        rfm,
        x='Recency',
        y='Monetary',
        color='Cluster',
        hover_data=['CustomerID', 'Frequency'],
        title='Customer Segments: Recency vs Monetary',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.subheader("Recency vs Frequency")
    fig2 = px.scatter(
        rfm,
        x='Recency',
        y='Frequency',
        color='Cluster',
        hover_data=['CustomerID', 'Monetary'],
        title='Customer Segments: Recency vs Frequency',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Frequency vs Monetary")
    fig3 = px.scatter(
        rfm,
        x='Frequency',
        y='Monetary',
        color='Cluster',
        hover_data=['CustomerID', 'Recency'],
        title='Customer Segments: Frequency vs Monetary',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig3, use_container_width=True)

# --- Tab 3: Interactive scatter matrix (optional preview) ---
with tab3:
    st.subheader("📈 Scatter Matrix (All RFM variables)")
    fig_matrix = px.scatter_matrix(
        rfm,
        dimensions=['Recency', 'Frequency', 'Monetary'],
        color='Cluster',
        title="RFM Feature Relationships by Cluster",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig_matrix, use_container_width=True)

# Cluster summary table (inside an expander for clarity)
with st.expander("📋 Cluster Summary Table", expanded=True):
    st.subheader("Average RFM Values by Cluster")

    # Group by cluster and calculate average RFM and customer count
    summary = rfm.groupby('Cluster').agg({
        'Recency': 'mean',
        'Frequency': 'mean',
        'Monetary': 'mean',
        'CustomerID': 'count'
    }).rename(columns={'CustomerID': 'Customer Count'})

    # Round for cleaner display
    summary = summary.round(1).reset_index()

    # Display the dataframe
    st.dataframe(summary, use_container_width=True)

st.markdown("---")
st.header("📊 Exploratory Data Analysis & Demographics")
st.markdown("Explore the most popular and high-value products, as well as the countries contributing to revenue.")

# 1. Top 10 Most Sold Products
st.subheader("🛒 Top 10 Most Sold Products")
top_products = rfm.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
fig1 = px.bar(top_products, x=top_products.values, y=top_products.index, orientation='h',
              labels={'x': 'Quantity Sold', 'index': 'Product Description'},
              title='Top 10 Products by Quantity Sold')
st.plotly_chart(fig1, use_container_width=True)

# 2. Top 10 Revenue Generating Products
st.subheader("💰 Top 10 Products by Revenue")
rfm['TotalRevenue'] = rfm['Quantity'] * rfm['UnitPrice']
top_revenue = rfm.groupby('Description')['TotalRevenue'].sum().sort_values(ascending=False).head(10)
fig2 = px.bar(top_revenue, x=top_revenue.values, y=top_revenue.index, orientation='h',
              labels={'x': 'Total Revenue (£)', 'index': 'Product Description'},
              title='Top 10 Products by Total Revenue')
st.plotly_chart(fig2, use_container_width=True)

# 3. Sales by Country (Top 10 excluding UK)
st.subheader("🌍 Top Countries by Revenue (excluding UK)")
country_revenue = rfm[rfm['Country'] != 'United Kingdom'].groupby('Country')['TotalRevenue'].sum().sort_values(ascending=False).head(10)
fig3 = px.bar(country_revenue, x=country_revenue.values, y=country_revenue.index, orientation='h',
              labels={'x': 'Total Revenue (£)', 'index': 'Country'},
              title='Top 10 Countries by Revenue')
st.plotly_chart(fig3, use_container_width=True)

