import streamlit as st
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Upload Datasets", page_icon="📤", layout="wide")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_uploaded_file(uploaded_file):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}_{uploaded_file.name}"
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return filename, filepath

def list_uploaded_files():
    files = os.listdir(UPLOAD_DIR)
    files.sort(reverse=True)
    return files

def delete_file(filename):
    path = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(path):
        os.remove(path)

st.title("📤 Upload & Manage Datasets")

st.subheader("Upload New CSV")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    filename, filepath = save_uploaded_file(uploaded_file)
    st.success(f"Saved: {filename}")
    st.session_state["active_dataset"] = filepath

st.divider()

st.subheader("📁 Upload History")

files = list_uploaded_files()

if len(files) == 0:
    st.info("No files uploaded yet.")
else:
    for f in files:
        col1, col2, col3 = st.columns([6,1,1])
        col1.write(f)
        if col2.button("📂 Load", key=f"load_{f}"):
            st.session_state["active_dataset"] = os.path.join(UPLOAD_DIR, f)
            st.success(f"Loaded: {f}")
        if col3.button("🗑️ Delete", key=f"del_{f}"):
            delete_file(f)
            st.warning(f"Deleted: {f}")
            st.rerun()


st.divider()

if "active_dataset" in st.session_state:
    st.subheader("👀 Active Dataset Preview")
    df = pd.read_csv(st.session_state["active_dataset"])
    st.dataframe(df.astype(str), width="stretch")
else:
    st.info("No dataset loaded. Upload or load one from history.")
