
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/supervisor"

st.set_page_config(page_title="Multi-Agent AI", page_icon="🤖", layout="wide")

st.markdown("""
<style>
.main-title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#4F8BF9;
}
.subtitle{
text-align:center;
color:gray;
margin-bottom:20px;
}
.agent{
display:inline-block;
padding:4px 10px;
border-radius:15px;
background:#4F8BF9;
color:white;
font-size:13px;
margin-bottom:8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🤖 Multi-Agent AI Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>LangChain • FastAPI • Streamlit</div>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Control Panel")
    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.write("### Agents")
    st.write("🟣 Supervisor")
    st.write("🔵 Weather Agent")
    st.write("🟢 Calculator Agent")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        if m["role"]=="assistant":
            st.markdown("<div class='agent'>Supervisor</div>",unsafe_allow_html=True)
        st.markdown(m["content"])

prompt=st.chat_input("Ask something...")

if prompt:
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                r=requests.post(API_URL,json={"query":prompt},timeout=120)
                r.raise_for_status()
                data=r.json()
                answer=data.get("response","No response")
            except Exception as e:
                answer=f"Error: {e}"

            st.markdown("<div class='agent'>Supervisor</div>",unsafe_allow_html=True)
            st.markdown(answer)

    st.session_state.messages.append({"role":"assistant","content":answer})
