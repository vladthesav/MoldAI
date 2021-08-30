from flask import Flask, request,render_template
from torch_model import *
from PIL import Image
import numpy as np
import json
import os


app = Flask(__name__)

#this file stores some info and links about all the strains we care bout
with open('strain_info.json') as json_file:
    strain_info = json.load(json_file)
    
#this is where the magic happens
@app.route('/',methods=["GET", "POST"])
def index():
    #this is a list of data we want to display
    stuff = []
    if request.method == "POST":
        #this is when we get a file from the client
        if request.files:
            #turn image data into PILL objecct
            imagefile = request.files.get('image', '') 
            image = Image.open(imagefile)
            
            #this is where the ml happens
            out = get_output_dict(image)
            
            #here we loop through a dictionary of predictions {class_i: predictions_i}
            stuff = []
            for k in out.keys():
                #here we pack in the class name (k), probability as percent, class wiki link, and class info (some text from wikipedia)
                thing = [k, str(100*float(out[k]))[:4]+'%',strain_info[k]['wiki'],strain_info[k]['info']]
                stuff.append(thing)
            

            #now pass list thing into our template, predictions get displayed there
            return render_template("index.html", info = stuff)
        
    return render_template("index.html", info = stuff)
    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)
