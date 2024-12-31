import streamlit as st
import requests
import json

# Title of the app
st.title("Ames House Price Prediction")

# Instructions
st.write("Enter the house details below to get a price prediction.")

# Input fields for the house details
Lot_Area = st.number_input("Lot Area (in square feet)", min_value=0)
Year_Built = st.number_input("Year Built", min_value=1800, max_value=2024, step=1)
Total_Bsmt_SF = st.number_input("Total Basement Area (in square feet)", min_value=0)
Gr_Liv_Area = st.number_input("Above Ground Living Area (in square feet)", min_value=0)
Garage_Area = st.number_input("Garage Area (in square feet)", min_value=0)
Overall_Qual = st.slider("Overall Quality", min_value=1, max_value=10)
Overall_Cond = st.slider("Overall Condition", min_value=1, max_value=10)

# Create a predict button
if st.button("Predict"):
    # Prepare data for API request
    data = {
        "Lot_Area": Lot_Area,
        "Year_Built": Year_Built,
        "Total_Bsmt_SF": Total_Bsmt_SF,
        "Gr_Liv_Area": Gr_Liv_Area,
        "Garage_Area": Garage_Area,
        "Overall_Qual": Overall_Qual,
        "Overall_Cond": Overall_Cond,
    }

    # API URL (update the URL if needed)
    url = "http://127.0.0.1:8000/predict/"

    try:
        # Send request to the backend
        response = requests.post(url, json=data)
        
        if response.status_code == 200:
            prediction = response.json()["prediction"]
            st.success(f"Predicted House Price: ${prediction:,.2f}")
        else:
            st.error("Error occurred while making the prediction.")
            st.write(response.text)  # Display the backend error message

    except Exception as e:
        st.error(f"An error occurred: {e}")
