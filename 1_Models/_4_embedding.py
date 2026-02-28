from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(model='mxbai-embed-large', temperature=0)

res1 = model.embed_query('这是第一个测试文档')
print(res1)
print(len(res1))

print('=' * 80)

res2 = model.embed_documents(['这是第一个测试文档', '这是第二个测试文档'])
print(res2)
print(len(res2))
print(len(res2[0]))
print(len(res2[1]))