import streamlit as st
import pandas as pd
import pandas as pd
import pickle 
import numpy as np

#load the model
with open('churn_model.pkl','rb') as f:
    model = pickle.load(f)
st.set_page_config(page_title="Churn Prediction",page_icon=":guardsman:",layout="wide")
st.title("Churn Prediction Intelligence Dashboard")
st.markdown("predict the likelihood of a customer cancellation using Machine Learning model")

#-Sidebar
st.sidebar.header("Individual customer data")
tenure = st.sidebar.slider("Tenure(months)",0,72,12)
monthly_charges = st.sidebar.number_input("Monthly Charges($)",0,200,70)
contract=st.sidebar.selectbox("Contract Type",["Month-to-month","One year","Two year"])

#simple mapping for individual prediction 
input_data = np.array([[tenure, monthly_charges, 0 if contract == "Month-to-month" else (1 if contract == "One year" else 2)] + [0]*16])
if st.sidebar.button("Predict churn"):
    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)[0][1]
    if prediction[0]==1:
        st.sidebar.error(f"High risk : {prob:.2%} chance of churn")
    else:
        st.sidebar.success(f"Low risk : {prob:.2%} chance of churn")       

#-------Main Page: Bulk Prediction
st.subheader("Bulk Prediction")
uploaded_file = st.file_uploader("Upload a CSV file for batch processing",type=["csv"])   
if uploaded_file :
    data = pd.read_csv(uploaded_file)
    st.write("Data Preview")
    st.dataframe(data.head())
    st.download_button("Download processed Results","result.csv","text/csv")


