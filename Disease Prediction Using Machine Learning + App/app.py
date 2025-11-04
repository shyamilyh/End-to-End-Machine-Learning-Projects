# /app.py
import streamlit as st
import pandas as pd
import joblib
import os
from sklearn.preprocessing import LabelEncoder

st.set_page_config(page_title="Disease Predictor", layout="centered")

ARTIFACT_DIR = "serve_artifacts"   # folder in repo containing model + label encoder (or change to path)
MODEL_FNAME = "ensemble_model.pkl"
LABEL_FNAME = "label_encoder.pkl"

MODEL_PATH = os.path.join(ARTIFACT_DIR, MODEL_FNAME)
LABEL_PATH = os.path.join(ARTIFACT_DIR, LABEL_FNAME)

st.title("🩺 Disease Prediction Demo")

# Load model & label encoder
if not os.path.exists(MODEL_PATH):
    st.error(f"Model not found at {MODEL_PATH}. Upload the model to this path or update MODEL_PATH.")
    st.stop()
model = joblib.load(MODEL_PATH)

label_encoder = None
if os.path.exists(LABEL_PATH):
    label_encoder = joblib.load(LABEL_PATH)

# Try to infer input columns from model or fallback to Training.csv
# If you saved all_input_cols.json earlier, prefer that
COLS_FNAME = os.path.join(ARTIFACT_DIR, "all_input_cols.json")
if os.path.exists(COLS_FNAME):
    import json
    with open(COLS_FNAME, "r", encoding="utf-8") as f:
        input_cols = json.load(f)
else:
    # fallback: require user upload of a sample CSV
    st.info("No input column metadata found. Upload a sample CSV or ensure all_input_cols.json is saved under serve_artifacts.")
    upload = st.file_uploader("Upload a sample CSV (with feature columns)", type=["csv"])
    if upload is None:
        st.stop()
    sample = pd.read_csv(upload)
    input_cols = sample.columns.tolist()

st.sidebar.header("Input mode")
mode = st.sidebar.selectbox("Mode", ["Single sample (form)", "Upload CSV"])

if mode == "Upload CSV":
    uploaded = st.file_uploader("Upload CSV for batch predictions", type=["csv"])
    if uploaded:
        df_in = pd.read_csv(uploaded)
        # ensure same columns
        for c in input_cols:
            if c not in df_in.columns:
                df_in[c] = 0
        df_in = df_in[input_cols]
        st.write("Preview:")
        st.dataframe(df_in.head())
        if st.button("Predict batch"):
            preds = model.predict(df_in)
            if label_encoder is not None:
                preds = label_encoder.inverse_transform(preds)
            out = df_in.copy()
            out["prediction"] = preds
            st.dataframe(out.head())
            st.download_button("Download predictions (CSV)", out.to_csv(index=False), "preds.csv", "text/csv")
else:
    st.subheader("Enter features for a single sample")
    with st.form("single_form"):
        inputs = {}
        for c in input_cols:
            # assume binary/float numeric; adjust as needed
            inputs[c] = st.number_input(c, value=0.0, step=1.0)
        submitted = st.form_submit_button("Predict")
    if submitted:
        df_in = pd.DataFrame([inputs])[input_cols]
        try:
            pred = model.predict(df_in)
            if label_encoder is not None:
                pred_label = label_encoder.inverse_transform(pred)[0]
            else:
                pred_label = str(pred[0])
            st.success(f"Predicted disease: {pred_label}")
        except Exception as e:
            st.error("Prediction failed: " + str(e))
