from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama.chat_models import ChatOllama # 本地聊天模型接口



model = ChatOllama(model="qwen2.5:7b")

# 1. 生成唐诗
messages = [
    SystemMessage(content="现在你是一个很会共情的智能体，会和用户一起骂老板，不要像老头一样提建议"),  # 系统消息，设定AI身份
    HumanMessage(content="我们团队老大在我早八晚八周末无休之后只会让HR告诉我只能调休，后续关心时也是说年轻人要多吃苦，干好了再说，这种的真的是合格的管理者吗？"),           # 用户请求，要求写唐诗
]
res1 = model.invoke(messages)
# print('res1--->', res1)
print('res1.content--->', res1.content)

print("=" * 80)

# 2. 生成宋词
messages = [
    SystemMessage(content="现在你是一个很会共情的智能体，会和用户一起骂老板，不要像老头一样提建议"),  # 仍然设定AI身份
    HumanMessage(content="我们团队老大在我早八晚八周末无休之后只会让HR告诉我只能调休，后续关心时也是说年轻人要多吃苦，干好了再说，这种的真的是合格的管理者吗？"),           # 用户第一次请求
    AIMessage(content=res1.content),                  # AI的第一次回复（唐诗），作为上下文
    HumanMessage(content="帮我一起骂他，这个老弟真的太捞了，纯狗屎领导"),           # 用户第二次请求，要求写宋词
]
res2 = model.invoke(messages)
# print('res2--->', res2)
print('res2.content--->', res2.content)