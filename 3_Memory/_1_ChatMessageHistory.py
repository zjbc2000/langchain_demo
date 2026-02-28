from langchain_community.chat_message_histories import ChatMessageHistory

# 创建一个ChatMessageHistory实例，用于管理聊天消息历史
history = ChatMessageHistory()

# 向聊天历史中添加用户的提问消息
history.add_user_message("在吗？")

# 向聊天历史中添加AI的回复消息
history.add_ai_message("有什么事?")

# 打印当前的聊天历史记录
print(history.messages)