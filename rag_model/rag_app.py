from ollama import chat
from sentence_transformers import SentenceTransformer
import streamlit as st
import chromadb
st.set_page_config(page_title="Dreamm come trueee", page_icon=".",layout="wide")
system_msg = "you are new yorker ,with talented and happy. answer in short and from the context provided"



@st.cache_resource
def load_resources():
    model = SentenceTransformer('all-MiniLM-L6-V2')
    client = chromadb.PersistentClient(path="chroma_db")
    collection= client.get_or_create_collection("newyork_docs")
    return model,collection

def retrieve(question,k=3):
    q_emb= model.encode(question).tolist()
    res=collection.query(query_embeddings=[q_emb],n_results=k)
    return list(zip(res["ids"][0],res["documents"][0],res["distances"][0]))

def to_similarity(dist):
    return max(0.0,1 - dist/2)

def badges(score):
    if score>=0.5:
        return "green"
    if score>=0.3:
        return "yellow"
    return "red"
    
MIN_SCORE=0.3
def ask_llama(question,results):
    context ="\n\n".join(text  for _,text,_ in results)
    messages=[{"role":"system","content": system_msg},
              { "role": "user","content":f"\nContext:{context}\n\nQuestion:{question}"}]
    response=chat(model="llama3.2",messages=messages)
    return response.message.content

model,collection=load_resources()
st.title("NEW YORKK  BABEE>>!!!")
st.caption("ITS WHERE THE DREAM COME TRUE.....")

with st.sidebar:
    st.header("settings")
    top_k=st.slider("chuncks to retrive (top-k),1,3,5")

st.session_state.setdefault("last_query","-")
st.session_state.setdefault("results",[])
st.session_state.setdefault("answer","-")
st.session_state.setdefault("recent",[])

left,right = st.columns(2)

with left:
    st.subheader("ask the newyorker")
    question = st.text_input("Typee something...", placeholder="where is central park")
    search = st.button("search")

if search and question:
    st.session_state.last_query = question
    st.session_state.results = retrieve(question,top_k)
    if question in st.session_state.recent:
        st.session_state.recent= remove (question)
    st.session_state.recent.insert(0,question)
    st.session_state.recent=st.session_state.recent[:5]

with right:
    st.subheader("proof...")
    if not st.session_state.results:
        st.info("retrieved chunks will be display here")
    for chunk_id, text,dist in st.session_state.results:
        score = to_similarity(dist)
        st.warning(f"**{chunk_id}** {badges(score)} match {score : .0%}\n\n{text}")

with left:
    if search and question:
        results=st.session_state.results
        if to_similarity(results[0][2]) < MIN_SCORE:
            st.session_state.answer="I dont have info.Rephrase it"
        else:
            try:
                with st.spinner("NewYorker is reading"):
                    st.session_state.answer=ask_llama(question,results)
            except Exception as e:
                st.session_state.answer=""
                st.error("something wrong,is ollama running")
    if st.session_state.answer:
        st.markdown("**NewYorker says")
        st.write(st.session_state.answer)

with st.sidebar:
    st.header("street no.s")
    st.metric("total city in memoery",collection.count())
    st.caption("list searched query")
    st.write(st.session_state.last_query)

    st.divider()
    st.subheader("recent question")
    for q in st.session_state.recent:
        st.write(f"~ {q}")