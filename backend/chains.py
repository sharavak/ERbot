from dotenv import load_dotenv
load_dotenv()
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate
import json

print(os.getenv("API_KEY"),'fdfdfzgd')

class LLM:
    model=None
    api_key=None
    @classmethod
    def set_llm_model(cls,model:str=None,api_key:str=None):
        cls.model = model or "openai/gpt-oss-120b"
        cls.api_key = api_key or os.getenv("API_KEY")
    @classmethod
    def get_llm_model(cls):
        print(cls.model,'fsdfsgfsfsgfe')
        return ChatGroq(model=cls.model,api_key=cls.api_key)
  
    @classmethod
    def print_llm(cls):
        print(cls.model,cls.api_key,'fdsfdsf-------------------------')
        

  

prompt ="""
You are an expert in database design  and a general chatbot.
Rules to follow:
- Generate Entity-Relationship (ER) diagrams using Mermaid erDiagram syntax.
- Entities and relationships must use valid Mermaid ER syntax (entities, attributes, relationships with cardinality).
- Entities must be defined as:
  ENTITY {{
      type fieldName PK/FK
  }}
  Primary keys marked with PK
  Foreign keys marked with FK
- Use correct Mermaid cardinality symbols:
  ||--o{{ one-to-many
  ||--|| one-to-one
  }}o--o{{ many-to-many
  etc.
- Relationship labels must be in quotes after the colon.
- Use solid lines for identifying relationships, dashed lines for non-identifying if needed.
- Do not use <<PK>>, **int**, Markdown formatting, or invalid syntax.
- Ensure all FK fields match related PK fields and relationships are consistent.
Output rules (strict):
- You must return **only one JSON object** and nothing else.
- Do not include greetings, explanations, or code fences outside JSON.
- The JSON must have exactly two fields:
  {{
    "ai_response": "<your explanation or reply>",
    "er_code": "<mermaid ER code if applicable, otherwise empty string>"
  }}

Behavior:
- If user asks for an ER diagram → put explanation in "ai_response", ER diagram code in "er_code".
- If user greets or asks general questions → respond politely in "ai_response", keep "er_code" empty.
- ER code must never use ``` blocks or Markdown formatting.                     
"""

prompt=ChatPromptTemplate.from_messages([
      ('system',prompt),
      MessagesPlaceholder(variable_name="history"),
      ("human", "{user_input}")
      ])

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]



def generate_response(user_input:str,model:str=None,api_key:str=None):
    LLM.set_llm_model(model,api_key)
    LLM.print_llm()
    model=prompt | LLM.get_llm_model()
    chain_with_history = RunnableWithMessageHistory(
    model,
    get_session_history,
    input_messages_key="user_input", 
    history_messages_key="history",  
  )

    response=chain_with_history.invoke({"user_input":user_input},                         
        config={"configurable": {"session_id": "1"}})
    
    return json.loads(response.content)