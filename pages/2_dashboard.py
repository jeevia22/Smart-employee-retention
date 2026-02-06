import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from utils.preprocessing import validate_dataset, preprocess_data
from utils.model import train_model, predict_risk

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")
st.title("📊 HR Analytics Dashboard")

if "active_dataset" not in st.session_state:
    st.warning("Please upload or load a dataset from the Upload page.")
    st.stop()

df = pd.read_csv(st.session_state["active_dataset"])

is_valid, missing = validate_dataset(df)
if not is_valid:
    st.error(f"Missing columns: {missing}")
    st.stop()

X, y, processed = preprocess_data(df)
model, _ = train_model(X, y)
risk_scores = predict_risk(model, X)

result_df = df.copy()
result_df["Risk_Score"] = risk_scores
result_df["Risk_Label"] = result_df["Risk_Score"].apply(lambda x: "High" if x >= 0.5 else "Low")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Risk Distribution")
    fig1, ax1 = plt.subplots()
    sns.countplot(x="Risk_Label", data=result_df, ax=ax1)
    st.pyplot(fig1)
    plt.close(fig1)

    st.subheader("OverTime vs Risk")
    fig2, ax2 = plt.subplots()
    sns.countplot(x="OverTime", hue="Risk_Label", data=result_df, ax=ax2)
    st.pyplot(fig2)
    plt.close(fig2)

with col2:
    st.subheader("Monthly Income vs Risk")
    fig3, ax3 = plt.subplots()
    sns.boxplot(x="Risk_Label", y="MonthlyIncome", data=result_df, ax=ax3)
    st.pyplot(fig3)
    plt.close(fig3)

    st.subheader("Correlation Heatmap")
    fig4, ax4 = plt.subplots(figsize=(6,4))
    sns.heatmap(processed.corr(), annot=True, cmap="coolwarm", ax=ax4)
    st.pyplot(fig4)
    plt.close(fig4)
