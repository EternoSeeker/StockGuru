import streamlit as st
import pandas as pd
import numpy as np
import requests

if "isUserLoggedIn" not in st.session_state:
    st.session_state["isUserLoggedIn"] = False

#if st.session_state["isUserLoggedIn"]:
# user_details = {
#    "name": st.session_state["userDetails"]["name"],
#    "email": st.session_state["userDetails"]["email"],
#    "preferences": st.session_state["userDetails"]["preferences"]
# }

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

with col4:
    preferred_stocks_option = st.multiselect(
    'Select your preferences',
    ['AAPL - Apple', 'MSFT - Microsoft', 'PFE - Pfizer', 'JNJ - Johnson & Johnson',
     'JPM - JPMorgan Chase', 'GS - Goldman Sachs', 'XOM - ExxonMobil', 'CVX - Chevron',
     'PG - Procter & Gamble', 'KO - Coca-Cola', 'AMZN - Amazon', 'WMT - Walmart',
     'TSLA - Tesla', 'F - Ford', 'T - AT&T', 'VZ - Verizon', 'DIS - Disney', 'NFLX - Netflix',
     'BA - Boeing', 'LMT - Lockheed Martin'])

if st.button("Save Preferences"):
    st.success("Preferences saved successfully!")
    st.subheader("Your Preferences")
    st.write(f"**Preferred Sectors:** {', '.join(preffered_sectors_option)}")
    st.write(f"**Risk Tolerance:** {risk_tolerance_option}")
    st.write(f"**Investment Goal:** {investment_goal_option}")
    st.write(f"**Preferred Stocks:** {', '.join(preferred_stocks_option)}")

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