import os
from groq import Groq

# Initialize Groq client using API key from environment
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_ai_insights(employee_details: dict, risk_score: float):
    prompt = f"""
You are an expert HR analytics consultant.

An employee has the following details:
{employee_details}

The machine learning model predicts a HIGH attrition risk with a risk score of {risk_score:.2f}.

1. Explain in simple terms why this employee might be at risk.
2. Provide 3 to 5 practical HR recommendations to retain this employee.

Write the response in a clear, professional, and HR-friendly manner.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ Currently supported Groq model
        messages=[
            {"role": "system", "content": "You are an expert HR consultant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )

    return response.choices[0].message.content
