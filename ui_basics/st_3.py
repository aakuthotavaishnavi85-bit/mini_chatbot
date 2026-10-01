import streamlit as st
import time
st.set_page_config(page_title="chatbot app demo")

st.title("chatbot UI Demo ")

with st.chat_message("user"):
    st.write("hello from the user side!")

user_msg=st.chat_input("ask anything...")
    with st.chat_message("user"):
        st.write(user_msg)
    with st.chat_message("assistant"):
        with st.spinner("thinking.."):
            time.sleep(1.5)
        st.write(f"hey , you wrote: {user_msg},but i'm still in develpoment mode. i cant reply")



