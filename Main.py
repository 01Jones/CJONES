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





# Main content based on navigation selection
st.sidebar.title("Navigation")
page = st.sidebar("Select a page", ["Home", "About", "Contact"])





# Streamlit app title
st.title("Ticker Tweet Tracker")
st.write("Enter a stock ticker to see the total number of tweets mentioning it over 1 day, 7 days, and 30 days.")

# Input box for ticker
ticker = st.text_input("Enter a Ticker Symbol (e.g., AAPL, TSLA, MSFT):", value="$AAPL").strip()

# Input for API Bearer Token
bearer_token = "AAAAAAAAAAAAAAAAAAAAAD5OxQEAAAAAXI1jaL%2FDeiCB6yERuuax5dIm%2BuU%3DtHW0CzBCgwgHX7nQgrCRbHlFNYsfaDnEmmLBkhnrTC8XmymcHV"

# Function to fetch tweet counts
def fetch_tweet_counts(query, start_time, end_time, bearer_token):
    """
    Fetch tweet counts using Twitter API v2 'Tweet Counts' endpoint.
    """
    url = "https://api.twitter.com/2/tweets/counts/recent"
    headers = {"Authorization": f"Bearer {bearer_token}"}
    params = {"query": query, "granularity": "day", "start_time": start_time, "end_time": end_time}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        tweet_count = sum([entry["tweet_count"] for entry in data.get("data", [])])
        return tweet_count
    else:
        st.error(f"Error {response.status_code}: {response.text}")
        return None

# Button to fetch tweet counts
if st.button("Fetch Tweet Counts"):
    if not ticker or not bearer_token:
        st.error("Please enter both a ticker symbol and your Twitter API Bearer Token.")
    else:
        try:
            # Define time periods
            end_time = (datetime.utcnow() - timedelta(seconds=10)).isoformat("T") + "Z"
            one_day_ago = (datetime.utcnow() - timedelta(days=1)).isoformat("T") + "Z"
            seven_days_ago = (datetime.utcnow() - timedelta(days=7)).isoformat("T") + "Z"
            thirty_days_ago = (datetime.utcnow() - timedelta(days=30)).isoformat("T") + "Z"

            # Define query
            query = f"{ticker} -is:retweet"

            # Fetch tweet counts
            st.write("Fetching tweet counts...")
            one_day_count = fetch_tweet_counts(query, one_day_ago, end_time, bearer_token)
            seven_day_count = fetch_tweet_counts(query, seven_days_ago, end_time, bearer_token)
            thirty_day_count = fetch_tweet_counts(query, thirty_days_ago, end_time, bearer_token)

            # Display results
            if one_day_count is not None and seven_day_count is not None and thirty_day_count is not None:
                st.success("Tweet counts fetched successfully!")
                data = {
                    "Time Period": ["Last 1 Day", "Last 7 Days", "Last 30 Days"],
                    "Tweet Count": [one_day_count, seven_day_count, thirty_day_count]
                }
                df = pd.DataFrame(data)
                st.table(df)

        except Exception as e:
            st.error(f"An error occurred: {e}")




