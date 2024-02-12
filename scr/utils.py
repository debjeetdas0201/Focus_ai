import os
import time
import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.llms import AzureOpenAI

from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

from dotenv import load_dotenv

import streamlit as st

load_dotenv()

# OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
# OPENAI_API_TYPE  = os.getenv("OPENAI_API_TYPE")
# OPENAI_API_VERSION  = os.getenv("OPENAI_API_VERSION")
# OPENAI_API_BASE  = os.getenv("OPENAI_API_BASE")
# CHAT_MODEL = os.getenv("CHAT_MODEL")
# CHAT_MODEL_DEPLOYMENT_NAME  = os.getenv("CHAT_MODEL_DEPLOYMENT_NAME")

# EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL")
# EMBEDDINGS_MODEL_DEPLOYMENT_NAME = os.getenv("EMBEDDINGS_MODEL_DEPLOYMENT_NAME")

OPENAI_API_KEY = "b7d5aa82d15a4b99a1c730f681ec2bbc"
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-07-01-preview"
OPENAI_API_BASE = "https://hmh-digitalhub-azure-openai.openai.azure.com/"
CHAT_MODEL = "gpt-35-turbo"
CHAT_MODEL_DEPLOYMENT_NAME = "gpt-35-turbo"
EMBEDDINGS_MODEL = "text-embedding-ada-002"
EMBEDDINGS_MODEL_DEPLOYMENT_NAME = "text-embedding-ada-002"

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")


model_chat = AzureChatOpenAI(
    openai_api_base=OPENAI_API_BASE,
    openai_api_version=OPENAI_API_VERSION,
    deployment_name=CHAT_MODEL_DEPLOYMENT_NAME,
    model_name = CHAT_MODEL,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type="azure")


model_basic = AzureOpenAI(
    openai_api_base=OPENAI_API_BASE,
    openai_api_version=OPENAI_API_VERSION,
    deployment_name=CHAT_MODEL_DEPLOYMENT_NAME,
    model_name = CHAT_MODEL,
    openai_api_key=OPENAI_API_KEY,
    openai_api_type="azure")




def for_general_conversation(query):
    query = query + ". Make the answer Concise in 1 lines"
    response = model_chat([HumanMessage(content=query)])
    response = list(response)[0][1]
    print(response)
    return response


def QnA(query, data_path):
    agent = create_csv_agent(
        model_basic,
        data_path,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
    return agent.run(query)

SPEECH_KEY = 'a991d83e4f7d4861bd6707133c9db66a'
SPEECH_REGION = 'eastus'

# Set up Azure Speech-to-Text and Text-to-Speech credentials
speech_key = SPEECH_KEY
service_region = "eastus"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
# Set up Azure Text-to-Speech language 
speech_config.speech_synthesis_language = "en-US"

# Set up the voice configuration
speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Define the text-to-speech function
def text_to_speech(text):
    
    try:
        placeholder = st.image('static/Bot.gif')
        result = speech_synthesizer.speak_text_async(text).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Text-to-speech conversion successful.")
            return True
        else:
            print(f"Error synthesizing audio: {result}")
            return False
    except Exception as ex:
        print(f"Error synthesizing audio: {ex}")
        return False
    finally:
        placeholder.empty()


def speechrecognition(): 
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        placeholder = st.image('static/Human.gif')
        print("Listening.....") 
        r.pause_threshold = 2
        audio = r.listen(source, 0,6)
    try:
        print("Recogizing....")
        query = r.recognize_google(audio) 
        return query.lower()
    except sr.UnknownValueError:
        print("Unable to understand")
    except sr.RequestError as e:
        print("Unable to provide required output".format(e))
    finally:
        placeholder.empty()

