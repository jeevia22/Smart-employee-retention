import streamlit as st

from utils.pdf_generator import generate_pdf_report
from utils.ai_recommendation import get_ai_insights

st.set_page_config(page_title="Reports", page_icon="📄", layout="wide")
st.title("📄 PDF Reports")

if "result_df" not in st.session_state:
    st.warning("Please run Predictions page first.")
    st.stop()

df = st.session_state["result_df"]
high_risk = df[df["Risk_Label"] == "High"]

if len(high_risk) == 0:
    st.info("No high-risk employees to report.")
    st.stop()

if st.button("Generate PDF Report"):
    with st.spinner("Generating PDF with AI insights..."):
        records = []
        for _, row in high_risk.iterrows():
            rec = row.to_dict()
            ai_text = get_ai_insights(rec, rec["Risk_Score"])
            rec["AI_Insights"] = ai_text
            records.append(rec)

        pdf_path = generate_pdf_report(records)

    st.success("PDF generated!")

    with open(pdf_path, "rb") as f:
        st.download_button(
            "📥 Download High-Risk Employees Report",
            f,
            file_name="High_Risk_Employees_Report.pdf",
            mime="application/pdf"
        )
