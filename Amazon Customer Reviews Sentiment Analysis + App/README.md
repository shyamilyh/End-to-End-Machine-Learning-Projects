# 🛍️ Amazon Customer Reviews Sentiment Analysis  

### 📘 Overview  
This project focuses on building a **Sentiment Analysis Model** that classifies **Amazon customer reviews** as **positive**, **negative**, or **neutral**.  
The objective is to leverage **Natural Language Processing (NLP)** techniques to extract insights from customer opinions and assist Amazon in understanding customer satisfaction, identifying product issues, and improving overall service quality.  

---

## ⚙️ Project Workflow  

1. **Objective Definition**  
   - Develop a **machine learning model** to predict sentiment from customer reviews.  
   - Enable **data-driven business insights** into product performance, brand perception, and customer experience.  

2. **Data Loading & Exploration**  
   - Imported and explored the Amazon reviews dataset to understand its structure and attributes.  
   - Checked for **missing values**, **duplicates**, and **data types**.  
   - Reviewed sample reviews and their corresponding ratings to assess text quality.  

3. **Data Cleaning & Preprocessing**  
   - **Handled missing values** in `reviewerName` and `reviewText`.  
   - **Text cleaning**: removed punctuation, special characters, HTML tags, and converted text to lowercase.  
   - Tokenized and normalized text for NLP processing.  
   - Removed stopwords to improve signal-to-noise ratio.  

4. **Exploratory Data Analysis (EDA)**  
   - Visualized **rating distribution** to understand sentiment spread.  
   - Conducted **word frequency analysis** to identify common keywords in positive and negative reviews.  
   - Analyzed **review lengths vs ratings** to find correlation patterns.  
   - Displayed results using bar charts, word clouds, and histograms.  

5. **Feature Engineering**  
   - Transformed text data into numerical representations using **TF-IDF Vectorization**.  
   - Split the dataset into training and testing sets for model development.  

6. **Model Development**  
   - Built multiple models including:  
     - **Logistic Regression**  
     - **Naïve Bayes Classifier**  
     - **Random Forest Classifier**  
   - Trained models to predict review sentiment based on textual data.  

7. **Model Evaluation**  
   - Evaluated model performance using metrics like:  
     - **Accuracy**, **Precision**, **Recall**, and **F1-score**  
   - Compared confusion matrices to determine misclassification patterns.  
   - Selected the model with the **highest predictive accuracy and generalization performance**.  

---

## 📊 Key Findings  

- ⭐ **Sentiment Distribution:**  
  - Most reviews were **positive**, showing high customer satisfaction.  
  - A small fraction of reviews expressed **negative or neutral sentiment**.  

- 💬 **Frequent Words:**  
  - Positive reviews often included terms like *“excellent,” “great,” “love,”* and *“amazing.”*  
  - Negative reviews featured words like *“bad,” “poor,” “broke,”* and *“disappointed.”*  

- 📈 **Text Patterns:**  
  - Positive reviews tended to be shorter and more direct.  
  - Negative reviews were longer, often describing detailed product issues.  

- 🤖 **Model Performance:**  
  - The **Tuned Linear SVC** model achieved the best accuracy (around **94%**).  
  - The **TF-IDF vectorization** approach effectively captured important text features.  

---

## 🧠 Insights & Business Impact  

- Enables **real-time monitoring of customer feedback** for product teams.  
- Helps identify **product flaws** and **service issues** through negative review analysis.  
- Provides actionable insights for **marketing, pricing, and product development**.  
- Enhances **customer satisfaction** through targeted quality improvement.  

---

## 🧰 Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| Programming | Python |
| Data Handling | Pandas, NumPy |
| NLP Processing | NLTK, Scikit-learn, TF-IDF |
| Visualization | Matplotlib, Seaborn, WordCloud |
| Environment | Jupyter Notebook |

---

## ✅ Results & Conclusion  

The **Sentiment Analysis Model** accurately classifies customer reviews into positive, negative, and neutral categories.  
This enables businesses to **quantify customer sentiment**, extract valuable product insights, and respond proactively to customer needs.  

The analysis confirms that **text mining and NLP models** can play a crucial role in improving customer experience and brand reputation through intelligent feedback analysis.  

---


