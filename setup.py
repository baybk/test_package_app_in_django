from setuptools import setup, find_packages

setup(
    name="dj7n_rag_chat_model",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=4.2,<5.0",
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