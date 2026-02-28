from langchain_core.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_ollama.llms import OllamaLLM

# 初始化Ollama模型，用于后续的反义词生成任务
model = OllamaLLM(model="qwen2.5:7b")

# 定义示例数据，用于FewShot学习，帮助模型理解任务要求
examples = [
    {"word": "开心", "antonym": "难过"},
    {"word": "高", "antonym": "矮"},
]

# 定义示例模板，用于格式化每个示例数据
example_template = """
单词: {word}
反义词: {antonym}\n
"""

# 创建PromptTemplate对象，用于生成示例的提示
example_prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=example_template,
)
print('example_prompt--->', example_prompt)

# 创建FewShotPromptTemplate对象，用于生成包含任务说明、示例和待预测数据的完整提示
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="给出每个单词的反义词",
    suffix="单词: {input}\n反义词:",
    input_variables=["input"],
    example_separator="\n",
)
print('few_shot_prompt--->', few_shot_prompt)

# 格式化提示，用于获取特定单词的反义词
prompt_text = few_shot_prompt.format(input="粗")
# 打印格式化后的提示，以查看生成的提示内容
print('prompt_text--->', prompt_text)
print("*" * 80)
# 调用模型，传入格式化后的提示，以获取模型的响应
result = model.invoke(prompt_text)
print('result--->', result)