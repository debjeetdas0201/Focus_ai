import speech_recognition as spr
import streamlit as st
from scr.utils import Speak_text_azure, QnA, for_general_conversation, recognize_from_microphone
import webbrowser as wb


def activate_conv_ai():
    
    recog=spr.Recognizer()
    mic=spr.Microphone()    
    with mic as source:
        print('speak: ')
        audio=recog.listen(source, phrase_time_limit = 6 )
        try:
            get_text=recog.recognize_google(audio)
            print("You said:",get_text)

        except spr.UnknownValueError:
            print("Unable to understand")
        except spr.RequestError as e:
            print("Unable to provide required output".format(e))
        finally:    
            print("End of Process")