# %%
# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
# %%
class Autoencoder(nn.Module):
    def __init__(self):
        super(Autoencoder, self).__init__()
        # encoder layers
        self.enc1 = nn.Conv2d(3, 512, kernel_size=3, padding=1)
        self.enc2 = nn.Conv2d(512, 256, kernel_size=3, padding=1)
        self.enc3 = nn.Conv2d(256, 128, kernel_size=3, padding=1)
        self.enc4 = nn.Conv2d(128, 64, kernel_size=3, padding=1)
        self.enc5 = nn.Conv2d(64, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)        
        
        # decoder layers
        self.dec1 = nn.Conv2d(32, 64, kernel_size=3, padding=1)  
        self.dec2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.dec3 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.dec4 = nn.Conv2d(256, 512, kernel_size=3, padding=1)
        
        self.upsample = nn.Upsample(scale_factor=2, mode='nearest')
        self.out = nn.Conv2d(512, 1, kernel_size=3, padding=1)

    def forward(self, x0):
        # encode

        x = F.relu(self.enc1(x0))
        x = self.pool(x)
        x = F.relu(self.enc2(x))
        x = self.pool(x)
        x = F.relu(self.enc3(x))
        x = self.pool(x)
        x = F.relu(self.enc4(x))
        x = self.pool(x)
        x = F.relu(self.enc5(x))
        x = self.pool(x)
        
        # decode
        x = F.relu(self.dec1(x))
        x = self.upsample(x)
        x = F.relu(self.dec2(x))
        x = self.upsample(x)
        x = F.relu(self.dec3(x))
        x = self.upsample(x)
        x = F.relu(self.dec4(x))
        x = self.upsample(x)
        x = F.interpolate(x, size=(x0.shape[2],x0.shape[3]), mode='nearest')
        x = self.out(x)
        # x = F.sigmoid(self.out(x))
        return x
net = Autoencoder()
# print(net)