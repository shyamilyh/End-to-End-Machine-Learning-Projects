import streamlit as st
import joblib

# Load the trained model and label encoder
MODEL_PATH = 'best_disease_model.pkl'
model = joblib.load(MODEL_PATH)

# For simplicity, re-fitting on the training data labels. In a real scenario,
# the fitted label encoder should also be saved and loaded.
TRAIN_PATH = 'Training.csv'
df_train = pd.read_csv(TRAIN_PATH)
TARGET = 'prognosis' if 'prognosis' in df_train.columns else df_train.columns[-1]
le = LabelEncoder()
le.fit(df_train[TARGET])

st.title('Disease Prediction App')
st.write('Enter the symptoms to predict the disease.')

# Get the list of symptoms (features) from the training data, excluding the target
symptoms = df_train.drop(columns=[TARGET]).columns.tolist()

# Create input fields for symptoms
st.sidebar.header('Select Symptoms')
input_data = {}
for symptom in symptoms:
    input_data[symptom] = st.sidebar.checkbox(symptom.replace('_', ' ').title(), value=False)

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Make prediction when the button is clicked
if st.button('Predict Disease'):
    # Ensure the input columns match the training data columns
    # This is crucial if the model expects a specific order/set of features
    # For simplicity, assume the order is the same and all symptoms from training are present
    # in the sidebar checkboxes. In a more robust app, handle missing features.

    # The model pipeline includes preprocessing, so we feed the raw input_df
    prediction_encoded = model.predict(input_df)
    predicted_disease = le.inverse_transform(prediction_encoded)[0]
    st.subheader('Predicted Disease:')
    st.write(predicted_disease)

st.title('Disease Prediction App')
st.write('Select the symptoms you are experiencing from the list below and click "Predict Disease".')

# Get the list of symptoms (features) from the training data, excluding the target
symptoms = df_train.drop(columns=[TARGET]).columns.tolist()

# Create input fields for symptoms
st.sidebar.header('Select Symptoms')
input_data = {}
for symptom in symptoms:
    # Format symptom names for readability
    display_symptom = symptom.replace('_', ' ').title()
    input_data[symptom] = st.sidebar.checkbox(display_symptom, value=False)

# Convert input data to a DataFrame
input_df = pd.DataFrame([input_data])

# Add a button to trigger prediction
if st.button('Predict Disease'):
    # Make prediction when the button is clicked
    # Ensure the input columns match the training data columns
    # This is crucial if the model expects a specific order/set of features
    # For simplicity, assume the order is the same and all symptoms from training are present
    # in the sidebar checkboxes. In a more robust app, handle missing features.

    # The model pipeline includes preprocessing, so we feed the raw input_df
    prediction_encoded = model.predict(input_df)
    predicted_disease = le.inverse_transform(prediction_encoded)[0]
    st.subheader('Predicted Disease:')
    st.write(predicted_disease)

# Ensure the columns of the input DataFrame are in the same order as the training data
training_columns = df_train.drop(columns=[TARGET]).columns
input_df = pd.DataFrame([input_data])[training_columns]

# Make prediction when the button is clicked
if st.button('Predict Disease'):
    # The model pipeline includes preprocessing, so we feed the raw input_df
    prediction_encoded = model.predict(input_df)
    predicted_disease = le.inverse_transform(prediction_encoded)[0]
    st.subheader('Predicted Disease:')
    st.write(predicted_disease)

# Make prediction when the button is clicked
if st.button('Predict Disease'):
    # The model pipeline includes preprocessing, so we feed the raw input_df
    prediction_encoded = model.predict(input_df)
    predicted_disease = le.inverse_transform(prediction_encoded)[0]
    st.subheader('Predicted Disease:')
    st.write(predicted_disease)

st.markdown("""
## How to run this app

1.  **Install Streamlit:** If you don't have Streamlit installed, open your terminal or command prompt and run:
    ```bash
    pip install streamlit
    ```

2.  **Run the app:** Navigate to the directory where you saved this `app.py` file in your terminal or command prompt and run:
    ```bash
    streamlit run app.py
    ```
""")
