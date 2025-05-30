# Customer Segmentation and Purchase Patterns in Online Retail

This project analyzes real-world transaction data from a UK-based online retailer. The main goal is to uncover customer purchasing behaviors, segment customers based on their value and frequency, and extract actionable insights using visual analytics and machine learning.

## Objectives
- Perform RFM (Recency, Frequency, Monetary) analysis to profile customer behavior
- Segment customers using clustering (K-Means)
- Explore trends in purchases, returns, and top-selling products
- Create visual storytelling through charts and dashboards
- Strengthen skills in data cleaning, statistics, and exploratory analysis

## Tools & Technologies
- Python  
- pandas, numpy  
- seaborn, matplotlib, plotly  
- scikit-learn (K-Means)  
- Streamlit (for dashboard)  
- Jupyter Notebook
- Git & GitHub

## Dataset
**Name:** Online Retail  
**Source:** UCI Machine Learning Repository  
[Dataset Link](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

## Notes on Clustering
The primary clustering method applied in this project is **K-Means**, chosen for its balance between performance and interpretability.  
Due to the size and structure of the dataset, **DBSCAN** was considered but not fully implemented, as it introduced significant computational overhead without clear added value in this context.  
An optional commented-out cell in the notebook includes the initial setup for DBSCAN, should future users want to experiment with density-based clustering approaches.

---

This project is part of a portfolio to demonstrate analytical thinking, real-world data handling, and business-oriented data science practices.
