# Share
Share Tempo

import streamlit as st
from PIL import Image
import cv2 
import numpy as np
import os
import sys
from hurry.filesize import size

#pip install hurry.filesize


def load_image(path):
    image = cv2.imread(path)
    return image

def welcome():
    
    st.title('Image Data Compression with AI')
    
    st.subheader('A simple app that shows different image compression algorithms. You can choose the options'
             + ' from the left.')
    
    st.image('logo.png',use_column_width=True)

def photo():
    st.header("Image Data Compression SIX-AM")
    
    if st.button('See Original Image'):
        
        original = Image.open('test.jpg')
        st.image(original, use_column_width=True)
        output = {"Original Image Size":original.size, "Image Size (bytes)": str(size(os.stat('test.jpg').st_size))}
        st.text_area(label="File Size",value=output,height = 150)
        
    file_path = "test.jpg"
    file = file_path.split('.jpg')[0]

    frame = Image.open(file_path)     #Input Test Image
    x = st.slider('Change Compression value',min_value = 0,max_value = 100)

    frame.save(f"result/compressed_{file}.jpeg",optimize = True,quality=x) 

    com_result = Image.open(f"result/compressed_{file}.jpeg")

    output_com = {"Compressed Image Dimension":com_result.size, "Image Size (bytes)":str(size(os.stat(f"result/compressed_{file}.jpeg").st_size)),
                    "Compression Ratio": str( round(int(os.stat(f"result/compressed_{file}.jpeg").st_size) * 100 / int(os.stat('test.jpg').st_size),2)) + " % of original image size" }
    st.text_area(label="Compressed File Size",value=output_com,height = 150)
    st.image(com_result, use_column_width=True,clamp = True)
    
   

def main():
    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome','Image Compression', 'Image Decompression', 'Face Detection', 'Feature Detection', 'Object Detection')
        )
            
    if selected_box == 'Welcome':
        welcome() 
    if selected_box == 'Image Compression':
        photo()



if __name__ == "__main__":
    main()
