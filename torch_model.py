import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms

from efficientnet_pytorch import EfficientNet

#define model here
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        #this is the pretrained EfficientNet model which we use as a feature extractor
        self.base = EfficientNet.from_pretrained('efficientnet-b0')
        
        #fully connected layer which maps features to 7-dim vector space (7 dims for 7 classes)
        self.fc = nn.Linear(1280*7*7, 7)
    
    def forward(self, x):
        x = self.base.extract_features(x)
        x=x.view(x.size(0), -1)
        x = self.fc(x)
        return x
    #here we apply a softmax activation to get our 'probabilities'  
    def probabilities(self, x):
      linear = self.forward(x)
      return torch.exp(linear)/torch.sum(torch.exp(linear))
    
#transforms for making Pil images into the data type PyTorch wants
tfms = transforms.Compose([
    transforms.Resize((224,224)), 
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

#now let's load our weights into the model
net = Net()
net.load_state_dict(torch.load('models/e_net'), strict=False)

#here are all the classes this model was trained to detect
class_list = ['Chaetomium',
 'Acremonium',
 'Cladosporium',
 'Aspergillus',
 'Ulocladium',
 'Alternaria',
 'Aureobasidium']

#gets rescaled predictions as a numpy array
def get_predictions(x):
    #make sure it's rgb
    x = x.convert("RGB")
    x = tfms(x).unsqueeze(0)

    with torch.no_grad(): out = net.probabilities(x).detach().numpy()
    return out

#now return a dictioany of the form {C_i: predictions_i}
def get_output_dict(x):
    preds = get_predictions(x)[0]
    return {c:d for c,d in zip(class_list,preds)}
