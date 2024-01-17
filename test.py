from Res2former import Res2former
import torch
model = Res2former()
checkpoint = torch.load('Res2former.pth',map_location='cpu')
model.load_state_dict(checkpoint['model'],strict= False)
print (model.parameters())