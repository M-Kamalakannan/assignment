
import streamlit as st

import pandas as pd
df=pd.read_excel("https://github.com/M-Kamalakannan/assignment/blob/main/preprocessed_data.xlsx")
from sklearn.model_selection import train_test_split
from sklearn import datasets, linear_model, metrics

y = df[['Risk_Level']]
x = df[['AAP.mm.','RiverDIST.m.','FaultDIST.m.','Slop.Percent.']]

X_train, X_test,y_train, y_test = train_test_split(x, y,test_size=0.005,random_state=1)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

reg = linear_model.LogisticRegression()
reg.fit(X_train, y_train)

def prediction(rainfall,riverdist,faultdist,slope):
  prediction=reg.predict([[rainfall,riverdist,faultdist,slope]])
  print(prediction)
  return prediction
def main():
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
  

