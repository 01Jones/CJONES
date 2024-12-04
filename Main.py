# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4

# app.py

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import requests
import twikit
import tweepy
from bs4 import BeautifulSoup


# Input your API credentials
api_key = "5Od9JIeK9BDVnOjjgQvvSdVAh"
api_secret = "djtjd1gRUvTki5YRLl006rGsjpQ3SzMJYfji317XvE1XYBSrrf"
access_token = "744622183-PYWccpQMhkATqVZpERjasovNDcer3U54bdDuNRPY"
access_token_secret = "GGJcu8ksG3lSrnlOa4vl3xWn7uFhD0eO1uyRA4Mwn08Vx"
#Bearer AAAAAAAAAAAAAAAAAAAAAD5OxQEAAAAAXI1jaL%2FDeiCB6yERuuax5dIm%2BuU%3DtHW0CzBCgwgHX7nQgrCRbHlFNYsfaDnEmmLBkhnrTC8XmymcHV





# Sidebar Navigation
# Sidebar dropdown 
option = st.sidebar.selectbox("Dashboard", ('Home', 'Economic Insights', 'Valuation Models', 'Performance', 'Company Insights', 'Comparison Analysis', 'Framework')) 



# Streamlit app title
if option == 'Home':
    st.title("Home Page")
    st.write("Welcome to the Home Page! Here's an overview of the website.")
    st.title("Ticker Tweet Tracker")
    st.write("Enter a stock ticker to see the total number of tweets mentioning it over 1 day, 7 days, and 30 days.")

# Input box for ticker
    ticker = st.text_input("Enter a Ticker Symbol (e.g., AAPL, TSLA, MSFT):", value="$AAPL").strip()






