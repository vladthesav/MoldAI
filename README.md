# MoldAI
MoldAI is a computer vision web app that classifies common strains of mold on surfaces and displays information about it. This was created for HopHacks 2019.

It consists of a PyTorch model running inside of a flask server that takes an image from an html form and outputs a list of predictions that get displayed allong with information about each strain. The PyTorch model uses features extracted by EfficientNet-b0 (https://arxiv.org/abs/1905.11946) and was trained on remarkably little data (311 images total). Through transfer learning I was able to score 72% accuracy on the validation set.

To run this app you will need the following installed:
  - Flask
  - Pillow
  - PyTorch
  - EfficientNet-Pytorch (instructions on how to install here https://github.com/lukemelas/EfficientNet-PyTorch)
  
  
To use this app use the following bash commmands:
   - git clone https://github.com/vladthesav/MoldAI.git
   - cd MoldAI
   - python server.py
    
 After that connect to your local machine and you're set!
 
  
