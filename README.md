# MoldAI
MoldAI is a computer vision web app that classifies common strains of mold on surfaces and displays information about it. This was created for HopHacks 2019.

It consists of a PyTorch model running inside of a flask server that takes an image from an html form and outputs a list of predictions that get displayed allong with information about each strain.

To run this app you will need the following installed:
  - Flask
  - Pllow
  - PyTorch
  - EfficientNet-Pytorch (instructions on how to download here https://github.com/lukemelas/EfficientNet-PyTorch)
  
 Start the server with the following command:
    -- python server.py
 
  
