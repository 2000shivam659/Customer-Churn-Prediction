import pickle
import pandas as pd
import streamlit as st
import pandas as pd

# Set basic page configuration
st.set_page_config(
    page_title="Customer_Churn_Prediction_Model",
    page_icon="$",
    layout="centered"
)

# Load the model
with open("XGB_Churn_Classifier.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Custom CSS for background color and style
st.markdown(
    """
    <style>
    body {
        background-color: #F0F0F0; /* Change to your desired background color */
        font-family: Arial, sans-serif; /* Change font family */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create page header with custom style
st.markdown(
    """
    <h1 style='text-align: center; color: #336699;'>Customer Churn Prediction Model</h1>
    <p style='text-align: center; font-size: 20px; color:red;'>Please fill out the following form:</p>
    """,
    unsafe_allow_html=True
)

# Take Age inputs from user
age = st.text_input("Customer Age:")

# Take gender inputs from user
gender = st.selectbox("Customer Gender", 
                      ['Male', 'Female'])

# Take location inputs from user
location = st.selectbox("Customer Location", 
                        ['Houston', 'Los Angeles', 'Miami', 'Chicago', 'New York'])

# Take Month Of Subscription inputs from user
subscription_length_months = st.text_input("Subscription Months:")

# Take Monthly Bill inputs from user
monthly_bill = st.text_input("Monthly Bill ($):")

# Take Total Used GB inputs from user
total_used_gb = st.text_input("Total Usage (GB):")

# Create an array of all these inputs
features = [{
    'Age': age,
    'Gender': gender,
    'Location': location,
    'Subscription_Length_Months': subscription_length_months,
    'Monthly_Bill': monthly_bill,
    'Total_Usage_GB': total_used_gb
}]

# Convert it to pandas DataFrame before passing it to the model
features_df = pd.DataFrame(features)

if total_used_gb:
    output = model.predict(features_df)
    if output == 1:
        st.error("Alert: Possible Churn Risk")
    elif output == 0:
        st.success("Steadfast Customer: Demonstrating Loyalty")
