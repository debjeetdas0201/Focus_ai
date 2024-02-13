import streamlit as st
from PIL import Image
import numpy as np
import os
import pandas as pd
from cv2 import *

persona_data = pd.read_csv('data\persona.csv')

def Registration():
    """
    Add details
    
    """

    st.markdown('<p style="color:white;">CAPTURE YOUR IMAGE</p>', unsafe_allow_html=True)
    img_file_buffer = st.camera_input(label = "___________________")
    
    
    if img_file_buffer is not None:
        # To read image file buffer as a PIL Image:
        img = Image.open(img_file_buffer)

        # add a input text:
        st.markdown('<p style="color:white;">ENTER YOUR NAME</p>', unsafe_allow_html=True)
        user_name = st.text_input(label = "___________________")
        st.markdown('<p style="color:white;">SELECT YOUR PERSONA</p>', unsafe_allow_html=True)
        role_value = st.selectbox(label = "___________________",
                                options= ('CXO', 'Manager', 'Agent'), 
                                index = None,
                                placeholder= 'Choose an option',
                                label_visibility='collapsed')
        
        # saving the image in folder
        if user_name:
            photo_dir = 'faces'
            img.save(os.path.join(photo_dir,f"{user_name}.jpeg"))


        if role_value:
            temp_data = pd.DataFrame({'Name':[user_name], 'Persona': [role_value]})
            return temp_data


# try:
#     temp_data = Registration()
#     if temp_data is not None:
#         if st.button("Submit"):
#             persona_data  = pd.concat([persona_data , temp_data])
#                 # persona_data = persona_data.drop_duplicates()
#             persona_data.to_csv('data\persona.csv', index=False)
#             streamlit_js_eval(js_expressions="parent.window.location.reload()")

# except Exception as e:
#     print(e)
        


