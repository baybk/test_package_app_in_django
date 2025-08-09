from setuptools import setup, find_packages

setup(
    name="dj7n_rag_chat_model",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=4.2,<5.0",
        "langchain>=0.3.26",
        "langchain-community>=0.3.26",
        "faiss-cpu>=1.11.0",
        "sentence-transformers>=4.1.0",
        "python-docx>=1.2.0",
        "pymupdf>=1.26.1",
        "langchain-google-genai>=2.0.10",
        "google-generativeai>=0.8.5"
    ],
    author="Bay Nguyen",
    author_email="baybknguyen@gmail.com",
    description="Rag Chat Model AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/baybk/dj7n_rag_chat_model.git",
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)