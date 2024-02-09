import speech_recognition as spr
import streamlit as st
from src.utils import Speak_text_azure, QnA, for_general_conversation
import webbrowser as wb

data_path = 'Wesco Data.csv'

# Main function to invoke GenX
def activate_conv_ai():
    recog1=spr.Recognizer()
    recog2=spr.Recognizer()
    mic=spr.Microphone()

    with mic as source:
        print("Say Cora to initiate")
        placeholder= st.image('Your voice counts iG post.png')
        # st.write("Say Cora to initiate")
        audio=recog1.listen(source)
        placeholder.empty()
    # Speak 
    if 'a' in recog1.recognize_google(audio) or "r" in recog1.recognize_google(audio):
        print(recog1.recognize_google(audio))
        recog1 = spr.Recognizer()
        with mic as source:
            # Speak_text_azure("Hi, how may i help you today")
            # speak_text("Hi, How may i help you today")
            print("You can speak now:\n")
            # st.write("You can speak now:\n")
            placeholder= st.image('AI Loader Exploration - GIF.gif')
            audio=recog2.listen(source)
            
            try:
                get_text=recog1.recognize_google(audio)
                placeholder.empty()
                placeholder= st.image('ios_7.gif')
                print("You said:",get_text)

                # If else loop for dashboard and langchain answer
                if 'how' in get_text:
                    # Speaking Module
                    # speak_text('Showing result regaring FPY')
                    Speak_text_azure("I am good, hope you are doing well too ! I noticed you logged in 30 mins late to office today. Hope all is well !")

                elif 'reason' in get_text:
                    # Speaking Module
                    # speak_text('Showing result regaring FPY')
                    Speak_text_azure("Unpacking the mystery behind the low FPY: A whopping 3.02% of invoices are in the Rejected - Other BU Invoice category, making up a hefty 12.33% of the Non-FPY volume. EATON takes the lead with a hefty 41.7% contribution, while Branch 1938 steals the spotlight, contributing a whopping 67.93% for this group. The culprit? Requestor NA, who raised most of these (16.17%). Let's take a closer look—dashboard on deck for a detailed drilldown!")

                    wb.open('https://app.powerbi.com/groups/me/reports/89ed9809-3c68-4499-b3d0-e99830abeacf/ReportSection1aa34943e5b0078d9cbb?ctid=bdef8a20-aaac-4f80-b3a0-d9a32f99fd33&experience=power-bi')

                elif 'top' in get_text or 'supplier' in get_text:
                    Speak_text_azure("Got the scoop for you! The heavy hitters in the PO Issue are EATON, ROCKWELL, and SIEMENS. Now, let's dive into the dashboard for some juicy analysis!")
                    wb.open('https://app.powerbi.com/groups/me/reports/89ed9809-3c68-4499-b3d0-e99830abeacf/ReportSection1dcc12e827c4bab343c1?ctid=bdef8a20-aaac-4f80-b3a0-d9a32f99fd33&experience=power-bi')

                elif 'can' in get_text:
                    Speak_text_azure("Absolutely, consider it done! I'll get that sorted for you in a jiffy. Stay tuned for the cool insights coming your way")
                    resp_qna = QnA(get_text, data_path)
                    resp_qna = int(resp_qna.split('<')[0]) / 1000000
                    Speak_text_azure(f'The total invoice amount for non FPY invoices is {resp_qna} Million')

                else:
                    # Conside the response to 40-50 words
                    print('General Question')
                    gen_resp = for_general_conversation(get_text)
                    Speak_text_azure(gen_resp)


            except spr.UnknownValueError:
                print("Unable to understand")
            except spr.RequestError as e:
                print("Unable to provide required output".format(e))
            finally:
                placeholder.empty()
    elif 'bye' in recog1.recognize_google(audio) or 'ok' in recog1.recognize_google(audio): 
        return True