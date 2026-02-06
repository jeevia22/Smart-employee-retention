from fpdf import FPDF

def generate_pdf_report(high_risk_records):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "High-Risk Employees Attrition Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    if len(high_risk_records) == 0:
        pdf.cell(0, 10, "No high-risk employees found.", ln=True)
    else:
        for idx, record in enumerate(high_risk_records, start=1):
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"Employee {idx}", ln=True)
            pdf.set_font("Arial", size=11)

            # Employee details
            for key, value in record.items():
                if key not in ["AI_Insights"]:
                    pdf.multi_cell(0, 8, f"{key}: {value}")

            pdf.ln(2)

            # AI Insights
            pdf.set_font("Arial", "B", 11)
            pdf.cell(0, 8, "AI Explanation & Recommendations:", ln=True)
            pdf.set_font("Arial", size=11)
            pdf.multi_cell(0, 8, record.get("AI_Insights", "No AI insights available."))

            pdf.ln(8)
            pdf.line(10, pdf.get_y(), 200, pdf.get_y())
            pdf.ln(8)

    file_path = "high_risk_employees_report.pdf"
    pdf.output(file_path)

    return file_path
