from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlas
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

#Populate with your data!

# Atlas Connection
MONGO_URI = "mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = "sample_mflix"
COLLECTION_NAME = "embedded_movies"

client = MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Embeddings
openai_api_key = "your-openai-api-key"
embeddings_model = "text-embedding-ada-002"
embeddings = OpenAIEmbeddings(model=embeddings_model, openai_api_key=openai_api_key)

# Retriever
vectorstore = MongoDBAtlas(
    collection=collection,
    embedding=embeddings,
    index_name="vectorPlotIndex",
    fields=["plot_embedding", "year"],
)
retriever = vectorstore.as_retriever()

# LLM 
llm = ChatOpenAI(openai_api_key=openai_api_key, model_name="gpt-4")

# Create RAG Chain
qa_chain = RetrievalQA(llm=llm, retriever=retriever)

# Query
query = "Tell me about movies from the 1990s related to space exploration?"
response = qa_chain.run(query)

print("RAG Response:", response)
