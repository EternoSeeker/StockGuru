import streamlit as st
import requests
from textblob import TextBlob

st.title("Market News")

# Function to fetch news data from the API
def fetch_news(symbols):
    url = "https://api.marketaux.com/v1/news/all"
    params = {
        "symbols": symbols,
        "filter_entities": True,
        "api_token": st.secrets["MARKETAUX_API_TOKEN"]
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        st.error("Failed to fetch news data.")
        return []

# Function to perform sentiment analysis
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"

# Get symbols from user input
symbols = st.text_input("Enter symbols (comma-separated):", value="AAPL")

# Fetch news data based on user input symbols
news_data = fetch_news(symbols)

# Display news data and sentiment analysis in the Streamlit app
if news_data:
    for news_item in news_data:
        st.subheader(f"Title: {news_item['title']}")
        st.write(f"Description: {news_item['description']}")
        st.link_button("Visit Site", news_item['url'])
        # st.write(f"URL: {news_item['url']}")
        st.image(news_item['image_url'], caption="Image", use_column_width=True)
        
        # Perform sentiment analysis
        sentiment = analyze_sentiment(news_item['description'])
        st.markdown(f"<span style='color:white; font-size:1.7rem;'>Sentiment: {sentiment}</span>", unsafe_allow_html=True)
        st.write("---")
else:
    st.write("No news data available.")