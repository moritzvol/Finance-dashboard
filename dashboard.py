import requests, pandas as pd, streamlit as st
from API_Key import api_key

st.header('Financial Dashboard')

endpoint = st.sidebar.selectbox('Endpoint: ',options= ['A','B'])

url = f'https://marketdata.tradermade.com/api/v1/historical?api_key={api_key}'

if endpoint == 'A':
    curr1 = st.sidebar.text_input("From currency","USD")
    curr2 = st.sidebar.text_input("From currency","EUR")
    amount = st.sidebar.text_input('Amount','1000')
    extension = f'&from={curr1}&to{curr2}&amount={amount}'
    url = url + extension
    data = requests.get(url).json()
    st.write(data)