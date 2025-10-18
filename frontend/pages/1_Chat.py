import streamlit as st
import requests
from utils import mermaid_to_encoded_string

st.set_page_config(page_title="ER diagram AI",page_icon='https://cdn-icons-png.flaticon.com/64/11629/11629055.png')
st.sidebar.header("ER diagram AI 🟦─<🟧")

url=st.secrets['url'] or "http://localhost:8000/"

if 'chat_history' not in st.session_state:
    st.session_state.chat_history=[]
if "api_key" not in st.session_state:
    st.session_state.api_key=None
if 'model' not in st.session_state:
    st.session_state.model=''

model=st.sidebar.selectbox(label='Select your model',options=['llama-3.3-70b-versatile','llama-3.1-8b-instant',
'openai/gpt-oss-120b','openai/gpt-oss-20b'],index=0)

api_key = st.sidebar.text_input("API Key", type="password",placeholder="Groq API KEY (Optional!)")
if api_key:
    st.session_state.api_key=api_key

st.sidebar.markdown("---")  
if st.sidebar.button("New Conversation"):
    try:
        data=requests.post(url+"refresh",data={"session_id":"1"})
    except:
        pass
    st.session_state.chat_history = []

if model:
    st.session_state.model=model

if not st.session_state.chat_history:
    hist={"human":"",'ai':"Hi, I'm ERBot. What can I generate today?",'er_code':""}
    st.session_state.chat_history.append(hist)

import time
def response_generator(response):   
    for word in response:
        yield word
        time.sleep(0.01)


@st.cache_data
def generating_img(encoded_mermaid):
    try:
        url = f'https://mermaid.ink/img/{encoded_mermaid}?type=png'
        response = requests.get(url,timeout=20)
        return response.content
    except:
        return ""

for i in st.session_state.chat_history:
    for j in i:
        if j!='er_code':
            if i[j]:
                st.chat_message(j).write(i[j])
        if j=='er_code':
            if i[j].strip():
                st.image(i[j]) 

chat_input=st.chat_input(placeholder="Type your query")
if chat_input:
    st.chat_message('user').write(chat_input)
    with st.chat_message(name="ai"):
        placeholder = st.empty()
        placeholder.markdown("💭 _Thinking..._")
        try:
            data = requests.post(url+ 'chat', json={"user_input":chat_input,"model":st.session_state.model,'api_key':st.session_state.api_key if st.session_state.api_key else ''})
            data=data.json()
            if 'error' in data:
                st.error(f"Try for new conversation since Token Limit is exceeded")
            else:
                ai_response=data['ai_response']
                placeholder.empty()
                placeholder.write(response_generator(ai_response))
                res=data['er_code']
                hist={"human":chat_input,'ai':ai_response,'er_code':""}
                if res:
                    res = res.strip()
                    res=res.replace('`','')
                    encoded_mermaid = mermaid_to_encoded_string(res)
                    img_data = generating_img(encoded_mermaid)
                    if img_data:
                        st.image(img_data)
                        hist['er_code'] = img_data
                    else:
                        placeholder.write(response_generator("Error in generating the diagram   "))
                st.session_state.chat_history.append(hist)
        except requests.exceptions.RequestException as e:
            st.error(f"Try for new conversation since Token Limit or Rate Limit is exceeded! {e}")