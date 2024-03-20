from openai import OpenAI
import streamlit as st

st.title("Stock Guru Chatbot")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

if len(st.session_state.messages) == 0:
    # First message from the bot asking about the domain of companies
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": """Welcome to our cutting-edge Conversational Recommender System for stock investments! Our goal is to provide you with personalized recommendations and real-time insights. To better assist you, could you please share the domain of companies you are interested in? Example: Technology, Healthcare""",
        }
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

tempString = ""
if prompt := st.chat_input("Message StockGuru..."):
    with st.chat_message("user"):
        st.markdown(prompt)

    user_message = {
        "role": "user",
        "content": prompt
    }

    if "domain" not in st.session_state:
        user_message["content"] = f"{prompt} is my domain preference, now ask me about my risk factor preference- high, medium, or low?"
        st.session_state["domain"] = prompt
    elif "risk_factor" not in st.session_state:
        user_message["content"] = f"{prompt} is my risk, now ask me about my investment term- short, medium, or long?"
        st.session_state["risk_factor"] = prompt
    elif "investment-term" not in st.session_state:
        user_message["content"] = f"{prompt} is my investment term, now ask me one more final question related to my preferences."
        st.session_state["investment-term"] = prompt
    elif "next-answer" not in st.session_state:
        if ["userDetails"] in st.session_state:
            current_user_stocks = st.session_state["userDetails"]["preferences"]["CurrentStocks"]
        st.session_state["next-answer"] = prompt
        user_message["content"] = f"{prompt} - These were my preferences, {current_user_stocks} are my current stock holdings in NASDAQ and NYSE. Suggest me a some good stock that might perform well from other domains for diversification. Also in subsequent prompts, Only answer my questions related to stocks and market."

    # Add the user's message to the list
    st.session_state.messages.append(user_message)
    # Generate the bot's response
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
        user_message["content"] = prompt
        length = len(st.session_state.messages)
        st.session_state.messages[length - 1] = user_message
        # Ensure the response is not already in the messages list
        if response not in [m["content"] for m in st.session_state.messages]:
            st.session_state.messages.append({"role": "assistant", "content": response})
