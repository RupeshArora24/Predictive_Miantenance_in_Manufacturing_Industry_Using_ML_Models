import streamlit as st 
import pandas as pd
import numpy as np

def main():
    st.title("Predective Maintainance In Manufacturing Industry using ML ")
    menu = ["Home","Login","SignUp"]
    submenu=["Plot","Prediction"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice=="Home" :
        st.subheader("Home")
        st.text("Why Maintainance is Important ?")
    elif choice == "Login":
        username = st.sidebar.text_input("Username")
        Password = st.sidebar.text_input("Password",type='password')
        if st.sidebar.checkbox("Login"):
            if Password == "12345":
                st.success("Welcome {}".format(username))
                activity = st.selectbox("Activity",submenu)
                if activity=="Plot" :
                    st.subheader("Data Visualization")
                elif activity=="Prediction":
                    st.subheader("Predective Analytics")    
        else:
                st.warning("Incorrect Username OR Password !!! ")  

if __name__=='main':
    main()                  