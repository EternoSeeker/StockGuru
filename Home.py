import base64
import streamlit as st
import streamlit as st

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        width: 100vw;
        margin: 0;
        padding: 0;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('./data/images/background.jpg')

original_title = '<h1 style="font-family: sans-serif; color:white; font-size: 5rem;"> Stock-Guru 📈 </h1>'
st.markdown(original_title, unsafe_allow_html=True)

subheader1 = '<h2 style="font-family: sans-serif; color:white; font-size: 1.8rem;"> Your personalized stock recommendation system. </h2>'
st.markdown(subheader1, unsafe_allow_html=True)

description = '<h3 style="font-family: sans-serif; color:white; font-size: 1.1rem; font-weight: light;"> Whether you\'re a seasoned investor or just starting out, Our goal is to provide you with personalized recommendations and real-time insights to help you navigate the complex world of financial markets. Let\'s embark on this journey together, empowering you to make informed investment decisions tailored to your unique financial goals and risk profile. </h3>'
st.markdown(description, unsafe_allow_html=True)

# st.subheader("Your personalized stock recommendation system.")
# st.write(
#     """Whether you're a seasoned investor or just starting out, 
#          Our goal is to provide you with personalized recommendations and real-time insights to help you navigate the complex world of financial markets. 
#          Let's embark on this journey together, empowering you to make informed investment decisions tailored to your unique financial goals and risk profile."""
# )
