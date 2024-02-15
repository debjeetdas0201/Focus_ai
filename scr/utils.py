import os
import time
import azure.cognitiveservices.speech as speechsdk
import speech_recognition as sr
import pandas as pd
from dotenv import load_dotenv

import streamlit as st

load_dotenv()





# Function to get persona based on name
def get_persona(name):
    # Assuming your CSV file is named 'your_file.csv'
    file_path = 'data/persona.csv'

    # Read CSV into DataFrame
    df = pd.read_csv(file_path)

    person_row = df[df['Name'] == name]
    if not person_row.empty:
        return person_row['Persona'].values[-1]
    else:
        return 'cxo'

SPEECH_KEY = os.getenv("SPEECH_KEY")
SPEECH_REGION = os.getenv("SPEECH_REGION")

speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SPEECH_REGION)
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

