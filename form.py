import streamlit as sl
import pyrebase
import webbrowser
config={
    "apiKey": "AIzaSyCilEt1u-MY3Yz56_fPoGbsysgLoweReYI",
    "authDomain": "newsletter-f9a5f.firebaseapp.com",
    "projectId": "newsletter-f9a5f",
    "databaseURL":"https://newsletter-f9a5f-default-rtdb.firebaseio.com/",
    "storageBucket": "newsletter-f9a5f.appspot.com",
    "messagingSenderId": "793080417319",
    "appId": "1:793080417319:web:4bcc987850a3fd934c5202",
    "measurementId": "G-NNWFG7Z232"
}
firebase=pyrebase.initialize_app(config)
db=firebase.database()

sl.title('Sponsor us!')
inp=sl.text_input('Name:')
inp2=sl.text_input('Email:')

btn=sl.button('Continue!')

if btn:
   
    data={inp:""}
    r=inp2.replace('.','')
    data2={r:""}

    db.child('Form').child('Name').update(data)
    db.child('Form').child('Email').update(data2)
     webbrowser.open('https://rattleofficial.github.io/sponsor/payment.html')
    

   
