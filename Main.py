# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4

# app.py

import streamlit as st
import pandas as pd
import requests
import twikit
import tweepy

# Input your API credentials
api_key = st.text_input("5Od9JIeK9BDVnOjjgQvvSdVAh", type="password")
api_secret = st.text_input("djtjd1gRUvTki5YRLl006rGsjpQ3SzMJYfji317XvE1XYBSrrf", type="password")
access_token = st.text_input("744622183-PYWccpQMhkATqVZpERjasovNDcer3U54bdDuNRPY", type="password")
access_token_secret = st.text_input("GGJcu8ksG3lSrnlOa4vl3xWn7uFhD0eO1uyRA4Mwn08Vx", type="password")

#Bearer AAAAAAAAAAAAAAAAAAAAAD5OxQEAAAAAXI1jaL%2FDeiCB6yERuuax5dIm%2BuU%3DtHW0CzBCgwgHX7nQgrCRbHlFNYsfaDnEmmLBkhnrTC8XmymcHV


# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.write("Use this sidebar to navigate.")
menu = st.sidebar.radio("Go to", ["Home", "X/Twitter", "Pending"])


#TWITTER
st.title("Twitter Tracker")
st.write("This app fetches the total number of tweets mentioning 'AAPL' in the last 7 days.")
if st.button("Fetch Tweet Count"):
    if not all([api_key, api_secret, access_token, access_token_secret]):
        st.error("Please provide all API credentials.")
    else:
        try:
            # Authenticate to Twitter
            auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
            api = tweepy.API(auth)
            
            # Fetch tweets using Tweepy Cursor
            query = "AAPL -filter:retweets"
            tweets = tweepy.Cursor(api.search_tweets, q=query, lang="en", result_type="recent").items(100)

            # Count tweets
            tweet_count = len(list(tweets))
            st.success(f"Total tweets mentioning 'AAPL' in the last 7 days: {tweet_count}")

        except Exception as e:
            st.error(f"An error occurred: {e}")











# Main content based on navigation selection
if menu == "Home":
    st.title("Home")
    st.write("Welcome to the Home page!")
elif menu == "About":
    st.title("About")
    st.write("This app demonstrates a basic sidebar navigation.")
elif menu == "Contact":
    st.title("Contact")
    st.write("Feel free to contact us at example@example.com.")








# Title and description
st.title("Welcome to My Streamlit App!")
st.write("This is a basic Streamlit app hosted on GitHub. Explore its features below!")

# User Input
st.header("User Input Form")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Thanks for visiting.")

# Display a chart
st.header("Sample Chart")
data = {"Category": ["A", "B", "C"], "Values": [10, 20, 30]}
st.bar_chart(data)

