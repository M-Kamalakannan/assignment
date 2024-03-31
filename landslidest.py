import streamlit as st
import pandas as pd
import pickle
pic=open('regression',rb)
calssifier=pickle.load(pic)

def prediction(rainfall,riverdist,faultdist,slope):
  prediction=classifier.predict([[rainfall,riverdist,faultdist,slope]])
  print(prediction)
  return prediction
def main(:
  st.title("risk of landslide occurance prediction")
  html_temp=" "
  st.markdown(html_temp,unsafe_allow_html =True)
  rainfall=st.text_input("Anual rainfall","Type Here")
  riverdist=st.text_input("River distance","Type Here")
  faultdist=st.text_input("fault distance","Type Here")
  slope=st.text_input("slope ","Type Here")

if st.button("predict"):
  result=prediction(rainfall,riverdist,faultdist,slope)
st.success("the output is{}".format(result))
 if __name__=="__main__":
   main()
  
#X_test=[[ 0.77093807,0.00823664,0.35703567,2.45688651]]

#mj = joblib.load('regression_model.joblib')
#predicted=mj.predict(X_test)
#st.subheader(predicted)

