import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("model_building/decision_tree_model.pkl", "rb"))

st.title("🛒 SuperKart Sales Prediction App")

st.write("Enter Product Details")

# Example input fields
feature1 = st.number_input("Feature 1")
feature2 = st.number_input("Feature 2")
feature3 = st.number_input("Feature 3")

if st.button("Predict"):
    input_data = pd.DataFrame(
        [[feature1, feature2, feature3]],
        columns=["feature1", "feature2", "feature3"]
    )

    prediction = model.predict(input_data)

    st.success(f"Predicted Sales: {prediction[0]}")