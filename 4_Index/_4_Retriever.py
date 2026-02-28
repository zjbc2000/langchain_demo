# 从langchain_community.document_loaders模块导入TextLoader类，用于加载文本文件
from langchain_community.document_loaders import TextLoader

# 从langchain.text_splitter模块导入CharacterTextSplitter类，用于分割文本
from langchain.text_splitter import CharacterTextSplitter

# 从langchain_community.vectorstores模块导入FAISS类，用于创建和管理向量数据库
# 需要安装faiss  pip install faiss-cpu
from langchain_community.vectorstores import FAISS

# 从langchain_community.embeddings模块导入OllamaEmbeddings类，用于生成文本嵌入向量
from langchain_ollama import OllamaEmbeddings


# 加载文本文件
loader = TextLoader("./pku.txt", encoding="utf8")
# 读取文件内容并创建文档对象
documents = loader.load()
print(f"documents--》{documents}")

# 创建文本分割器，设置每个片段大小为100字符，无重叠
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
# 将文档分割成多个文本片段
texts = text_splitter.split_documents(documents)
print(f"texts--》{texts}")
print(f"len(texts)--》{len(texts)}")

# 初始化嵌入模型，使用指定的模型进行文本嵌入
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

# 使用文本片段和嵌入模型创建FAISS向量数据库
db = FAISS.from_documents(texts, embeddings)
# 创建检索器，设置搜索参数k为1，即返回最相关的1个文档
retriever = db.as_retriever(search_kwargs={"k": 1})
print("retriever--->", retriever)

# 使用检索器查找与查询“北京大学什么时候成立的”相关的文档
docs = retriever.invoke("1937年北京大学发生了什么？")
print(docs)