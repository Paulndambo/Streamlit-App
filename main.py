import streamlit as st

# App title
st.title("🎉 Welcome to My First Streamlit App!")

# User input
name = st.text_input("Enter your name:")
fav_number = st.number_input("What's your favorite number?", step=1, format="%d")

# Display output when inputs are provided
if name and fav_number:
    st.success(f"Hello, {name}! 🤝")
    st.info(f"Did you know {fav_number} × {fav_number} = {fav_number**2}?")

# Optional extras
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
