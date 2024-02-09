import os

import azure.cognitiveservices.speech as speechsdk

from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from langchain.llms import AzureOpenAI

from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain_experimental.agents.agent_toolkits import create_csv_agent

from dotenv import load_dotenv

load_dotenv()

# OPENAI_API_KEY  = os.getenv("OPENAI_API_KEY")
# OPENAI_API_TYPE  = os.getenv("OPENAI_API_TYPE")
# OPENAI_API_VERSION  = os.getenv("OPENAI_API_VERSION")
# OPENAI_API_BASE  = os.getenv("OPENAI_API_BASE")
# CHAT_MODEL = os.getenv("CHAT_MODEL")
# CHAT_MODEL_DEPLOYMENT_NAME  = os.getenv("CHAT_MODEL_DEPLOYMENT_NAME")

# EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL")
# EMBEDDINGS_MODEL_DEPLOYMENT_NAME = os.getenv("EMBEDDINGS_MODEL_DEPLOYMENT_NAME")

OPENAI_API_KEY = "6b7202a499884f3193b3f4acc2b074fb"
OPENAI_API_TYPE = "azure"
OPENAI_API_VERSION = "2023-07-01-preview"
OPENAI_API_BASE = "https://openai-poc-app-dev.openai.azure.com/"
CHAT_MODEL = "gpt-35-turbo"
CHAT_MODEL_DEPLOYMENT_NAME = "GenpactGpt"
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
    query = query + ". Make the answer Concise in 3 lines"
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

def Speak_text_azure(text):
    SPEECH_KEY = 'a991d83e4f7d4861bd6707133c9db66a'
    SPEECH_REGION = 'eastus'
    print('Speaker called')
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
    
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Get text from the console and synthesize to the default speaker.
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()