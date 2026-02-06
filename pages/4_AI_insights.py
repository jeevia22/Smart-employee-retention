import streamlit as st

from utils.ai_recommendation import get_ai_insights

st.set_page_config(page_title="AI Insights", page_icon="🧠", layout="wide")
st.title("🧠 AI Explanation & Recommendations")

if "result_df" not in st.session_state:
    st.warning("Please run Predictions page first.")
    st.stop()

df = st.session_state["result_df"]
high_risk = df[df["Risk_Label"] == "High"].reset_index(drop=True)

if len(high_risk) == 0:
    st.info("No high-risk employees available.")
    st.stop()

idx = st.selectbox("Select High-Risk Employee", options=high_risk.index)
emp = high_risk.loc[idx]

st.subheader("Selected Employee")
st.write(emp.astype(str))

if st.button("Generate AI Insights"):
    with st.spinner("Generating..."):
        ai_text = get_ai_insights(emp.to_dict(), emp["Risk_Score"])
    st.subheader("🧠 AI Output")
    st.write(ai_text)
