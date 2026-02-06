import streamlit as st

st.set_page_config(page_title="SERIS", page_icon="📊", layout="wide")

st.markdown("""
# 📊 Smart Employee Retention Intelligence System (SERIS)

Welcome! This system helps HR teams:

- 📤 Upload and manage employee datasets
- 📊 Visualize workforce and attrition trends
- 🤖 Predict attrition risk using Machine Learning
- 🧠 Get AI explanations & recommendations (Groq)
- 📄 Generate PDF reports for management

👉 Use the **left sidebar** to navigate between pages:
- **Upload**: Upload, view history, load or delete datasets  
- **Dashboard**: Visual analytics  
- **Predictions**: Risk scores & high-risk employees  
- **AI Insights**: Per-employee AI explanation & recommendations  
- **Reports**: Download PDF reports  

Start by going to **📤 Upload** page.
""")
