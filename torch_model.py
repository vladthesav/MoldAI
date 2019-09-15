import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms

from efficientnet_pytorch import EfficientNet


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.base = EfficientNet.from_pretrained('efficientnet-b0')
        
        self.fc = nn.Linear(1280*7*7, 7)

    def forward(self, x):
        x = self.base.extract_features(x)
        x=x.view(x.size(0), -1)
        x = self.fc(x)
        return x
      
    def probabilities(self, x):
      linear = self.forward(x)
      return torch.exp(linear)/torch.sum(torch.exp(linear))

tfms = transforms.Compose([
    transforms.Resize((224,224)), 
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

net = Net()
net.load_state_dict(torch.load('models/e_net'), strict=False)

class_list = ['Chaetomium',
 'Acremonium',
 'Cladosporium',
 'Aspergillus',
 'Ulocladium',
 'Alternaria',
 'Aureobasidium']

def get_predictions(x):
    return net.probabilities(tfms(x).unsqueeze(0)).detach().numpy()

def get_output_dict(x):
    preds = get_predictions(x)[0]
    return {c:d for c,d in zip(class_list,preds)}