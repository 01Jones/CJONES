# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4

# app.py

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import requests
import twikit
from twiit import Client, TooManyrequests
import tweepy
from bs4 import BeautifulSoup


# Input your API credentials
api_key = "5Od9JIeK9BDVnOjjgQvvSdVAh"
api_secret = "djtjd1gRUvTki5YRLl006rGsjpQ3SzMJYfji317XvE1XYBSrrf"
access_token = "744622183-PYWccpQMhkATqVZpERjasovNDcer3U54bdDuNRPY"
access_token_secret = "GGJcu8ksG3lSrnlOa4vl3xWn7uFhD0eO1uyRA4Mwn08Vx"
#Bearer AAAAAAAAAAAAAAAAAAAAAD5OxQEAAAAAXI1jaL%2FDeiCB6yERuuax5dIm%2BuU%3DtHW0CzBCgwgHX7nQgrCRbHlFNYsfaDnEmmLBkhnrTC8XmymcHV





# Sidebar Navigation
st.sidebar.markdown('<h1 style="font-size: 30px;">Navigation</h1>', unsafe_allow_html=True)
option = st.sidebar.radio("Select a page", ('Home', 'Watchlist', 'Twitter', 'Performance', 'Company Insights', 'Comparison Analysis', 'Framework')) 


#Home Page
if option == 'Home':
    st.title("Home")
    st.title("Home Page")


#Watchlist Page
if option == 'Watchlist':
    st.title("Watchlist")
    st.title("Tweet Tracker")

    
# Twitter Page
if option == 'Twitter':
    st.title("Twitter")
    st.title("Tweet Tracker")
# Function to scrape Finviz news mentions for a ticker
    def scrape_finviz_mentions(ticker):
        # URL to search for the ticker symbol on Finviz news page
        url = f"https://finviz.com/quote.ashx?t={ticker}"
        
        # Send a GET request to Finviz
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            return None
        
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the news section (Finviz stores news in a div with class 'news-link')
        news_section = soup.find_all('a', class_='tab-link-news')
        
        # Filter news articles from the last 24 hours
        now = datetime.datetime.now()
        last_24_hours = now - datetime.timedelta(days=1)
        
        mentions_count = 0
        for news_item in news_section:
            # Extract the time and title of each news article
            news_title = news_item.get_text()
            news_url = news_item.get('href')
            
            # Find the timestamp for the news article (this is stored in a title attribute)
            news_time = news_item.get('title')
            if news_time:
                # Convert the time string to a datetime object
                news_time_obj = datetime.datetime.strptime(news_time, '%b-%d-%Y %I:%M%p')
                
                # If the article was posted within the last 24 hours, count it
                if news_time_obj >= last_24_hours:
                    mentions_count += 1
        
        return mentions_count
    
    # Streamlit app
    st.title('Finviz Ticker Mentions Counter')
    
    # Input for stock ticker
    ticker = st.text_input('Enter Ticker Symbol (e.g., AAPL, TSLA)', 'AAPL')
    
    if st.button('Get Mentions'):
        if ticker:
            mentions = scrape_finviz_mentions(ticker)
            if mentions is not None:
                st.write(f"Ticker {ticker} has been mentioned {mentions} times in the last 24 hours on Finviz news.")
            else:
                st.write(f"Failed to retrieve data for ticker {ticker}. Please check the symbol and try again.")
        else:
            st.write("Please enter a valid ticker symbol.")




