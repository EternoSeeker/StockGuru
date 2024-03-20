import streamlit as st
import pandas as pd
import numpy as np
import requests

if "isUserLoggedIn" not in st.session_state:
    st.session_state["isUserLoggedIn"] = False

st.subheader("User Profile")

# Create a container to hold the user details
user_details_container = st.container()

# # Display the user's name
# user_details_container.markdown(f"### Name: {user_details['name']}")

# # Display the user's email
# user_details_container.markdown(f"**Email:** {user_details['email']}")

# Update preferences
col1, col2 = st.columns(2)

with col1:
    preferred_sectors_option = st.multiselect(
    'Select domains to invest in:',
    ['Technology', 'Healthcare', 'Finance', 'Energy', 'Consumer Goods', 'Retail', 'Automotive', 'Telecommunications', 'Entertainment', 'Aerospace and Defense'])

with col2:
   risk_tolerance_option = st.selectbox(
    "Select your risk tolerance",
    ("Low", "Medium", "High"),
   )

col3, col4 = st.columns(2)

with col3:
    investment_goal_option = st.selectbox(
     "Select your investment goal",
     ("Short-term", "Medium-term", "Long-term"),
    )

listing_status_df = pd.read_csv("data/listing_status.csv")
symbols_df = listing_status_df["symbol"]

with col4:
    current_investments = st.multiselect(
    'Select your current investments',
    symbols_df.tolist())

if st.button("Save Preferences"):
    st.success("Preferences saved successfully!")
    user_details = {
        "name": st.session_state["userDetails"]["name"],
        "email": st.session_state["userDetails"]["email"],
        "preferences": st.session_state["userDetails"]["preferences"]
    }
    st.session_state["userDetails"] = user_details

symbol_input = st.text_input('Enter Symbol:', key='symbol_input', placeholder='e.g AAPL')
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey=5EJNPQV0T263M9MG'

if st.session_state["isUserLoggedIn"]:
    user_details = {
        "name": st.session_state["userDetails"]["name"],
        "email": st.session_state["userDetails"]["email"],
        "preferences": st.session_state["userDetails"]["preferences"]
    }

# Display the user's preferences
# user_details_container.markdown("**Preferences:**")
# for preference, value in user_details["preferences"].items():
#    user_details_container.markdown(f"- {preference}: {value}")

# if st.button("Logout"):
#    st.session_state["isUserLoggedIn"] = False
#    st.session_state["userDetails"] = {}
#    st.markdown(f"<p style='color:white'>You have been logged out</p>", unsafe_allow_html=True)
#    st.switch_page("/pages/6_Login.py")

    # Add any other relevant information or actions for the user's portfolio/profile