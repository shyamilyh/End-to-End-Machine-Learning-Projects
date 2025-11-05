import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

# Streamlit UI
st.set_page_config(page_title="Amazon Sentiment Analysis", layout="centered")
st.title("📊 Amazon Reviews Sentiment Analysis")
st.write("Enter a product review to predict sentiment (Positive / Neutral / Negative).")

# Input box
review = st.text_area("✍️ Type your review here:")

if st.button("Analyze Sentiment"):
    if review.strip() != "":
        cleaned = clean_text(review)
        features = vectorizer.transform([cleaned])
        prediction = model.predict(features)[0]

        if prediction == "Positive":
            st.success("✅ Sentiment: Positive")
        elif prediction == "Neutral":
            st.info("😐 Sentiment: Neutral")
        else:
            st.error("❌ Sentiment: Negative")
    else:
        st.warning("Please enter a review before analyzing.")
