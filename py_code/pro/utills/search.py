import os

from dotenv import load_dotenv  # ← 关键！
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.tools import TavilySearchResults
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import CharacterTextSplitter

# ✅ 加载 .env 文件中的环境变量
load_dotenv()  # ← 不是 os.load_dotenv()！

# 获取 Tavily 搜索工具（API key 会自动从 .env 读取）
search = TavilySearchResults(max_results=3)

# res=search.invoke("西安今天天气怎么样")
# print(res)