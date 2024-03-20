import requests
import pandas as pd
import streamlit as st

# Custom CSS for fancy design
st.markdown(
    """
    <style>
    .full-width {
        width: 100%;
    }
    .btn-submit {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 4px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('Real-Time Stock Performance Analysis')
symbol_input = st.text_input('Enter Symbol:', key='symbol_input', placeholder='e.g AAPL')

# Add a dropdown menu for time series interval
time_series_interval = st.selectbox('Select Time Series Interval', ['Daily', 'Weekly', 'Monthly'])

if st.button('Submit', key='submit_btn'):
    if time_series_interval == 'Daily':
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey=DNT3T50QF2PQ4ZDZ'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            time_series_data = data.get(f'Time Series ({time_series_interval})', {})

            extracted_entries = []
            for date, entry in time_series_data.items():
                open_price = entry.get('1. open', 'N/A')
                high_price = entry.get('2. high', 'N/A')
                low_price = entry.get('3. low', 'N/A')
                close_price = entry.get('4. close', 'N/A')
                extracted_entries.append({
                'Date': date,
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price
                })

            # Create DataFrame with specified column names
            columns = ['Date', 'Close']
            df = pd.DataFrame(extracted_entries, columns=columns)

            # Convert 'Date' column to datetime format
            df['Date'] = pd.to_datetime(df['Date'])
            df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

            st.write("Closing Prices Over Time:")
            st.line_chart(df.set_index('Date')['Close'])
            df1= pd.DataFrame(extracted_entries)
            st.dataframe(df1)

    elif time_series_interval == 'Weekly':
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol={symbol_input}&apikey=DNT3T50QF2PQ4ZDZ'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            time_series_data = data.get(f'Weekly Time Series', {})

            extracted_entries = []
            for date, entry in time_series_data.items():
                open_price = entry.get('1. open', 'N/A')
                high_price = entry.get('2. high', 'N/A')
                low_price = entry.get('3. low', 'N/A')
                close_price = entry.get('4. close', 'N/A')
                extracted_entries.append({
                'Date': date,
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price
                })

            # Create DataFrame with specified column names
            columns = ['Date', 'Close']
            df = pd.DataFrame(extracted_entries, columns=columns)

            # Convert 'Date' column to datetime format
            df['Date'] = pd.to_datetime(df['Date'])
            df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

            st.write("Closing Prices Over Time:")
            st.line_chart(df.set_index('Date')['Close'])
            df1= pd.DataFrame(extracted_entries)
            st.dataframe(df1)

    else:
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol_input}&apikey=DNT3T50QF2PQ4ZDZ'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            time_series_data = data.get(f'Monthly Time Series', {})

            extracted_entries = []
            for date, entry in time_series_data.items():
                open_price = entry.get('1. open', 'N/A')
                high_price = entry.get('2. high', 'N/A')
                low_price = entry.get('3. low', 'N/A')
                close_price = entry.get('4. close', 'N/A')
                extracted_entries.append({
                'Date': date,
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price
                })

            # Create DataFrame with specified column names
            columns = ['Date', 'Close']
            df = pd.DataFrame(extracted_entries, columns=columns)
            # Convert 'Date' column to datetime format
            df['Date'] = pd.to_datetime(df['Date'])
            df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

            st.write("Closing Prices Over Time:")
            st.line_chart(df.set_index('Date')['Close'])
            df1= pd.DataFrame(extracted_entries)
            st.dataframe(df1)
