from setuptools import setup, find_packages

setup(
    name="rag_usecase_openai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain",
        "openai",
        "tiktoken",
        "faiss-cpu",
        "langchain_experimental",
        "langchain[docarray]",
        "langchain-openai",
        "pypdf",
        "langchain-community"
    ]
)
