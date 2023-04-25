import io

import requests
from PIL import Image
import streamlit as st

def request_image(prompt):

    endpoint = "http://fastapi_service:3003/generate-image-dalle/"
    response = requests.post(endpoint,json={"prompt": prompt})


    if response.status_code == 200:
        
        img_bytes = io.BytesIO(response.content)
    else:
        raise Exception(f"Request failed with status {response.status_code}")
    
    return img_bytes
    
    