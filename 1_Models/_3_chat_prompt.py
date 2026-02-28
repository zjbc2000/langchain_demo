from langchain_ollama.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate



template_str = (
    "您是一位专业的鲜花店文案撰写员。\n"
    "对于售价为 {price} 元的 {flower_name} ，您能提供一个吸引人的简短描述吗？\n"
    "#"
)
prompt_emplate = ChatPromptTemplate.from_template(template_str)
prompt = prompt_emplate.format_messages(price='50', flower_name=["玫瑰"])
print('prompt-->', prompt)

# temperature=0表示输出完全确定（无随机性），适合需要稳定输出的场景
model = ChatOllama(model="qwen2.5:7b", temperature=0)
result = model.invoke(prompt)
print('result.content--->', result.content)