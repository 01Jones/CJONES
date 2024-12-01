# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4

# app.py

import streamlit as st
import pandas as pd


# Title and description
st.title("Welcome to My Streamlit App!")
st.write("This is a basic Streamlit app hosted on GitHub. Explore its features below!")

# Sidebar
st.sidebar.header("Navigation")
st.sidebar.write("Use this sidebar to navigate.")

# User Input
st.header("User Input Form")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Thanks for visiting.")

# Display a chart
st.header("Sample Chart")
data = {"Category": ["A", "B", "C"], "Values": [10, 20, 30]}
st.bar_chart(data)

