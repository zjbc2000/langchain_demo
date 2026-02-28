# 本脚本演示了如何使用LangChain的不同文档加载器加载文本文件，并对加载结果进行简单处理。
# 包含详细注释和方法参数说明，便于理解和扩展。

# 1. 使用TextLoader加载结构化文本文件
# -------------------------------------------------
# 安装pymupdf模块（如需加载PDF）: pip install pymupdf
from langchain_community.document_loaders import PyMuPDFLoader

# 导入TextLoader类，用于加载结构化文本文件
from langchain_community.document_loaders import TextLoader

# TextLoader参数说明:
# - file_path (str): 要加载的文本文件路径
# - encoding (str, 可选): 文件编码格式，默认为"utf8"
# 例如: TextLoader("example.txt", encoding="utf8")
# loader = TextLoader("衣服属性.txt", encoding="utf8")
# 如需加载PDF文件，可使用如下方式（需安装pymupdf）:
loader = PyMuPDFLoader("test.pdf")

# 使用TextLoader加载文档，返回一个Document对象列表
docs = loader.load()

# 打印加载的文档内容（Document对象列表）和文档数量
print("TextLoader 加载结果：")
print(docs)
print("文档数量:", len(docs))
print("=" * 80)

# 提取第一个文档的前4个字符内容并打印
# Document对象的page_content属性为文档正文内容
a = docs[0].page_content[:4]
print("第一个文档前4个字符:", a)


print("=" * 80)  # 分隔线，区分不同加载方式

# 2. 使用UnstructuredLoader加载非结构化文件
# -------------------------------------------------
# 安装依赖:
# pip install unstructured
# pip install langchain_unstructured
from langchain_unstructured import UnstructuredLoader
import os

# 设置环境变量，指定最大线程数（可选，提升大文件处理性能）
os.environ["NUMEXPR_MAX_THREADS"] = "24"

# UnstructuredLoader参数说明:
# - file_path (str): 要加载的文件路径（支持多种格式，如txt、pdf、docx等）
# - encoding (str, 可选): 文件编码格式，默认为"utf8"
# 例如: UnstructuredLoader("example.txt", encoding="utf8")
loader = UnstructuredLoader("衣服属性.txt", encoding="utf8")
# 需要安装unstructured[pdf]模块  pip install unstructured[pdf]
# loader = UnstructuredLoader("test.pdf", encoding="utf8")

# 使用UnstructuredLoader加载文档，返回一个Document对象列表
docs = loader.load()

# 打印加载的文档内容（Document对象列表）和文档数量
print("UnstructuredLoader 加载结果：")
print(docs)
print("文档数量:", len(docs))

# 提取第一个文档的前4个字符内容并打印
a = docs[0].page_content[:4]
print("第一个文档前4个字符:", a)