from src.voice_main import activate_conv_ai
# from src.utils import Speak_text_azure
import streamlit as st
from PIL import Image
# import cv2
# import time
# from src.camera import video_frame_callback
image1 = Image.open('favicon.ico')

st.set_page_config(
        page_title="CORA VA",
        page_icon=image1,
        #layout="wide",
)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


for i in range(0,100):
    while True:
        try:
            activate_conv_ai()
        except Exception as e:
            print(e)
            continue
        break

# def voice_caller():
#     while True:
#         try:
#             exit_bool = activate_conv_ai()
#             if exit_bool == True:
#                 break
#         except Exception as e:
#             print(e)
#             continue



# cam = cv2.VideoCapture(0)
# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# FRAME_WINDOW = st.image([])
# placeholder = st.image('68222ce7852a6b64cf2557d5bb501e95.gif')
# while True:
    # ret, frame = cam.read()
    # if not ret:
    #     st.error("Failed to capture frame from camera")
    #     st.info("Please turn off the other app that is using the camera and restart app")
    #     st.stop()
    # name = video_frame_callback(frame)
    # #Display name and ID of the person
    # if name is not None:
    #     cam.release()
    #     placeholder.empty()
    #     Speak_text_azure(f"Hey {name}, How can I assist you?")
        # voice_caller()
        # placeholder = st.image('ezgif-2-078cdcb3f1d3.gif')
        # time.sleep(30)
        # placeholder.empty()
        # placeholder = st.image('68222ce7852a6b64cf2557d5bb501e95.gif')
        # cam = cv2.VideoCapture(0)