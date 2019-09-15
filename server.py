from flask import Flask, request,render_template, redirect
from torch_model import *
from PIL import Image
import numpy as np
import json
import cv2
import io
import os


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

with open('strain_info.json') as json_file:
    strain_info = json.load(json_file)

@app.route('/',methods=["GET", "POST"])
def index():
    yeet = {}
    if request.method == "POST":
        if request.files:
            imagefile = request.files.get('image', '') 
            image = Image.open(imagefile)
            out = get_output_dict(image)

            stuff = []
            for k in out.keys():
                thing = [k, str(100*float(out[k]))[:4]+'%',strain_info[k]['wiki'],strain_info[k]['info']]
                #stuff.append('<div><h3>'+k + ': ' + str(100*float(out[k]))[:4] + '%<a></h3><p><a href ={}>{}<a></p></div>'.format(strain_info[k]['wiki'],strain_info[k]['info']))
                stuff.append(thing)
            


            return render_template("index.html", info = stuff)
    return render_template("index.html", info = stuff)
    

if __name__ == '__main__':
    app.run(port = 5000, debug=True)
