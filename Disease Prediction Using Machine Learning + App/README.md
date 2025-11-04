# 🧠 Disease Prediction using Machine Learning & Streamlit

This project implements a **Disease Prediction System** based on symptoms using machine learning techniques.  
The model is trained on a symptom-disease dataset and deployed as an interactive **Streamlit web application**.

---

## 🚀 Project Overview

The notebook and app perform the following tasks:

1. **Data Preprocessing**
   - Handles missing values and feature scaling.
   - Encodes disease labels for machine learning compatibility.

2. **Model Training & Evaluation**
   - Trains multiple ML models: Random Forest, Support Vector Machine (SVM), and Naive Bayes.
   - Performs 5-Fold Stratified Cross-Validation for robust evaluation.
   - Tunes Random Forest hyperparameters with GridSearchCV (small `n_estimators` for fast training).
   - Implements a **Voting Ensemble** combining the three models for optimal accuracy.

3. **Model Performance**
   - Random Forest showed the most consistent accuracy among single models.
   - The **Voting Ensemble** outperformed all individual models with strong generalization and minimal overfitting.

4. **Deployment with Streamlit**
   - The trained model and label encoder are saved as `.pkl` files.
   - A Streamlit app provides a user-friendly interface for real-time disease prediction.

---

## 🧰 Tech Stack

| Component | Description |
|------------|-------------|
| **Python** | Core programming language |
| **Pandas / NumPy** | Data manipulation and numerical computation |
| **Scikit-learn** | Machine Learning models and preprocessing |
| **Matplotlib / Seaborn** | Data visualization |
| **Streamlit** | Interactive web app deployment |
| **Joblib / JSON** | Model and artifact serialization |

---

## 📂 Repository Structure

```
📦 Disease_Prediction
├── 🧮 Disease_Prediction_Using_Machine_Learning.ipynb
├── 📜 app.py
├── 📁 serve_artifacts/
│   ├── ensemble_model.pkl
│   ├── label_encoder.pkl
│   ├── numeric_features.json
│   └── all_input_cols.json
├── 📄 README.md
├── 📄 requirements.txt
└── 📊 Training.csv / Testing.csv
```

---

## ⚙️ How to Run Locally

1. Clone the repository or download the files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter notebook to train and export the model:
   ```bash
   jupyter notebook Improved_Disease_Prediction_Final.ipynb
   ```
4. Start the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

---

## 🩺 Usage

### Option 1: Single Input Mode
- Enter each symptom manually in the Streamlit form.
- Click **Predict** to see the predicted disease.

### Option 2: Batch Prediction Mode
- Upload a `.csv` file containing the same columns as the training data.
- The app displays predictions for all rows.

---

## 📈 Results Summary

| Model | Technique | Accuracy (Approx.) | Notes |
|--------|------------|------------------|--------|
| Random Forest | Ensemble of decision trees | ~98-99% | Best single model |
| SVM | Non-linear classifier | ~96-97% | Requires feature scaling |
| Naive Bayes | Probabilistic model | ~94-95% | Fast baseline |
| **Voting Ensemble** | Soft voting (RF + SVM + NB) | **~99%+** | Best overall performer |

---

## 🌟 Future Improvements

- Integrate deep learning models (e.g., MLP, Autoencoders).
- Incorporate symptom severity or duration as additional inputs.
- Add SHAP or LIME explainability to improve interpretability.
- Deploy on **Streamlit Cloud** or **Hugging Face Spaces** for public access.

---

## 👩‍💻 Author

Developed as part of a Machine Learning deployment project for healthcare analytics.  
Feel free to contribute or suggest improvements!
