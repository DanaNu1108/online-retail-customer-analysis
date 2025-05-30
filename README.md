# Customer Segmentation and Purchase Patterns in Online Retail

This project analyzes real-world transaction data from a UK-based online retailer. The goal is to uncover purchasing behaviors, segment customers based on RFM metrics, and generate business insights through machine learning and interactive visualizations.

## Objectives

- Perform RFM (Recency, Frequency, Monetary) analysis to profile customer behavior.
- Apply unsupervised machine learning (K-Means clustering) to segment customers.
- Explore trends in purchases, returns, and top-selling products.
- Create an interactive dashboard using Streamlit.
- Strengthen data cleaning, exploratory analysis, and statistical thinking.

## Tools & Technologies

- Python
- pandas, numpy
- seaborn, matplotlib, plotly
- scikit-learn (K-Means)
- Streamlit
- Jupyter Notebook
- Git & GitHub

## Dataset

- **Name**: Online Retail  
- **Source**: UCI Machine Learning Repository  
- [View Dataset](https://archive.ics.uci.edu/ml/datasets/Online+Retail)

## Clustering Notes

The main clustering method used is K-Means, selected for its balance between performance and interpretability.  
DBSCAN was considered but not implemented due to its computational cost on this dataset and the limited improvement in clustering outcomes.  
The notebook includes a commented section with DBSCAN setup for optional experimentation.

## Project Components

- Full analysis in Jupyter Notebook (`notebooks/online_retail_analysis.ipynb`)
- Dashboard interface built with Streamlit (`streamlit_app/main.py`)
- Exported data files and artifacts for reproducibility

## Portfolio and Presentation

This project is part of my data science portfolio. For an overview, additional insights, and visual structure, please refer to the project page on Notion:

[View on Notion](https://www.notion.so/your-notion-link-here)
