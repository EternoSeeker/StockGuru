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

    stock_keywords = ["stocks", "finance", "investment", "market", "trading"]

    for i in range(1, 7):
        with cols[(i - 1) % 3]:
            image_url = get_image_url(random.choice(stock_keywords))
            display_news_card(f"Stock Market News {i}", f"This is the content of Stock Market News {i}.", f"https://example.com/news{i}", image_url)


if __name__ == "__main__":
    main()
