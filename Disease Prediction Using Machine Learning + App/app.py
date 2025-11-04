import os
import json
import joblib
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Disease Predictor", layout="centered")
st.title("🩺 Disease Prediction App")

ARTIFACT_DIR = "serve_artifacts"
MODEL_PATH = os.path.join(ARTIFACT_DIR, "ensemble_model.pkl")
LABEL_PATH = os.path.join(ARTIFACT_DIR, "label_encoder.pkl")
COLS_PATH = os.path.join(ARTIFACT_DIR, "all_input_cols.json")

# Load model and artifacts
if not os.path.exists(MODEL_PATH):
    st.error(f"Missing model file at {MODEL_PATH}")
    st.stop()

model = joblib.load(MODEL_PATH)
label_encoder = None
if os.path.exists(LABEL_PATH):
    label_encoder = joblib.load(LABEL_PATH)

if not os.path.exists(COLS_PATH):
    st.error(f"Missing column metadata at {COLS_PATH}")
    st.stop()
with open(COLS_PATH, "r", encoding="utf-8") as f:
    input_cols = json.load(f)

st.sidebar.header("Input Mode")
mode = st.sidebar.radio("Mode", ["Single Sample", "Batch (CSV)"])

def prepare_df(df):
    for c in input_cols:
        if c not in df.columns:
            df[c] = 0
    return df[input_cols]

if mode == "Batch (CSV)":
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df.head())
        if st.button("Predict"):
            df = prepare_df(df)
            preds = model.predict(df)
            if label_encoder is not None:
                preds = label_encoder.inverse_transform(preds)
            df["prediction"] = preds
            st.dataframe(df.head())
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("Download Predictions", csv, "predictions.csv", "text/csv")
else:
    st.subheader("Enter values for one sample")
    with st.form("single_form"):
        vals = {c: st.number_input(c, value=0.0, step=1.0) for c in input_cols}
        submit = st.form_submit_button("Predict")
    if submit:
        df = pd.DataFrame([vals])
        df = prepare_df(df)
        preds = model.predict(df)
        if label_encoder is not None:
            preds = label_encoder.inverse_transform(preds)
        st.success(f"Predicted Disease: {preds[0]}")