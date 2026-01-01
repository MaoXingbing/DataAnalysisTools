import os


from langchain_community.chat_models import ChatTongyi
from dotenv import load_dotenv


load_dotenv()

llm=ChatTongyi(
    model='qwen-plus',
    api_key=os.getenv('DASHSCOPE_API_KEY')
)

