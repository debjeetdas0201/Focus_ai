import streamlit as st
from scr.chat import bots, load_changes
from scr.utils import text_to_speech, speechrecognition
import webbrowser as wb


# Main function to invoke GenX
def activate_conv_ai():
        try:
            print("You can speak now:\n")
            get_text = speechrecognition()
            print("You said:",get_text)
            
            if get_text is None:
                pass
            else:
                gen_resp = bots(get_text)
                text_to_speech(gen_resp)

            if 'bye' in get_text and 'ok' in get_text:
                return True

        except Exception as e:
             print(e)