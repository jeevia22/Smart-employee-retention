Smart Employee Retention Intelligence System (SERIS)

Overview :

- SERIS is an AI-powered HR analytics web application for analyzing and predicting employee attrition.

- It combines machine learning, data visualization, and generative AI to support proactive retention strategies.

- The system enables HR teams to upload datasets, analyze workforce trends, predict attrition risk, generate AI insights, and download PDF reports.
  

Key Features :

- Upload and manage employee CSV datasets
  
- Maintain dataset history with load and delete options

- Interactive dashboard for workforce and attrition analysis

- Machine learning-based attrition risk prediction using Logistic Regression

- AI-generated explanations and recommendations using Groq LLM

- Automatic PDF report generation for high-risk employees

- Multi-page, user-friendly Streamlit interface

- Deployed on Streamlit Cloud for live access
  

Problem Statement :

- Traditional HR systems rely on static, historical reports, leading to reactive decision-making.

There is a need to:

- Predict attrition risk in advance

- Explain why an employee is at risk

- Provide actionable recommendations

- Present insights in a simple and visual manner

- SERIS addresses this by integrating predictive analytics, explainable AI, dashboards, and reporting into a single platform.
  

Machine Learning Approach :

- Algorithm: Logistic Regression

- Type: Binary Classification (Attrition: Yes / No)

Features used:

- Age

- Monthly Income

- Job Level

- Years at Company

- OverTime

Output:

- Risk score (probability)

- Classification into High Risk or Low Risk

- Logistic Regression is used because it is simple, fast, and interpretable for HR analytics.

AI Insights

- High-risk employees are analyzed using the Groq LLM API.

The system generates:

- Human-readable explanations

- Actionable HR recommendations

- This converts model predictions into business-friendly decision support.

Dashboard and Visualization :

Provides visual analysis of:

- Attrition distribution

- Income vs attrition

- Overtime impact on attrition

- Feature correlation

- Helps HR teams understand patterns and validate predictions using data.
  

PDF Report Generation :

- Generates a professional PDF report containing:

- List of high-risk employees

- Risk scores

- AI-generated insights and recommendations

- Useful for management review, documentation, and strategic planning.
  

System Workflow :

- HR uploads employee CSV dataset

- System validates and preprocesses data

- ML model is trained using historical data

- Risk scores are generated for employees

- High-risk employees are identified

- AI generates explanations and recommendations

- Dashboard displays insights

- PDF report can be generated and downloaded
  

Technology Stack :

- Frontend/UI: Streamlit

- Backend Logic: Python

- Machine Learning: Scikit-learn (Logistic Regression)

- Data Processing: Pandas, NumPy

- Visualization: Matplotlib, Seaborn

- AI: Groq LLM API

- Reporting: FPDF

- Deployment: Streamlit Cloud and GitHub


Deployment :

- Deployed on Streamlit Cloud using GitHub integration.

- API keys and secrets are managed using Streamlit secrets manager.
  

Future Enhancements :

- Use advanced models such as Random Forest or XGBoost

- Add more HR features like Job Satisfaction and Performance Rating

- Support prediction on new employee data without Attrition column

- Add role-based access for HR and managers

- Integrate explainability tools such as SHAP or LIME
  

Conclusion :

- SERIS is an end-to-end AI-driven HR decision support system.

- It combines predictive analytics, explainable AI, visual analytics, and reporting.

- The system helps organizations move from reactive analysis to proactive employee retention strategies.

