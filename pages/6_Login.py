from pymongo import MongoClient
import streamlit as st
import hashlib

if "isUserLoggedIn" not in st.session_state:
    st.session_state["isUserLoggedIn"] = False
    st.session_state["userDetails"] = {}

# Connect to your MongoDB instance
if st.session_state["isUserLoggedIn"] == False:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

client = MongoClient(st.secrets["connection_string"])
db = client['stock_recommender']  # Replace 'your_database_name' with your actual database name
users = db['users']



# Assuming MongoDB connection setup and variables are defined here

if st.button("Login"):
    # Hash the password using SHA256
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Find a user with the given username and password
    user = users.find_one({"name": username, "hashedPassword": hashed_password})

    if user:
        # Exclude the hashed password from the details to be stored in session
        user_details = {
            "name": user["name"],
            "email": user["email"],
            "preferences": user.get("preferences", {})
        }
        # Store the user details in session state
        st.session_state["userDetails"] = user_details
        st.session_state["isUserLoggedIn"] = True
        st.markdown(f"<p style='color:green'>Welcome {username}!</p>", unsafe_allow_html=True)
        st.switch_page("/pages/7_Portfolio.py")
    else:
        st.markdown(f"<p style='color:red'>Invalid username or password</p>", unsafe_allow_html=True)

# Add a link to the registration page
st.markdown("Don't have an account? Register here.")
if st.button("Register"):
    st.switch_page("/pages/5_Register.py")

