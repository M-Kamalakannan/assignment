import streamlit as st
X_test=[[ 0.77093807  ,0.00823664  ,0.35703567 , 2.45688651]]
st.header("logistic regression")
import joblib
mj = joblib.load('regression_model.joblib')
predicted=mj.predict(X_test)
st.subheader(predicted)

