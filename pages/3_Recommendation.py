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
if prompt := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    tempString = prompt

    if "domain" not in st.session_state:
        st.session_state["domain"] = tempString
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": f"Thank you for sharing your interest in the {tempString} domain. Now, please specify the risk factor you are considering - high, medium, or low?",
            }
        )
    elif "risk_factor" not in st.session_state:
        st.session_state["risk_factor"] = tempString
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": f"Got it, your risk factor preference is {tempString}. Are you interested in any particular company within the {st.session_state['domain']} domain?",
            }
        )
    else:
        # Assuming user is specifying a particular company
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": f"Based on your preferences for the {st.session_state['domain']} domain and {st.session_state['risk_factor']} risk factor, I will provide insights and recommendations for {tempString}.",
            }
        )

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
        # Ensure the response is not already in the messages list
        if response not in [m["content"] for m in st.session_state.messages]:
            st.session_state.messages.append({"role": "assistant", "content": response})
