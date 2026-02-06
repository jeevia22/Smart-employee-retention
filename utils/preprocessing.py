import pandas as pd
from sklearn.preprocessing import LabelEncoder

REQUIRED_COLUMNS = ["Age", "MonthlyIncome", "JobLevel", "YearsAtCompany", "OverTime", "Attrition"]

def validate_dataset(df: pd.DataFrame):
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        return False, missing_cols
    return True, []

def preprocess_data(df: pd.DataFrame):
    data = df.copy()

    # Encode categorical columns
    overtime_encoder = LabelEncoder()
    attrition_encoder = LabelEncoder()

    data["OverTime"] = overtime_encoder.fit_transform(data["OverTime"])
    data["Attrition"] = attrition_encoder.fit_transform(data["Attrition"])

    X = data.drop("Attrition", axis=1)
    y = data["Attrition"]

    return X, y, data
