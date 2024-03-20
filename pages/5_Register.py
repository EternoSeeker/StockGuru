from pymongo import MongoClient
import streamlit as st
import hashlib

# Connect to your MongoDB instance
client = MongoClient(st.secrets["connection_string"])
db = client['stock_recommender']  # Replace 'your_database_name' with your actual database name
users = db['users']

username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    
    # Check if the username or email already exists in the database
    existing_user = users.find_one({"$or": [{"name": username}, {"email": email}]})
    
    if existing_user:
        st.error("Username or Email already exists. Please try again with a different one.")
        # Clear the input fields
    else:
        # Hash the password using SHA256
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Insert a user document with hashed password and preferred stocks
        user_document = {
            "name": username,
            "email": email,
            "hashedPassword": hashed_password,  # Use the actual hashed password
            "preferences": {
                "riskTolerance": "",
                "investmentGoal": "",
                "preferredSectors": [],
                "CurrentStocks": []
            }
        }

        result = users.insert_one(user_document)
        st.success(f"Registered successfully!")
        st.switch_page("pages/6_Login.py")