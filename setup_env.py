import subprocess

command = [
    "pip3", "install", "langchain", "langchain_community", "langchain_core", 
    "langchain_openai", "langchain_mongodb", "pymongo", "pypdf"
]

subprocess.run(command)
