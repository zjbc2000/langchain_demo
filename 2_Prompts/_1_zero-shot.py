from langchain_core.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM



model = OllamaLLM(model="qwen2.5:7b")

template = (
    "我的邻居姓{lastname}，他的妻子姓{wname}," 
    "他生了个儿子，结合两人的姓氏，给他儿子起个名字"
)

# 封装提示词
prompt = PromptTemplate(
    input_variables=["lastname", "wname"],
    template=template,
)

# format传数据
prompt_text = prompt.format(lastname="王", wname="李")
print(f"prompt_text-->{prompt_text}")

result = model.invoke(prompt_text)
print('result--->', result)
