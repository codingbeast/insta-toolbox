from setuptools import setup, find_packages

setup(
    name="insta-toolbox",
    version="0.1.0",
    author="raj kumar",
    author_email="advrter@gmail.com",
    description="A toolbox for creating Instagram shorts videos.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/codingbeast/insta-toolbox",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
)
