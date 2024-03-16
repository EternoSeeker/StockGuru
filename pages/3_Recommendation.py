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
if prompt := st.chat_input("Message ChatGuru..."):
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
        user_message["content"] = f"{prompt} is my risk, now ask me about my specific Company preference."
        st.session_state["risk_factor"] = prompt
    elif "company" not in st.session_state:
        user_message["content"] = f"I would likely consider {prompt} as my company preference, you can ask me some more questions related to my preferences, and then suggest me stock to invest in."
        st.session_state["company"] = prompt

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
