import streamlit as st 
import joblib 

model = joblib.load('sentiment-model.pkl')

sentiment_lable={'1':'Positive', '0':'Negative'}

st.title("Sentiment Analysis")

user_input=st.text_area("Enter your text here")

if st.button("Predict"):
    predict_sentiment = model.predict([user_input])[0]
    #print("Predicted Label:"+str(predict_sentiment))
    predict_sentiment_lable=sentiment_lable[str(predict_sentiment)]

    st.info(f"Predicted Sentiment: {predict_sentiment_lable}")

