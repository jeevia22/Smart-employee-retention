import streamlit as st
import pandas as pd

from utils.preprocessing import validate_dataset, preprocess_data
from utils.model import train_model, predict_risk

st.set_page_config(page_title="Predictions", page_icon="🤖", layout="wide")
st.title("🤖 Attrition Risk Predictions")

if "active_dataset" not in st.session_state:
    st.warning("Please upload or load a dataset from the Upload page.")
    st.stop()

df = pd.read_csv(st.session_state["active_dataset"])

is_valid, missing = validate_dataset(df)
if not is_valid:
    st.error(f"Missing columns: {missing}")
    st.stop()

X, y, _ = preprocess_data(df)
model, acc = train_model(X, y)
risk_scores = predict_risk(model, X)

result_df = df.copy()
result_df["Risk_Score"] = risk_scores
result_df["Risk_Label"] = result_df["Risk_Score"].apply(lambda x: "High" if x >= 0.5 else "Low")

st.success(f"Model Accuracy: {acc:.2f}")

st.subheader("All Employees")
st.dataframe(result_df.astype(str), width="stretch")

st.subheader("🚨 High-Risk Employees")
high_risk = result_df[result_df["Risk_Label"] == "High"]
if len(high_risk) == 0:
    st.info("No high-risk employees found.")
else:
    st.dataframe(high_risk.astype(str), width="stretch")

# Save for other pages
st.session_state["result_df"] = result_df
