import streamlit as st

def show_guides():
    st.title("Useful Resources")

    # st.header("Useful Resources")
    st.write("🔎 **Seeking Alpha:**")
    st.write("A platform for stock market insights, analysis, and recommendations.")
    st.link_button("Visit Seeking Alpha", url="https://seekingalpha.com/")

    st.write("💰 **Value Investing:**")
    st.write("A website dedicated to value investing principles and strategies.")
    st.link_button("Visit Value Investing", url="https://valueinvesting.io/")

    st.write("💸 **MoneyControl:**")
    st.write("A leading financial platform in India for real-time stock quotes and market news.")
    st.link_button("Visit MoneyControl", url="https://www.moneycontrol.com/")

    st.subheader("Additional Resources")

    st.write("Here are some additional resources that might be helpful:")

    st.write("📚 Investopedia: A comprehensive encyclopedia of financial terms and concepts.")
    st.link_button("Visit Investopedia", url="https://www.investopedia.com/")

    st.write("🃏 The Motley Fool: A multimedia financial services company providing stock analysis and investment advice.")
    st.link_button("Visit The Motley Fool", url="https://www.fool.com/")

    st.write("💱 Yahoo! Finance: A popular platform for real-time stock quotes, news, and financial information.")
    st.link_button("Visit Yahoo! Finance", url="https://finance.yahoo.com/")

    st.write("📊 MarketWatch: A financial information website providing real-time market data and analysis.")
    st.link_button("Visit MarketWatch", url="https://www.marketwatch.com/")

if __name__ == "__main__":
    show_guides()