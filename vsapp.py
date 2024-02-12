from scr.voice_main import activate_conv_ai
from scr.utils import text_to_speech
import streamlit as st
from PIL import Image
import cv2
import time
from scr.camera import video_frame_callback
import base64

image1 = Image.open('static/logo.jpeg')
png_logo = Image.open('static/png_logo.png')

st.set_page_config(
        page_title="CORA AI",
        page_icon=image1,
        #layout="wide",
)



def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

add_bg_from_local('static/background.jpg')


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        st.image(png_logo)
    with col3:
        st.write("")



def voice_caller():
    while True:
        try:
            exit_bool = activate_conv_ai()
            if exit_bool == True:
                break
        except Exception as e:
            print(e)
            continue



cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
FRAME_WINDOW = st.image([])
placeholder = st.image('static/face1.gif')
time.sleep(3)
while True:
    ret, frame = cam.read()
    if not ret:
        st.error("Failed to capture frame from camera")
        st.info("Please turn off the other app that is using the camera and restart app")
        st.stop()
    name = video_frame_callback(frame)
    #Display name and ID of the person
    if name is not None:
        placeholder.empty()
        placeholder = st.image('static/Check.gif')
        time.sleep(3)
        cam.release()
        placeholder.empty()
        placeholder = st.image('static/Bot.gif')
        placeholder.empty()
        text_to_speech(f"Hey {name}, How can I assist you?")
        voice_caller()
        placeholder.empty()
        placeholder = st.image('static/loader.gif')
        time.sleep(10)
        placeholder.empty()
        placeholder = st.image('static/face1.gif')
        cam = cv2.VideoCapture(0)