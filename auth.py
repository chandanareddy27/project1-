import streamlit as st
import pandas as pd
import osimport hashlib
USER_FILE = "data/users.csv"
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
def init_user_store():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(USER_FILE):
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(USER_FILE, index=False)
def load_users():
    init_user_store()
    return pd.read_csv(USER_FILE)
def save_user(username, password):
    users = load_users()
    hashes = hash_password(password)
    users.loc[len(users)] = [username, hashed]
    users.to_csv(USER_FILE, index=False)
def login():
    if "user" in st.session_state:
        return
    st.markdown("##🔐 Authentication")
    tab_login, tab_register = st.tabs(["Login", "Register"])
    with tab_login:
        username = st.text_input("Username", key="login_us")
        password = st.text_input("password", type="password")

