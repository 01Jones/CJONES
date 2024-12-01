# fred API 49dc69fb7e224d27e8cd2f5b4830ac9f
# Nasdaq API KtkauE_-pic1EFrCBFb4

# app.py

import streamlit as st
import pandas as pd





# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.write("Use this sidebar to navigate.")
menu = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

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

# Sidebar
st.sidebar.header("Navigation")

# User Input
st.header("User Input Form")
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Thanks for visiting.")

# Display a chart
st.header("Sample Chart")
data = {"Category": ["A", "B", "C"], "Values": [10, 20, 30]}
st.bar_chart(data)

