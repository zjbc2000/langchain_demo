'''
1. 字符切割器
'''
from langchain.text_splitter import CharacterTextSplitter

# 初始化CharacterTextSplitter对象，指定分割参数
text_splitter = CharacterTextSplitter(
    separator=" ",  # 空格分割，但是空格也属于字符
    chunk_size=5,  # 每个文本块的大小
    chunk_overlap=1,  # 相邻文本块的重叠字符数
)

# 示例代码，演示如何使用split方法按指定字符分割字符串
# print("a b c d e f".split('c'))
# 一句分割
# 将单个字符串按空格分割成指定大小的文本块列表
a = text_splitter.split_text("a b c d e f")
print(a)

# 多句话分割（文档分割）
# 将多个字符串按空格分割成指定大小的文本块列表，构成文档
texts = text_splitter.create_documents(["a b c d e f", "e f g h"], )
print(texts)


'''
2. 语义切分器
'''
# 需要安装spacy  pip install spacy
from langchain.text_splitter import SpacyTextSplitter


#cmd终端下载spacy模型  python -m spacy download en_core_web_sm
text_splitter = SpacyTextSplitter(
    chunk_size=50,  # 每个块最大 50 个字符
    chunk_overlap=10,  # 块之间重叠 10 个字符
    pipeline='en_core_web_sm'  # 使用英文模型
)
text = """
This is a sample text. It contains multiple sentences.
Here is another paragraph. It has some more sentences.
This is the final paragraph with additional text.
"""
docs = text_splitter.split_text(text)
# docs = text_splitter.create_documents([text])
print('docs--->', docs)
for i, chunk in enumerate(docs):
    print(f"Chunk {i + 1}: {chunk}")


'''
3. 递归切分器
'''
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],
    chunk_size=30,
    chunk_overlap=5
)
text = """
This is a sample text. It contains multiple sentences.
Here is another paragraph. It has some more sentences.
This is the final paragraph with additional text.
"""
docs = text_splitter.split_text(text)
# docs = text_splitter.create_documents([text])
print('docs--->', docs)
print('=' * 80)