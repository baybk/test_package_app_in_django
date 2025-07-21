from setuptools import setup, find_packages

setup(
    name="test_package_app",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=4.2,<5.0",
    ],
    author="Bay Nguyen",
    author_email="baybknguyen@gmail.com",
    description="Test package app for Django project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/baybk/test_package_app_in_django.git",
    license="MIT",
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)