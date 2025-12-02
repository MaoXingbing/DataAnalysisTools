from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables import RunnableWithMessageHistory
from py_code.pro.agent.agent import agent_executor
from langchain_community.chat_message_histories import ChatMessageHistory

store={}

def get_session_history(session:str)->BaseChatMessageHistory:
    if session not in store:
        store[session]=ChatMessageHistory()

    return store[session]

agenthistory=RunnableWithMessageHistory(
    runnable=agent_executor,
    get_session_history=get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

response=agenthistory.invoke(
    {'input':'你好，我的名字是max'},
    config={"configurable":{"session_id":"123"}},
)
print(response)

response1=agenthistory.invoke(
    {'input':'我叫什么'},
    config={"configurable":{"session_id":"123"}},
)
print(response1)