# 📊 Amazon Customer Reviews Sentiment Analysis

## 🔹 Project Overview
This project builds an **end-to-end sentiment analysis pipeline** on Amazon product reviews to classify text as **Positive, Neutral, or Negative**.  
It demonstrates **data preprocessing, NLP (TF-IDF), machine learning, imbalance handling (SMOTE), model tuning, and business insights**.  

👉 Live Demo (if deployed on Streamlit): [Streamlit App Link Here]  
👉 Full Report: See `notebooks/` or project documentation  

---

## 🔹 Workflow
1. **Data Preprocessing**: Cleaned reviews (lowercasing, punctuation removal, missing values).  
2. **Exploratory Data Analysis (EDA)**:  
   - Rating distribution skewed to positives.  
   - Negative reviews longer & more detailed.  
   - Frequent positive words: *great, good, sound*.  
   - Frequent negative words: *waste, dont, back, buy*.  
3. **Sentiment Labeling**: Based on star ratings.  
4. **Feature Engineering**: TF-IDF vectorization.  
5. **Model Training & Evaluation**: Compared Naive Bayes, Logistic Regression, Linear SVC.  
6. **Class Imbalance Handling**: Applied **SMOTE** oversampling.  
7. **Hyperparameter Tuning**: GridSearchCV for optimized models.  

---

## 🔹 Results
| Model                  | Accuracy | F1-score (Weighted) |
|-------------------------|----------|----------------------|
| Naive Bayes             | 0.88     | 0.82 |
| Logistic Regression     | 0.88     | 0.83 |
| Linear SVC              | 0.88     | 0.85 |
| **Linear SVC + SMOTE**  | **0.85** | **0.85** |

✅ **Best Model**: **Linear SVC with SMOTE**, balancing accuracy and class performance.  
✅ Negative/Neutral recall improved after SMOTE.  

---

## 🔹 Business Insights
- Only ~5% of reviews are strongly negative → products with many negatives can be flagged for **quality checks**.  
- Reviews with words like *“back”* or *“return”* are **3.5× more likely** to be 1-star → signals refund/return risks.  
- Positive reviews emphasize *quality, sound, great* → key **marketing highlights**.  

---

## 🔹 Tech Stack
- **Languages/Libraries**: Python, Pandas, Scikit-learn, Imbalanced-learn, NLTK, Matplotlib, Seaborn  
- **Techniques**: NLP (TF-IDF), SMOTE, Model Selection, Hyperparameter Tuning  
- **Deployment**: Streamlit (interactive app)  

---

## 🔹 Future Improvements
- Use **word embeddings** (Word2Vec, GloVe) or **transformers** (BERT).  
- Add **explainability** with SHAP/LIME.  
- Build an interactive **dashboard** for bulk review sentiment analysis.  

---

✍️ **Author**: [Your Name]  
📌 **GitHub Repo**: [Link to this repo]  
🚀 **Streamlit App**: [Link once deployed]  
