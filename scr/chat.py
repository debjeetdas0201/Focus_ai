import os
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()

OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
OPENAI_API_TYPE  = os.getenv("OPENAI_API_TYPE")
OPENAI_API_VERSION  = os.getenv("OPENAI_API_VERSION")
OPENAI_API_BASE  = os.getenv("OPENAI_API_BASE")
CHAT_MODEL = os.getenv("CHAT_MODEL")
CHAT_MODEL_DEPLOYMENT_NAME  = os.getenv("CHAT_MODEL_DEPLOYMENT_NAME")

EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL")
EMBEDDINGS_MODEL_DEPLOYMENT_NAME = os.getenv("EMBEDDINGS_MODEL_DEPLOYMENT_NAME")

prompt_template_manager = """Answer the manager's questions based on the below context and data. If the context doesn't contain any relevant information to the question, search from the internet and answer the query.
    Keep the response conscise in 2 line. Only use relevant data.

    {context}

    Question: {question}
    Answer:"""

prompt_template_agent = """Answer the agent's questions based on the below context and data. If the context doesn't contain any relevant information to the question, search from the internet and answer the query.
    Keep the response conscise in 2 line. Only use relevant data.

    {context}

    Question: {question}
    Answer:"""

prompt_template_cxo = """Answer the cxo's questions based on the below context and data. If the context doesn't contain any relevant information to the question, search from the internet and answer the query.
    Keep the response conscise in 2 line. Only use relevant data.

    {context}

    Question: {question}
    Answer:"""

def load_changes(persona):
    if persona == "Agent":
        prompt_template = prompt_template_agent
    elif persona == "Manager":
        prompt_template = prompt_template_manager
    else:
        prompt_template = prompt_template_cxo
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain_type_kwargs = {"prompt": PROMPT}

    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("faiss_index/faiss_index_"+ persona.lower(), embeddings)
    retriever = db.as_retriever()
    global qa 
    model = AzureChatOpenAI(
        openai_api_type = OPENAI_API_TYPE,
        openai_api_base = OPENAI_API_BASE,
        openai_api_version = OPENAI_API_VERSION,
        openai_api_key = OPENAI_API_KEY,
        model_name = CHAT_MODEL,
        deployment_name = CHAT_MODEL_DEPLOYMENT_NAME,
        temperature=0.7
        )
    qa = ConversationalRetrievalChain.from_llm(
        model, 
        retriever=retriever, 
        return_source_documents=False,
        combine_docs_chain_kwargs=chain_type_kwargs
        )

def add_text(history, text):
    history = history + [(text, None)]
    return history, ""

def bot(history):
    response = infer(history[-1][0], history)
    history[-1][1] = response
    return history

def bots(question, history = ""):
    response = infer(question, history)
    return response

def infer(question, history):
    
    res = []
    for human, ai in history[:-1]:
        pair = (human, ai)
        res.append(pair)
    
    chat_history = res
    query = question
    result = qa({"question": query, "chat_history": chat_history})
    return result["answer"]
