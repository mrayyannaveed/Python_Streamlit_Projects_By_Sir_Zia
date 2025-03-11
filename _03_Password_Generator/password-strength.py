import streamlit as st
import re

st.set_page_config(
    page_title="Password Strength Visualizer",
    page_icon="🔏",
    layout="wide"
)

st.title("🔐Password Strength Visualizer")
st.subheader("👉 **This is a simple password strength visualizer.**")
# st.markdown("🔑 **Is Your Password Strength Is Strong?**")
st.markdown("---")

st.markdown("## 📝 **How to use?**")
st.markdown("""
1. **Enter your password in the text box.**
2. **Press enter.**
3. **The result will be displayed.**
""")
st.markdown("---")

password = st.text_input("Enter your password", type="password", placeholder="Enter your password here...")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password must be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score +=1
    else:
        feedback.append("❌Password must contain at least one uppercase and lowercase characters.")

    if re.search(r"\d", password):
        score +=1
    else:
        feedback.append("❌Password must contain at least one number.")

    if re.search(r"[!@#$%&*]", password):
        score +=1
    else:
        feedback.append("❌Password must contain at least one special character (!@#$%&*).")

    if score == 4:
        feedback.append("✅Your password is strong.")
    elif score == 3:
        feedback.append("🟡Your password strength is medium.")
    elif score == 2:
        feedback.append("⚠️Your password strength is average make it stronger.")
    else:
        feedback.append("🔴Your password strength is weak make it more stronger.")


    if feedback:
        st.markdown("## Make Improvements to make *strong password strength*")
        for suggestion in feedback:
            st.markdown(suggestion)

else:
    st.info("🔍Please enter your password to check its strength.")

# st.markdown("---")
# st.markdown("## 📝 **How to make strong password?**")
# st.markdown("""
# 1. **Password must be at least 8 characters long.**
# 2. **Password must contain at least one uppercase letter.**
# 3. **Password must contain at least one lowercase letter.**
# 4. **Password must contain at least one number.**
# 5. **Password must contain at least one special character.**
# """)