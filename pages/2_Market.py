import streamlit as st
import random

def get_image_url(search_query):
    return f"https://source.unsplash.com/featured/?{search_query}"

def display_news_card(news_title, news_content, news_link, image_url):
    with st.container():
        st.image(image_url, use_column_width=True)
        st.subheader(news_title)
        st.write(news_content)
        st.markdown(f'[Read more]({news_link})')

def main():
    st.title("Stock Market News")

    cols = st.columns(3)

    # Dictionary to store hardcoded news details
    news_data = {
        "Musk's SpaceX building spy satellite network": {
            "content": "The $1.8 billion contract with the National Reconnaissance Office shows the extent of SpaceX's involvement in US intelligence and military projects and illustrates a deeper Pentagon investment into vast, low-Earth orbiting satellite systems aimed at supporting ground forces.",
            "link": "https://www.reuters.com/business/"
        },
        "Banks remain vulnerable a year after Credit Suisse's rescue": {
            "content": "A year after the banking crisis that felled Credit Suisse, authorities are still considering how to fix lenders' vulnerabilities - including in Switzerland, where the bank's takeover by rival UBS created a behemoth.",
            "link": "https://www.reuters.com/markets/europe/year-credit-suisses-rescue-banks-remain-vulnerable-2024-03-15/"
        },
        "Federal Reserve announces interest rate hike": {
            "content": "The Federal Reserve announced a 0.25% interest rate hike in response to rising inflation concerns, marking the first increase since 2023.",
            "link": "https://www.reuters.com/business/fed-holds-key-rate-overnight-repo-rate-steady-2024-03-16/"
        },
        "Amazon reports record-breaking holiday sales": {
            "content": "Amazon reported record-breaking holiday sales, with revenue surpassing expectations fueled by strong demand for online shopping.",
            "link": "https://www.businessinsider.com/amazon-holiday-sales-revenue-exceeds-expectations-2024-01"
        },
        "Apple announces launch of new product lineup": {
            "content": "Apple unveiled its latest product lineup, including the highly anticipated iPhone 15 and MacBook Pro with revolutionary features.",
            "link": "https://www.macrumors.com/2024/03/08/apple-announces-new-product-lineup/"
        },
        "Oil prices surge amid supply disruptions": {
            "content": "Oil prices surged to a seven-year high amid supply disruptions caused by geopolitical tensions and production cuts by major oil-producing countries.",
            "link": "https://www.reuters.com/business/oil-hits-7-yr-high-2024-03-14/"
        }
    }

    stock_keywords = ["stocks", "finance", "investment", "market", "trading","Banking"]

    for i, (news_title, news_details) in enumerate(news_data.items()):
        with cols[i % 3]:
            image_keyword = random.choice(stock_keywords)
            stock_keywords.remove(image_keyword)  # Remove the used keyword
            image_url = get_image_url(image_keyword)
            display_news_card(news_title, news_details["content"], news_details["link"], image_url)

if __name__ == "__main__":
    main()
