from read import *
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains.retrieval_qa.base import RetrievalQA

# load vectordb from local storage
def load_vectordb(persist_directory="faiss_index"):

    vectordb = FAISS.load_local(persist_directory, embeddings=OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    return vectordb

# get relevant documents from vectordb according to topic
def retrieve_relevant_documents(vectordb, topic):

    query_results = vectordb.similarity_search(topic, k=10)
   
    return query_results


# generate articles by using OpenAI 
def generate_article(topic, context, vectordb):

    llm = ChatOpenAI(model="gpt-4o", temperature=0)

    retriever = vectordb.as_retriever()

    # Create the RAG (Retrieval Augmented Generation) chain
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

    # Define your query
    query = f"Write a comprehensive article about the following:\nTopic: {topic}\nContext: {context}"

    # Run the chain with the relevant docs and question
    article = rag_chain.run(query)
        
    return article