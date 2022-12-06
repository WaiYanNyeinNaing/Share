import streamlit as st
from PIL import Image
import cv2 
import numpy as np
import os
import sys
from hurry.filesize import size

#pip install hurry.filesize


def load_image(path):
    image = Image.open(path)
    image = image.convert('RGB')
    return image


def welcome():
    
    st.title('Image Data Compression with AI')
    
    st.subheader('A simple app that shows different image compression algorithms. You can choose the options'
             + ' from the left.')
    
    st.image('logo.jpg',use_column_width=True)

def photo():
    st.header("Image Data Compression SIX-AM")

    uploaded_file = st.file_uploader("Upload Files",type=['png','jpeg','jpg'])
    if uploaded_file is not None:
        file_details = {"FileName":uploaded_file.name,"FileType":uploaded_file.type}
        st.write(file_details)

        file_path = uploaded_file.name
        file = file_path.split('.')[0]

        frame = load_image(uploaded_file)   #Input Test Image
        x = st.slider('Change Compression value',min_value = 0,max_value = 100)

        frame.save(f"result/compressed_{file}.jpeg",optimize = True,quality=x) 

        com_result = Image.open(f"result/compressed_{file}.jpeg")

        output_com = {"Compressed Image Dimension":com_result.size, "Image Size (bytes)":str(size(os.stat(f"result/compressed_{file}.jpeg").st_size)),
                        "Compression Ratio": str( round(int(os.stat(f"result/compressed_{file}.jpeg").st_size) * 100 / int(os.stat('test.jpg').st_size),2)) + " % of original image size" }
        st.text_area(label="Compressed File Size",value=output_com,height = 150)
        st.image(com_result, use_column_width=True,clamp = True)

    if st.button('Original Image'):
        original = load_image(uploaded_file)
        st.image(original, use_column_width=True)
        output = {"Original Image Size":original.size, "Image Size (bytes)": str(round(uploaded_file.size/1000)) + "K"}
        st.text_area(label="File Size",value=output,height = 150)

 
        







       
    
  
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
