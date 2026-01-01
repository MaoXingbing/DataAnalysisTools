from typing import Annotated, TypedDict, List

from langchain_community.chat_models import ChatTongyi
from langchain_core.caches import InMemoryCache
from langchain_core.messages import AnyMessage, HumanMessage
# from langgraph.config import get_stream_writer
from operator import add
from langgraph.graph import StateGraph,START, END
from langgraph.checkpoint import MemorySaver
#from langgraph.checkpoint.memory import InMemorySaver



#TODO:构建大模型
llm=ChatTongyi(
    model='qwen-plus',
    api_key=''
)
class State(TypedDict):
    message:Annotated[list[AnyMessage],add]
    type:str

def supervisor_node(state:State):
    print(">>>进入supervisor_node节点")
    # writer=get_stream_writer()
    # '''writer 的作用：是流式输出的写入工具，用于在节点执行时实时输出日志、状态等信息，让工作流执行过程更透明；'''
    # writer({"node",">>>进入supervisor_node节点"})
    prompt='''一个。专业的客服助手负责对用户的问题进行分类，并将任务分给其他 agent 执行。
           如果用户的问题适合旅游路线规划相关的，那就返回 travel。
           如果用户的问题是希望找一个笑话，那就返回 joke。
           如果用户的问题是希望对一个对联，那就返回 couplet。
           如果是其他的问题，返回 other，除了这几个选项外，不要返回任何其他的内容。
           '''
    prompts=[
        {'role':'system','content':prompt},
        {'role':'user','content':state['message'][0]}
    ]

    return {"message":[HumanMessage(content="我暂时无法回答这个问题")],"type":"other"}

def other_node(state:State):
    print(">>>进other_node节点")
    # writer = get_stream_writer()
    # writer({"node", ">>>进入other_node节点"})
    return {"message":[HumanMessage(content="我暂时无法回答这个问题")],"type":"other"}

def couplet_node(state:State):
    print(">>>进入couplet_node节点")
    # writer=get_stream_writer()
    # writer({"node",">>>进入couplet_node节点"})
    return {"message":[HumanMessage(content="我暂时无法回答这个问题")],"type":"couplet"}

def joke_node(state:State):
    print(">>>进入joke_node节点")
    # writer=get_stream_writer()
    # writer({"node",">>>进入joke_node节点"})
    return {"message":[HumanMessage(content="我暂时无法回答这个问题")],"type":"joke"}

def travel_node(state:State):
    print(">>>进入travel_node节点")
    # writer=get_stream_writer()
    # writer({"node",">>>进入travel_node节点"})
    return {"message":[HumanMessage(content="我暂时无法回答这个问题")],"type":"travel"}


#条件路由
def routing_func(state:State):
    if state['type']=='travel':
        return 'travel_node'
    elif state['type']=='joke':
        return 'joke_node'
    elif state['type']=='couplet':
        return 'couplet_node'
    elif state['type']=='END':
        return 'END'
    else:
        return 'other_node'


#构建图
builder = StateGraph(State)

#添加节点
builder.add_node('supervisor_node',supervisor_node)
builder.add_node('travel_node',travel_node)
builder.add_node('joke_node',joke_node)
builder.add_node('couplet_node',couplet_node)
builder.add_node("other_node",other_node)

#添加边
builder.add_edge(START,'supervisor_node')
builder.add_conditional_edges('supervisor_node',routing_func,['supervisor_node','travel_node','joke_node','couplet_node',"other_node"])
builder.add_edge('travel_node','supervisor_node')
builder.add_edge('joke_node','supervisor_node')
builder.add_edge('couplet_node','supervisor_node')
builder.add_edge('other_node','supervisor_node')



#构建图
checkpointer=MemorySaver()
graph=builder.compile(checkpointer=checkpointer)

#执行任务测试的代码
if __name__ == "__main__":
    config={
        "configurable":{
            "thread_id":"1"
        }
    }

    for chunk in graph.stream({"message":["给我讲一个笑话"]}
                  ,config
                  ,stream_mode="custom"):
        print(chunk)





