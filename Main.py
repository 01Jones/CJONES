# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4

# app.py
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import requests
import csv
import twikit
from twikit import Client, TooManyRequests
from random import randint
import yfinance as yf

# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4
# KtkauE_-pic1EFrCBFb4

# Input your API credentials
api_key = "5Od9JIeK9BDVnOjjgQvvSdVAh"
api_secret = "djtjd1gRUvTki5YRLl006rGsjpQ3SzMJYfji317XvE1XYBSrrf"
access_token = "744622183-PYWccpQMhkATqVZpERjasovNDcer3U54bdDuNRPY"
access_token_secret = "GGJcu8ksG3lSrnlOa4vl3xWn7uFhD0eO1uyRA4Mwn08Vx"
#Bearer AAAAAAAAAAAAAAAAAAAAAD5OxQEAAAAAXI1jaL%2FDeiCB6yERuuax5dIm%2BuU%3DtHW0CzBCgwgHX7nQgrCRbHlFNYsfaDnEmmLBkhnrTC8XmymcHV
USERNAME = 'example_user'
EMAIL = 'email@example.com'
PASSWORD = 'password0000'





# Sidebar Navigation
st.sidebar.markdown('Navigation')
option = st.sidebar.radio("Select a page", ('Home', 'Watchlist', 'Twitter', 'Performance', 'Company Insights', 'Comparison Analysis', 'Framework')) 


#Home Page
if option == 'Home':
    st.title("Home")
    st.title("Home Page")


#Watchlist Page
if option == 'Watchlist':
    st.title("Watchlist")
    st.title("Tweet Tracker")
