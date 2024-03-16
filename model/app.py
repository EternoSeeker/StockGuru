import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Streamlit app title
st.title('AlphaVantage Data')

# Symbol input form
symbol_input = st.text_input('Enter Symbol:')

# Submit button
if st.button('Submit'):
    # API URL for daily data
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol_input}&apikey=5EJNPQV0T263M9MG'

    # API request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        time_series_data = data.get('Time Series (Daily)', {})

        # Extracting specific entries from the JSON data
        extracted_entries = []
        for date, entry in time_series_data.items():
            open_price = entry.get('1. open', 'N/A')
            high_price = entry.get('2. high', 'N/A')
            low_price = entry.get('3. low', 'N/A')
            close_price = entry.get('4. close', 'N/A')

            # Append the extracted entries as a dictionary
            extracted_entries.append({
                'Date': date,
                'Open': open_price,
                'High': high_price,
                'Low': low_price,
                'Close': close_price
            })

        # Create a DataFrame from the extracted entries
        df = pd.DataFrame(extracted_entries)

        # Convert 'Date' column to datetime
        df['Date'] = pd.to_datetime(df['Date'])

        # Plotting
        plt.figure(figsize=(10, 6))
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plt.plot(df['Date'], df['Close'], marker='o', linestyle='-')
        plt.title('Closing Prices Over Time')
        plt.xlabel('Date')
        plt.ylabel('Closing Price')
        plt.grid(True)
        plt.xticks(rotation=45)

        # Set y-axis ticks at 20%, 40%, 60%, 80%, and 100% of the y-axis range
        y_min, y_max = plt.gca().get_ylim()
        y_ticks = [y_min + (y_max - y_min) * pct for pct in [0.2, 0.4, 0.6, 0.8, 1.0]]
        plt.gca().set_yticks(y_ticks)

        st.pyplot()

        # Display the DataFrame
        st.write(df)
    else:
        st.error('Failed to fetch data')