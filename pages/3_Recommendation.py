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
            "content": """Welcome to our cutting-edge Conversational Recommender System for stock investments!Our goal is to provide you with personalized recommendations and real-time insights.
                        To better assist you, could you please share the domain of companies you are interested in ?
                        Example: Technology, Healthcare""",
        }
    )
    with st.chat_message("assistant"):
        st.markdown(
            """Welcome to our cutting-edge Conversational Recommender System for stock investments!Our goal is to provide you with personalized recommendations and real-time insights.
                To better assist you, could you please share the domain of companies you are interested in ?
                Example: Technology, Healthcare"""
        )
else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("You:"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Second message from the bot asking about the risk factor
    if len(st.session_state.messages) == 1:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Great! Now, could you please specify the risk factor you are considering - high, medium, or low?",
            }
        )
        with st.chat_message("assistant"):
            st.markdown(
                "Great! Now, could you please specify the risk factor you are considering - high, medium, or low?"
            )
    # Third message from the bot asking about a specific company
    elif len(st.session_state.messages) == 2:
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "Sure! Lastly, could you please provide the name of the specific company you are interested in?",
            }
        )
        with st.chat_message("assistant"):
            st.markdown(
                "Sure! Lastly, could you please provide the name of the specific company you are interested in?"
            )

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
    st.session_state.messages.append({"role": "assistant", "content": response})
