import streamlit as st
import pandas as pd
import numpy as np
import requests

if "isUserLoggedIn" not in st.session_state:
    st.session_state["isUserLoggedIn"] = False

st.subheader("User Profile")

if st.session_state["isUserLoggedIn"]:
    user_details = {
        "name": st.session_state["userDetails"]["name"],
        "email": st.session_state["userDetails"]["email"],
        "preferences": st.session_state["userDetails"]["preferences"]
    }
    user_details_container = st.container()
    # Display the user's name
    user_details_container.write(f"### Name: {user_details['name']}")
    # Display the user's email
    user_details_container.write(f"**Email:** {user_details['email']}")

listing_status_df = pd.read_csv("data/listing_status.csv")
symbols_df = listing_status_df["symbol"]

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
    current_investments = st.multiselect(
    'Select your current investments',
    symbols_df.tolist())


if st.button("Save Preferences"):
    st.success("Preferences saved successfully!")
    user_details = {
        "preferences": {
            "riskTolerance": risk_tolerance_option,
            "investmentGoal": investment_goal_option,
            "preferredSectors": preferred_sectors_option,
            "CurrentStocks": current_investments
        }
    }
    st.session_state["userDetails"] = user_details
    current_user_stocks = st.session_state["userDetails"]["preferences"]["CurrentStocks"]

    # Draw the multi-line chart
    chart_data = pd.DataFrame()  # Initialize an empty DataFrame

    for symbol_input in current_user_stocks:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey=5EJNPQV0T263M9MG'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            time_series_data = data.get('Time Series (Daily)', {})

            dates = []
            closes = []
            for date, entry in time_series_data.items():
                close_price = entry.get('4. close', 'N/A')
                dates.append(date)
                closes.append(float(close_price))

            chart_data[symbol_input] = closes

    chart_data = chart_data.set_index(pd.DatetimeIndex(dates))
    st.write("Here's how your current stock investments have been performing over the last 6 months:")

    st.line_chart(chart_data)

# if st.button("Logout"):
#    st.session_state["isUserLoggedIn"] = False
#    st.session_state["userDetails"] = {}
#    st.markdown(f"<p style='color:white'>You have been logged out</p>", unsafe_allow_html=True)
#    st.switch_page("/pages/6_Login.py")

    # Add any other relevant information or actions for the user's portfolio/profile