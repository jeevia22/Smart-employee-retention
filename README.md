🧠 Smart Employee Retention Intelligence System (SERIS)

SERIS is an AI-powered HR analytics web application that helps organizations analyze, predict, and understand employee attrition. It combines machine learning, data visualization, and generative AI to support proactive retention strategies.

The system allows HR teams to upload employee datasets, visualize workforce trends, predict attrition risk, generate AI-based explanations and recommendations, and download professional PDF reports for management.

🚀 Features

📤 Upload and manage employee CSV datasets

🗂️ Dataset history with load & delete options

📊 Interactive dashboard for workforce & attrition analysis

🤖 Machine Learning-based attrition risk prediction (Logistic Regression)

🧠 AI-powered explanations & recommendations using Groq LLM

📄 Automatic PDF report generation for high-risk employees

🧭 Multi-page, user-friendly Streamlit interface

☁️ Deployed on Streamlit Cloud for live access

🧩 Problem Statement

Organizations often rely on static, historical reports to understand employee attrition, which leads to reactive decision-making. There is a need for a system that can:

Predict attrition risk in advance

Explain why an employee is at risk

Provide actionable recommendations

Present insights in a simple, visual, and usable way

SERIS addresses this by combining predictive analytics + explainable AI + dashboards + reporting into one platform.

🧠 Machine Learning Approach

Algorithm Used: Logistic Regression

Type: Binary Classification (Attrition: Yes / No)

Features:

Age

Monthly Income

Job Level

Years at Company

OverTime

The model outputs a risk score (probability) and classifies employees into High Risk or Low Risk.

Logistic Regression was chosen because it is simple, fast, and interpretable, which is important for HR analytics.

🧠 AI Insights (Groq LLM)

For employees identified as high risk, SERIS uses the Groq LLM API to generate:

Human-readable explanations of why the employee is at risk

Actionable recommendations for HR to reduce attrition risk

This converts raw ML predictions into business-friendly, decision-support insights.

📊 Dashboard & Visualization

The dashboard provides:

Attrition distribution

Income vs Attrition analysis

Overtime impact on attrition

Feature correlation heatmap

These visuals help HR teams understand patterns and validate predictions using data.

📄 PDF Report Generation

SERIS can generate a professional PDF report containing:

High-risk employees list

Risk scores

AI-generated insights & recommendations

Useful for:

Management review meetings

Documentation

Strategic planning

🏗️ System Workflow

HR uploads employee CSV dataset

System validates and preprocesses data

ML model is trained using historical data

Risk scores are generated for employees

High-risk employees are identified

AI generates explanations & recommendations

Dashboard displays insights

PDF report can be generated and downloaded

🛠️ Tech Stack

Frontend / UI: Streamlit

Backend Logic: Python

Machine Learning: Scikit-learn (Logistic Regression)

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Seaborn

AI: Groq LLM API

Reporting: FPDF

Deployment: Streamlit Cloud + GitHub

⚙️ Installation & Run Locally
git clone https://github.com/your-username/Smart-employee-retention.git
cd Smart-employee-retention
python -m venv venv
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
streamlit run app.py

🌐 Deployment

The application is deployed on Streamlit Cloud using GitHub integration.
Secrets like the Groq API key are managed securely using Streamlit’s secrets manager.

🔮 Future Enhancements

Use advanced models like Random Forest / XGBoost

Add more HR features (Job Satisfaction, Performance Rating, Promotions, etc.)

Support prediction on new employee data without Attrition column

Add role-based access for HR and managers

Integrate explainability tools like SHAP or LIME

✅ Conclusion

SERIS is an end-to-end AI-driven HR decision support system that combines:

Predictive analytics (ML)

Explainable insights (AI)

Visual analytics (Dashboards)

Decision support (PDF reports)

It helps organizations move from reactive analysis to proactive employee retention strategies.
