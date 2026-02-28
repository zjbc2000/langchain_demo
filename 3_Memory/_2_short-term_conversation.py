'''
conversation = RunnableWithMessageHistory()
'''

from langchain_ollama.chat_models import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage



llm = ChatOllama(model="qwen2.5:7b")

# 用于存储不同会话(session)的历史消息，key为session_id，value为ChatMessageHistory对象
history_dict = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    """
    获取指定session_id的消息历史对象，如果不存在则新建一个。

    参数:
        session_id (str): 会话的唯一标识符，用于区分不同用户或会话。

    返回:
        ChatMessageHistory: 与该session_id关联的消息历史对象。
    """
    if session_id not in history_dict:
        # 如果该session_id还没有历史，则新建一个ChatMessageHistory对象
        history_dict[session_id] = ChatMessageHistory()
    return history_dict[session_id]

# 创建带有消息历史管理的对话链
conversation = RunnableWithMessageHistory(
    runnable=llm,  # 指定底层大模型
    get_session_history=get_session_history,  # 指定获取历史的函数
)

# 指定本次对话的session_id，可用于区分不同用户或会话
session_id = "test-session"

# 第一轮对话：输入“周杰伦是谁?”
res1 = conversation.invoke(
    {"messages": [HumanMessage(content="周杰伦是谁?")]},  # 输入消息列表
    config={"configurable": {"session_id": session_id}},  # 配置会话ID
)
print(res1.content)  # 输出模型回复内容
print('history_dict--->', history_dict)
print("=" * 80)

# 第二轮对话：输入“给我推荐几首周杰伦的歌”
res2 = conversation.invoke(
    {"messages": [HumanMessage(content="给我推荐几首他的歌"), AIMessage(content=res1.content)]},
    config={"configurable": {"session_id": session_id}},
)
print(res2.content)
print('history_dict--->', history_dict)
print("=" * 80)

# 第三轮对话：提问“你刚才推荐的歌都是什么类型的?”
res3 = conversation.invoke(
    {"messages": [HumanMessage(content="你刚才推荐的歌都是什么类型的?"), AIMessage(content=res2.content)]},
    config={"configurable": {"session_id": session_id}},
)
print(res3.content)
print("=" * 80)
print(history_dict)
print(history_dict[session_id].messages)