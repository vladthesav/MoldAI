from flask import Flask, request,render_template, redirect
from torch_model import *
from PIL import Image
import numpy as np
import cv2
import io
import os


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index',methods=["GET", "POST"])
def index():
    yeet = {}
    if request.method == "POST":
        if request.files:
            imagefile = request.files.get('image', '') 
            image = Image.open(imagefile)
            yeet = get_output_dict(image)
            print(yeet) 

            return render_template("index.html", predictions=yeet)
    return render_template("index.html", predictions=yeet)
    

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
