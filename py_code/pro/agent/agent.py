from langchain import hub
from py_code.pro.utills.retriver import tools
from py_code.pro.model.model import model
from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

prompt = hub.pull("hwchase17/openai-functions-agent")
print(prompt.messages)

 # 创建Agent对象
agent = create_tool_calling_agent(model, tools, prompt)
 # 创建AgentExecutor对象
agent_executor = AgentExecutor(agent=agent, tools=tools,verbose=True)
msg=agent_executor.invoke(
    {'input':'今天上海的天气是啥'}
)
print(msg)
