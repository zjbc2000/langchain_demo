from langchain_ollama.llms import OllamaLLM  # 本地大语言模型接口



model = OllamaLLM(model="qwen2.5:7b")
result = model.invoke("刚到一个没有网的地方上班，现需摸鱼，帮我生成三个摸鱼的要点")
print("result--->", result)