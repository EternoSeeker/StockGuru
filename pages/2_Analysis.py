import requests
import pandas as pd
import matplotlib.pyplot as plt
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

show_data = st.checkbox('Show DataFrame')

if st.button('Submit', key='submit_btn'):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey=5EJNPQV0T263M9MG'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        time_series_data = data.get('Time Series (Daily)', {})

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

        df = pd.DataFrame(extracted_entries)
        df['Date'] = pd.to_datetime(df['Date'])
        df['Close'] = pd.to_numeric(df['Close'], errors='coerce')

        if show_data:
            st.write("Closing Prices Over Time:")
            st.dataframe(df)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.figure(figsize=(10, 6))
        plt.plot(df['Date'], df['Close'], marker='o', linestyle='-')
        plt.title('Closing Prices Over Time', fontsize=18)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Closing Price', fontsize=14)
        plt.grid(True)
        plt.xticks(rotation=45)

        st.pyplot()
    else:
        st.error('Failed to fetch data')
