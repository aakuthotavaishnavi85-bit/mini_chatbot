import streamlit as st

st.set_page_config(page_title="text input demo")
st.title("text input demo")

name = st.text_input("enter your name:",placeholder="e.g.aadi")
st.write(f"hello,{name}!")

secret = st.text_input("enter your password",type= "password")
st.write(f"your password has {len(secret)} characters")

comments=st.text_area("my additional comments?", height=150)
st.write(f"your wrote {len(comments)} character.")

if st.button("Submit"):
    st.write("Submitted!!!!")

show_message =st.checkbox("Do you want to proceed?")
if show_message:
    st.write("Done!!!,Have a nice day ")


