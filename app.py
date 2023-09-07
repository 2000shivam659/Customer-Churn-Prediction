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
# Convert age to an integer (assuming age should be an integer)
age = int(age) if age else 0

# Take gender inputs from user
gender_input = st.selectbox("Customer Gender", 
                      ['Male', 'Female'])
gender = 1 if gender_input == 'Male' else 0

# Take location inputs from user
location = st.selectbox("Customer Location", 
                        ['Houston', 'Los Angeles', 'Miami', 'Chicago', 'New York'])
Location_Houston, Location_Los_Angeles, Location_Miami, Location_Chicago, Location_New_York = 0, 0, 0, 0, 0
if location == 'Houston':
    Location_Houston = 1
elif location == 'Los Angeles':
    Location_Los_Angeles = 1   
elif location == 'Miami':
    Location_Miami = 1
elif location == 'New York':
    Location_New_York = 1
else:
    Location_Chicago = 1

# Take Month Of Subscription inputs from user
subscription_length_months = st.text_input("Subscription Months:")
# Convert subscription_length_months to an integer (assuming it should be an integer)
subscription_length_months = int(subscription_length_months) if subscription_length_months else 0

# Take Monthly Bill inputs from user
monthly_bill = st.text_input("Monthly Bill ($):")
# Convert monthly_bill to a float (assuming it should be a floating-point number)
monthly_bill = float(monthly_bill) if monthly_bill else 0.0

# Take Total Used GB inputs from user
total_used_gb = st.text_input("Total Usage (GB):")
# Convert total_used_gb to a float (assuming it should be a floating-point number)
total_used_gb = int(total_used_gb) if total_used_gb else 0

# Create an array of all these inputs
features = [{
    'Age': age,
    'Gender': gender,
    'Subscription_Length_Months': subscription_length_months,
    'Monthly_Bill': monthly_bill,
    'Total_Usage_GB': total_used_gb,
    'Total_Bill': int(subscription_length_months) * int(monthly_bill) if subscription_length_months and monthly_bill else 0,
    'Location_Houston': Location_Houston,
    'Location_Los Angeles': Location_Los_Angeles,
    'Location_Miami': Location_Miami,
    'Location_New York': Location_New_York,
}]

# Convert it to pandas DataFrame before passing it to the model
features_df = pd.DataFrame(features)

if total_used_gb:
    output = model.predict(features_df)
    if output == 1:
        st.error("Alert: Possible Churn Risk")
    elif output == 0:
        st.success("Steadfast Customer: Demonstrating Loyalty")
