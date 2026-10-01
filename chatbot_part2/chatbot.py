from ollama import chat
import streamlit as st

st.set_page_config(page_title="the ollama",page_icon=">_<")
st.title("llama - The AI assistant")



personality="you are a senior startup funder. answer shortly and breifly"
personality_2="you are a hackathon judge."
if "history" not in st.session_state:
    st.session_state.history=[{"role":"system","content":personality}]
if "toast_msg" not in st.session_state:
    st.session_state.toast_msg=None
if st.session_state.toast_msg:
    st.toast(
        st.session_state.toast_msg[0],
        icon=st.session_state.toast_msg[1]
        )
    st.session_state.toast_msg=None

with st.sidebar:
    st.header("Controls")

    if st.button("chat clear",type="primary"):
        st.session_state.history=[{"role":"system","content":personality}]
        
        st.rerun()

    if st.button("change personality"):
        st.session_state.history[0]["content"]=personality_2
        st.session_state.toast_msg=("personality changed")
        st.rerun()

    if st.button("reset personality"):
        st.session_state.history[0]["content"]=personality
        st.session_state.toast_msg=("personality changed")
        st.rerun()


with st.chat_message("assistant"):
    st.write("hey,what's up!!!")

for msg in st.session_state.history[1:]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
question = st.chat_input("type something...")
if question:
    st.session_state.history.append({"role":"user","content":question})
    try:
        with st.chat_message("user"):
            st.write(question)
        
        response = chat(model="llama3.2",messages=st.session_state.history)

        with st.spinner("thinking"):
            response= chat(model="llama3.2",messages=st.session_state.history)

        reply=response["message"]["content"]
        st.session_state.history.append({"role":"assistant","content":reply})
        with st.chat_message("assistant"):
            st.write(reply)
    except Exception as e :
        st.write("ollama is not responding..!!!")





    

    

