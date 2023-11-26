import re
import streamlit as st

def validate_password(password):
    return len(password) > 5

def validate_username(username):
    return len(username) > 1

def validate_email(email):
    email_format = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_format, email))


def operations_on_password_email(password1,password2,email,username) :
   further = 0 

   if password1==password2:
          st.success("Pasword Matched")
   else:
         st.warning("Password no the same, re-enter the password")

   if not validate_password(password1):
            st.error('Password should be more than 5 characters')    
   else:
      further +=1 

   if not validate_email(email):
              st.error('Enter a valid email address')
   else:
        further+=1 

   if not validate_username(username):
              st.error('Please enter a valid username')
   else:
        further+=1 
    

   return further   

 

  
    
 