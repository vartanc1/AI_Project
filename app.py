import json
import requests
import io
import base64
from Open_AI import openai_prompt # open ai api prompt
from Open_AI import prompt_cleaner # open ai text cleaner function

from PIL import Image, PngImagePlugin

url = "http://127.0.0.1:7860"



def app_func():
    
    
    openai_prompt()
    prompt_cleaner();
    my_file = open("text.txt","rt")

    x = my_file.read()
    my_file.close()

    payload = {
    "prompt":f"{x}",
    "negative_prompt": "nsfw",
    "steps": 20,
    "seed":-1,
    "cfg_scale": 5,
    "batch_size": 1,
    "enable_hr": True,
    "denoising_strength": 0.5,
    "hr_scale": 1.5,
    "hr_resize_x": 0,
    "hr_resize_y": 0,
    "hr_upscaler": "R-ESRGAN 4x+",
    "sampler_name": "DPM++ SDE Karras"
    }
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
        png_payload = {
            "image": "data:image/png;base64," + i
            }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save('static/output.png', pnginfo=pnginfo)