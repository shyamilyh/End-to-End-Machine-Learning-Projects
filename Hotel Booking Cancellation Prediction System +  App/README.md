# 🏨 Hotel Booking Cancellation Prediction System with Deployment  

### 📘 Overview  
This project focuses on developing a **Machine Learning (ML)–based system** that predicts **hotel booking cancellations** using historical booking data.  
The goal is to identify patterns and key factors influencing cancellations, enabling hotels to proactively manage bookings, minimize losses, and enhance revenue forecasting.  

---

## ⚙️ Project Workflow  

1. **Project Objective**  
   - Build a **predictive model** that accurately forecasts whether a booking will be canceled or confirmed.  
   - Analyze the **impact of various booking-related factors** such as customer type, lead time, deposit type, room type, and more.  
   - Enable hotels to take **preventive actions** like sending reminders, offering discounts, or adjusting overbooking strategies.  

2. **Data Loading & Exploration**  
   - Loaded the hotel booking dataset for two hotel types: *City Hotel* and *Resort Hotel*.  
   - Conducted exploratory steps to understand the dataset’s structure, data types, and initial statistics.  
   - Identified important features and potential issues such as missing or inconsistent data.  

3. **Data Cleaning & Preprocessing**  
   - Handled missing values with **appropriate imputation techniques**.  
   - Treated **outliers** (notably in `adr` – Average Daily Rate) to prevent model skewing.  
   - Encoded categorical features (e.g., hotel type, customer type, deposit type).  
   - Scaled numerical variables for consistent feature representation.  
   - Ensured the dataset was ready for model training and validation.  

4. **Exploratory Data Analysis (EDA)**  
   - Conducted visual and statistical analyses to identify patterns between features and the target variable (*cancellation*).  
   - Explored distributions for:  
     - Lead time vs. cancellation likelihood  
     - Seasonality trends  
     - Impact of customer type, market segment, and country of origin  
   - Used visualizations (heatmaps, bar plots, histograms) to understand relationships and feature importance.  

5. **Feature Engineering**  
   - Created new features such as **stay duration**, **booking month**, and **previous cancellations**.  
   - Checked feature correlations to improve model interpretability.  

6. **Model Building & Evaluation**  
   - Applied and compared several ML models:  
     - **Logistic Regression**  
     - **Random Forest Classifier**  
     - **XGBoost Classifier**  
   - Split data into **training and test sets** (typically 80/20).  
   - Evaluated performance using metrics: **Accuracy**, **Precision**, **Recall**, **F1-score**, and **ROC-AUC**.  
   - The **Random Forest model** achieved the best balance between performance and interpretability.  

7. **Model Deployment**  
   - Built a **Streamlit-based web application** for interactive prediction.  
   - Users can input booking details (lead time, deposit type, room type, etc.) to predict whether a booking is likely to be canceled.  
   - Designed a user-friendly interface for hotel staff to make real-time data-driven decisions.  

---

## 📊 Key Findings  

- 🏙️ **Hotel Type Insight:**  
  - *City Hotels* had a higher cancellation rate than *Resort Hotels*.  

- ⏱️ **Lead Time:**  
  - Bookings made far in advance showed a **higher probability of cancellation**.  

- 💳 **Deposit Type:**  
  - Guests who paid **no deposit** were more likely to cancel.  

- 🌦️ **Seasonal Trend:**  
  - Peak seasons (e.g., summer months) recorded higher booking volumes but also higher cancellation risks.  

- 👥 **Customer Type:**  
  - *Transient customers* (individual travelers) contributed most to cancellations, while *group bookings* showed more stability.  

---

## 🧠 Insights & Business Impact  

- Enables hotels to **reduce last-minute cancellations** through proactive strategies (reminders, incentives).  
- Improves **revenue forecasting accuracy** and **inventory management**.  
- Supports **data-driven decision-making** in overbooking and promotional strategies.  
- Empowers management to offer **personalized retention campaigns** for high-risk customers.  

---

## 🧰 Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| Programming | Python |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Deployment | Streamlit |
| Environment | Jupyter Notebook |

---

## ✅ Results & Conclusion  

This project successfully built and deployed a **hotel booking cancellation prediction model** capable of accurately forecasting cancellations.  
The deployed app allows hotel managers to quickly assess cancellation risk and apply corrective measures to reduce financial loss and improve operational efficiency.  

Key results include:  
- Improved understanding of **factors influencing cancellations**.  
- **Accurate classification performance** with Random Forest and XGBoost.  
- **Deployed prediction system** accessible via an easy-to-use Streamlit interface.  

---

