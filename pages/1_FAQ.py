import streamlit as st

def faq_accordion(question, answer):
    st.markdown(
        f"""
        <details>
            <summary>{question}</summary>
            <p>{answer}</p>
        </details>
        """,
        unsafe_allow_html=True,
    )

def main():
    st.title("Stock Trading FAQ Page")

    # Custom CSS for accordions
    st.markdown(
        """
        <style>
            details {
                border-radius: 10px;
                background-color: #f9f9f9;
                margin-bottom: 20px;
                box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
            }
            summary {
                font-weight: bold;
                font-size: 20px;
                padding: 15px 20px;
                cursor: pointer;
                outline: none;
                list-style: none;
                color: #ffffff;
                background-color: #4CAF50; /* Green color */
                border-radius: 10px;
                transition: background-color 0.3s;
                position: relative;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            summary::-webkit-details-marker {
                display: none;
            }
            summary:after {
                content: "+";
                font-size: 24px;
                position: absolute;
                right: 20px;
                transition: transform 0.3s;
            }
            details[open] summary:after {
                transform: rotate(45deg);
            }
            summary:hover {
                background-color: #45a049; /* Darker green color on hover */
            }
            p {
                margin: 0;
                padding: 20px;
                font-size: 18px;
                color: #333333;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    faq_accordion("Is it safe to trade online or are there risks in trading online?", "Online trading carries risks like any other form of investment. It's essential to understand market dynamics, research companies, and use risk management strategies to mitigate potential losses.")

    faq_accordion("What is the difference between Stock and Share?", "Stock and share are often used interchangeably, but they have distinct meanings. Stock refers to ownership in a corporation, while a share represents a unit of ownership in a company's stock.")

    faq_accordion("Where Do I Find Stock Related Information?", "You can find stock-related information on financial news websites, stock market apps, company websites, and financial statements. Additionally, brokerage platforms provide access to real-time stock quotes, charts, and analysis tools.")

    faq_accordion("How Would You Choose Stock For Your Portfolio?", "Choosing stocks for your portfolio involves thorough research and analysis. Consider factors such as the company's financial health, growth prospects, industry trends, and valuation metrics. Diversification across different sectors can also reduce risk.")

    faq_accordion("What Are Blue-Chip Stocks?", "Blue-chip stocks are shares of well-established, financially stable, and reputable companies with a history of reliable performance. They are typically leaders in their industries and often pay dividends to shareholders.")

    faq_accordion("What is Market Volatility?", "Market volatility refers to the degree of variation in the prices of securities or indexes within a market. High volatility indicates rapid and significant price fluctuations, while low volatility suggests more stable price movements.")

    faq_accordion("What Are Dividends?", "Dividends are payments made by a corporation to its shareholders, usually in the form of cash or additional shares. They represent a portion of the company's profits and are typically distributed regularly, providing income to investors.")

    faq_accordion("What Are the Different Order Types in Stock Trading?", "Common order types in stock trading include market orders, limit orders, stop orders, and trailing stop orders. Each type has its own characteristics and is used to execute trades under specific conditions.")

    faq_accordion("What Is Short Selling?", "Short selling is a trading strategy where an investor sells borrowed securities with the expectation that the price will decline. The investor aims to buy back the securities at a lower price, return them to the lender, and profit from the difference.")

    faq_accordion("How Can I Manage Risk in Stock Trading?", "Risk management strategies in stock trading include setting stop-loss orders, diversifying your portfolio, conducting thorough research, avoiding emotional decision-making, and being prepared to accept losses as part of the trading process.")

if __name__ == "__main__":
    main()
