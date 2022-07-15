# -*- coding: utf-8 -*-
import joblib
import streamlit as st

def main():
    
    html_temp = """
    <div style="background-color:blue;padding:16px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction</h2>
    </div>
    
    """
    
    st.markdown(html_temp, unsafe_allow_html=True)
    
    model= joblib.load("joblib_grad_boost")
    
    p1 = st.slider("Enter your age",18,100)
    
    s1 = st.selectbox("Sex", ("Male","Female"))
    
    if s1=="Male":
        p2= 1
        
    else:
        p2=0
        
    p3= st.number_input("Enter your BMI value")
    
    p4 = st.slider("Enter number of Children", 0,10)
    
    s2 = st.selectbox(("Smoker"), ("Yes","No"))
    
    if s2=="Yes":
        p5= 1
        
    else:
        p5=0
        
    s3 = st.selectbox(("Region Northeast"), ("Yes","No"))
    if s3=="Yes":
        
        p6= 1
        
    else:
        p6=0
        
    s4 = st.selectbox(("Region Northwest"), ("Yes","No"))
    if s4=="Yes":
        
        p7= 1
        
    else:
        p7=0
        
    s5 = st.selectbox(("Region Southeast"), ("Yes","No"))
    if s5=="Yes":
        
        p8= 1
        
    else:
        p8=0    
        

    s6 = st.selectbox(("Region Southwest"), ("Yes","No"))
    if s6=="Yes":
        
        p9= 1
        
    else:
        p9=0
    
    if st.button("Predict"):
    
        pred= model.predict([[p1,p2,p3,p4,p5,p6,p7,p8,p9]])
        
        
        
        st.balloons()
        st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
        
if __name__ == '__main__':
    main()
    
    
   