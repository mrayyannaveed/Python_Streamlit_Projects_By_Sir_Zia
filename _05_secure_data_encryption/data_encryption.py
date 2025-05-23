import streamlit as st
import hashlib 
from cryptography.fernet import Fernet

# --- SESSION-BASED KEY MANAGEMENT ---
if "Key" not in st.session_state:
    st.session_state.Key = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.Key)
else:
    st.session_state.cipher = Fernet(st.session_state.Key)

# --- Global In-Memory Store ---
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# --- Helper Functions ---
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text, passkey):
    return st.session_state.cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)

    for key, value in st.session_state.stored_data.items():
        if value["encrypted_data"] == encrypted_text and value["passkey"] == hashed_passkey:
            return st.session_state.cipher.decrypt(encrypted_text.encode()).decode()
        
    st.session_state.failed_attempts += 1
    return None

# --- Streamlit App Layout ---
st.set_page_config(page_title="Secure Data Encryption System", page_icon="🔐", layout="wide")
st.title("🔒 Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# --- Pages ---
if choice == "Home":
    st.subheader("Welcome to the Secure Data Encryption System")
    st.write("This system allows you to securely store and retrieve sensitive data using unique passkeys.")

elif choice == "Store Data":
    st.subheader("Store Data Securely")
    user_data = st.text_area("Enter your data here:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_data = encrypt_data(user_data, passkey)
            st.session_state.stored_data[hashed_passkey] = {
                "encrypted_data": encrypted_data,
                "passkey": hashed_passkey
            }
            st.success("✅ Data encrypted and stored successfully!")
            st.code(encrypted_data, language="text")
        else:
            st.error("⚠️ Both fields are required")         

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data Securely")
    encrypted_text = st.text_area("Enter the encrypted text:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_data(encrypted_text, passkey)

            if decrypted_text:
                st.success("✅ Data decrypted successfully!")
                st.code(decrypted_text, language="text")
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")

                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to login page.")
                    st.session_state.page = "Login"
                    st.rerun()
        else:
            st.error("⚠️ Both fields are required")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin1234":
            st.session_state.failed_attempts = 0
            st.success("✅ Reauthorized successfully! You can now retrieve data.")
            st.rerun()
        else:
            st.error("❌ Incorrect password!")
