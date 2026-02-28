# 导入OllamaEmbeddings类，用于生成文本嵌入
from langchain_ollama import OllamaEmbeddings
# 导入CharacterTextSplitter类，用于分割文本
from langchain.text_splitter import CharacterTextSplitter
# 导入Chroma类，用于创建和管理文本嵌入的向量数据库
# 需要安装chromadb  pip install chromadb
from langchain_community.vectorstores import Chroma

# 读取pku.txt文件内容，该文件包含了北京大学的相关信息
with open('./pku.txt', encoding='utf-8') as f:
    state_of_the_union = f.read()

# 创建CharacterTextSplitter实例，用于将文本分割成大小为50、无重叠的块
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=10)
# 使用text_splitter分割文本
# texts = text_splitter.split_text(state_of_the_union)
texts = text_splitter.create_documents([state_of_the_union])
# 打印分割后的文本块和文本块数量
print(f'texts-->{texts}')
print(f'len(texts)-->{len(texts)}')

# 创建OllamaEmbeddings实例，使用预训练的mxbai-embed-large模型生成文本嵌入
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# 使用分割后的文本和生成的文本嵌入创建Chroma向量数据库
# documents: 需要存入向量数据库的文档列表
# embedding: 用于将文档转换为向量的嵌入模型
# collection_name: Chroma集合的名称，用于区分不同的向量集合
# collection_metadata: 集合的元数据，这里通过 "hnsw:space" 指定相似度度量方式（如 "cosine", "l2", "ip"）, 默认是"cosine"
# persist_directory: 向量数据库的持久化存储目录，便于后续加载和管理
# docsearch = Chroma.from_texts(texts, embeddings)
docsearch = Chroma.from_documents(documents=texts,
                                  embedding=embeddings,
                                  collection_metadata={"hnsw:space": "cosine"})

# 定义查询问题，寻找1937年北京大学发生的重要事件
query = "1937年北京大学发生了什么？"
# 使用向量数据库进行相似性搜索，找到与查询最相关的文档
# docs = docsearch.similarity_search(query, k=1)
# 返回的是距离最近的文档, 值越小越相似
docs = docsearch.similarity_search_with_score(query, k=2)
# 打印搜索结果和结果数量
print(f'docs==>{docs}')
print(f'len(docs)==>{len(docs)}')