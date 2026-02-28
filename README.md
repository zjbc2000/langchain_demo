#### coding module:
1. Models: from langchain_ollama/transformers
2. Prompts: from langchain_**core**.prompts import PromptTemplate
3. Memory: from langchain_**community**.chat_message_histories import ChatMessageHistory
4. Index:
   1) loader(.loader()): 
                 from langchain_**unstructured** import UnstructuredLoader
                 from langchain_community.document_loaders import TextLoader
   2) splitter(.split_text()): 
                 from langchain.**text_splitter** import CharaterTextSplitter
   3) VectorStore: (l2/ip/cosine) from langchain_community.vectorstores import Chroma
   4) retriever: 需要传入参数query, k, 调用封装好的方法; 
       如 FAISS 的 as_retriever + invoke;
       如 Chroma 的 similarity_search_with_score;


#### tips:
1. 请手动安装ollama以部署qwen2.5:7B模型，或用huggingface下载模型用transformers库导入
2. 初步安装langchain依赖：
pip install langchain langchain_community
3. langchain_community里也有不少好东西，可按注释进行依赖安装
