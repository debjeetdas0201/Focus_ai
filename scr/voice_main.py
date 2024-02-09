import speech_recognition as spr
import streamlit as st
from src.utils import Speak_text_azure, QnA, for_general_conversation
import webbrowser as wb

data_path = 'Wesco Data.csv'

# Main function to invoke GenX
def activate_conv_ai():
    # recog1=spr.Recognizer()
    recog=spr.Recognizer()
    mic=spr.Microphone()

    # with mic as source:
    #         print("Say Cora to initiate")
    #         placeholder= st.image('Your voice counts iG post.png')
    #         # st.write("Say Cora to initiate")
    #         audio=recog1.listen(source)
    #         placeholder.empty()
    # # Speak 
    # if 'a' in recog1.recognize_google(audio) or "r" in recog1.recognize_google(audio):
    #     print(recog1.recognize_google(audio))
    #     recog1 = spr.Recognizer()
        
    with mic as source:
        # Speak_text_azure("Hi, how may i help you today")
        # speak_text("Hi, How may i help you today")
        print("You can speak now:\n")
        # st.write("You can speak now:\n")
        
        # placeholder= st.image('AI Loader Exploration - GIF.gif')
        audio=recog.listen(source, phrase_time_limit = 7)
        
        try:
            get_text=recog.recognize_google(audio)
            # placeholder.empty()
            # placeholder= st.image('ios_7.gif')
            print("You said:",get_text)
            
            # If else loop for dashboard and langchain answers
            if 'how' in get_text:
                # Speaking Module
                # speak_text('Showing result regaring FPY')
                Speak_text_azure("I am good, hope you are doing well too ! I noticed you logged in 45 mins late to office today. Hope all is well !")
            elif 'visit' in get_text or 'looks' in get_text:
                # Speaking Module
                # speak_text('Showing result regaring FPY')
                Speak_text_azure("You need to respond to Microsoft LSS proposal. I sent you minutes from the meeting you had with Paula on 14th January. Couple of actions aredue today. Also, replacement for Madhuri from you team is still not closed. Other than that, your day looks good. Your amber scores are down and you haven’tdone one on ones this week. Please confirm and I can block calendars for the same. Other than that dont forget to include Generative AI solutions, duplicatepayments and Smart Collect Celonis solutions while discussing with customers.")
            elif 'calendar' in get_text:
                # Speaking Module
                # speak_text('Showing result regaring FPY')
                Speak_text_azure("It's done, booked it for coming Wednesday basis availability !")
            elif 'suppliers' in get_text or 'reduction' in get_text:
                # Speaking Module
                # speak_text('Showing result regaring FPY')
                Speak_text_azure("Yes FPY has reduced since last week in Wesco and the main reasons are related to PO issues. Top suppliers contributing to this are  EATON,ROCKWELL, and SIEMENS. Let's take a closer look—dashboard on deck for a detailed drilldown!")
                wb.open('https://app.powerbi.com/groups/me/reports/89ed9809-3c68-4499-b3d0-e99830abeacf/ReportSection1dcc12e827c4bab343c1ctid=bdef8a20-aaac-4f80-b3a0-d9a32f99fd33&experience=power-bi')
            # elif 'reason' in get_text:
            #     # Speaking Module
            #     # speak_text('Showing result regaring FPY')
            #     Speak_text_azure("Unpacking the mystery behind the low FPY: A whopping 3.02% of invoices are in the Rejected - Other BU Invoice category, making up a hefty 1233% of the Non-FPY volume. EATON takes the lead with a hefty 41.7% contribution, while Branch 1938 steals the spotlight, contributing a whopping 67.93% for thisgroup. The culprit? Requestor NA, who raised most of these (16.17%). Let's take a closer look—dashboard on deck for a detailed drilldown!")
            #     wb.open('https://app.powerbi.com/groups/me/reports/89ed9809-3c68-4499-b3d0-e99830abeacf/ReportSection1aa34943e5b0078d9cbbctid=bdef8a20-aaac-4f80-b3a0-d9a32f99fd33&experience=power-bi')
            # elif 'top' in get_text or 'supplier' in get_text:
            #     Speak_text_azure("Got the scoop for you! The heavy hitters in the PO Issue are EATON, ROCKWELL, and SIEMENS. Now, let's dive into the dashboard for some juicyanalysis!")
            #     wb.open('https://app.powerbi.com/groups/me/reports/89ed9809-3c68-4499-b3d0-e99830abeacf/ReportSection1dcc12e827c4bab343c1ctid=bdef8a20-aaac-4f80-b3a0-d9a32f99fd33&experience=power-bi')
            # elif 'can' in get_text:
            #     Speak_text_azure("Absolutely, consider it done! I'll get that sorted for you in a jiffy. Stay tuned for the cool insights coming your way")
            #     resp_qna = QnA(get_text, data_path)
            #     resp_qna = resp_qna.split('<')[0]
            #     Speak_text_azure(f'Answer for {get_text} is {resp_qna}')
            elif 'bye' in recog.recognize_google(audio) and 'ok' in recog.recognize_google(audio):
                return True
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
            print("hello")
            # placeholder.empty()