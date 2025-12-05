import dotenv
import os
from langchain_core.messages import HumanMessage
from py_code.pro.utills import retriver
from langchain_openai import ChatOpenAI
from py_code.pro.utills.retriver import tools

dotenv.load_dotenv()

# 获取模型
model=ChatOpenAI(
    model="qwen-max",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

#将工具集绑定到模型
bind=model.bind_tools(tools=tools)
# for tool in tools:
#     print(tool.name)

#根据输入自动调用工具
messag=[HumanMessage(content='今天上海天气是啥')]
res=bind.invoke(messag)
print(f'content:{res.content}')
print(f"ToolCalls: {res.tool_calls}")