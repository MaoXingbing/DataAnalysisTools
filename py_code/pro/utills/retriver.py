from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.tools import create_retriever_tool
from langchain_text_splitters import CharacterTextSplitter
from py_code.pro.utills import search

#RAG
paths=[
    '/home/maoxinbing/py_code/pro/db/情感文件.txt',
]

docs=[]
for path in paths:
    loader=TextLoader(file_path=path,encoding='utf-8')
    docs.extend(loader.load())

chunk=CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100,
)  #文件切分器

#文件切分
splitdocs=chunk.split_documents(docs)

#使用此模型将chunk变成向量
model=DashScopeEmbeddings(
    model="text-embedding-v2",
    dashscope_api_key='sk-edbd925ffc1f42aea4428b3d995ba30b',
)

#存储到向量数据库
db=FAISS.from_documents(documents=splitdocs,embedding=model)

#made retriever
retriever=db.as_retriever()
# path in local
# db.save_local("faiss_xiaorongmao_index")
# res=db.similarity_search("我好难过",k=2)
# for index in res:
#     print(index.page_content)

retriver_tool=create_retriever_tool(
    retriever=retriever,
    name='search_local',
    description="查找本地信息中的情感描述",
)

#创建工具集
tools=[retriver_tool, search.search]