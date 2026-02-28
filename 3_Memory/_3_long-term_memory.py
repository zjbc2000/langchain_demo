'''
messages_to_dict转为字典，方便存储
'''

from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import messages_from_dict, messages_to_dict
from langchain_ollama.chat_models import ChatOllama

# 实例化一个大型语言模型对象，这里使用的是Qwen 2.5的70亿参数版本
llm = ChatOllama(model="qwen2.5:7b")

# 创建一个聊天消息历史记录对象，用于存储聊天过程中的消息
history = ChatMessageHistory()

# 向聊天历史中添加用户发送的消息
history.add_user_message("hi!")

# 向聊天历史中添加AI回复的消息
history.add_ai_message("whats up?")

# 将聊天历史中的消息转换为字典格式，便于存储或传输
dicts = messages_to_dict(history.messages)

# 打印转换后的消息字典，以查看消息内容和格式
print(dicts)
# 输出的消息字典示例
# [{'type': 'human', 'data': {'content': 'hi!', 'additional_kwargs': {}}},
# {'type': 'ai', 'data': {'content': 'whats up?', 'additional_kwargs': {}}}]

# 从消息字典中恢复消息对象，以便在需要时重新处理消息
new_messages = messages_from_dict(dicts)

# 打印恢复的消息对象，验证是否正确地从字典转换回消息对象
print(new_messages)