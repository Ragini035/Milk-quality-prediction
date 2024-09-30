import streamlit as st
import pickle
import sklearn

model = pickle.load(open("dtmodel3.pkl","rb"))

st.title("Milk quality Production")

ph = st.number_input("ph")
temp = st.number_input("Temperature")
test = st.number_input("Test")
odor = st.number_input("Odor")
Fat = st.number_input("Fat")
Turbidity = st.number_input("Turbidity")
color = st.number_input("Color")

# st.button("Submit")

def prediction(ph,temp,test,odor,Fat,Turbidity,color):
    output = model.predict([[ph,temp,test,odor,Fat,Turbidity,color]])
    st.write(output[0])

if st.button("Submit"):
    prediction(ph,temp,test,odor,Fat,Turbidity,color)

