import streamlit as st
import feedparser

def fetch_news():
    rss_url = "https://finance.yahoo.com/news/rss"
    feed = feedparser.parse(rss_url)
    if feed.get("status") == 200:
        return feed.entries
    else:
        st.warning("Failed to fetch news from Yahoo Finance.")
        return []

def display_news_card(news_title, news_summary, news_link):
    st.markdown(
        f"""
        <div class="news-card">
            <h3>{news_title}</h3>
            <p>{news_summary}</p>
            <a href="{news_link}" target="_blank">Read more</a>
        </div>
        """,
        unsafe_allow_html=True
    )

def main():
    st.title("Stock Market News")

    st.markdown(
        """
        <style>
            .news-card {
                width: 100%;
                border: 1px solid #e6e6e6;
                border-radius: 5px;
                padding: 10px;
                margin-bottom: 10px;
            }

            .news-card h3 {
                font-size: 18px;
                margin-bottom: 10px;
            }

            .news-card p {
                font-size: 14px;
                margin-bottom: 10px;
            }

            .news-card a {
                font-size: 14px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    news_list = fetch_news()
    for news in news_list:
        display_news_card(news.title, news.summary, news.link)

if __name__ == "__main__":
    main()
