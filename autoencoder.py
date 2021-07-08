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
        self.encx = nn.Conv2d(3, 1, kernel_size=3, padding=1)
        self.enc0 = nn.Conv2d(3, 512, kernel_size=3, padding=1)
        self.enc1 = nn.Conv2d(512, 256, kernel_size=3, padding=1, stride=2)
        self.enc2 = nn.Conv2d(256, 128, kernel_size=3, padding=1)
        self.enc3 = nn.Conv2d(128, 64, kernel_size=3, padding=1, stride=2)
        self.enc4 = nn.Conv2d(64, 32, kernel_size=3, padding=1)
        self.enc5 = nn.Conv2d(32, 16, kernel_size=3, padding=1, stride=2)
        self.enc6 = nn.Conv2d(16, 8, kernel_size=3, padding=1)
        self.enc7 = nn.Conv2d(8, 4, kernel_size=3, padding=1, stride=2)
        # self.pool = nn.MaxPool2d(2, 2)        
        
        # decoder layers
        self.dec0 = nn.ConvTranspose2d(4, 4, kernel_size=3, padding=1)  
        self.dec1 = nn.ConvTranspose2d(4, 8, kernel_size=2, stride=2)
        self.dec2 = nn.ConvTranspose2d(8, 16, kernel_size=3, padding=1)
        self.dec3 = nn.ConvTranspose2d(16, 32, kernel_size=2, stride=2)
        self.dec4 = nn.ConvTranspose2d(32, 64, kernel_size=3, padding=1)
        self.dec5 = nn.ConvTranspose2d(64, 128, kernel_size=2, stride=2)
        self.dec6 = nn.ConvTranspose2d(128, 256, kernel_size=3, padding=1)
        self.dec7 = nn.ConvTranspose2d(256, 512, kernel_size=2, stride=2)
        
        # self.upsample = nn.Upsample(scale_factor=2, mode='nearest')
        self.out = nn.ConvTranspose2d(512, 1, kernel_size=3, padding=1)

    def forward(self, x0):
        # encode
        debug = False
        # ex = F.relu(self.encx(x0))
        e0 = F.relu(self.enc0(x0))
        if debug:
            print(e0.shape)
        e1 = F.relu(self.enc1(e0))
        if debug:
            print(e1.shape)
        e2 = F.relu(self.enc2(e1))
        if debug:
            print(e2.shape)
        e3 = F.relu(self.enc3(e2))
        if debug:
            print(e3.shape)
        e4 = F.relu(self.enc4(e3))
        if debug:
            print(e4.shape)
        e5 = F.relu(self.enc5(e4))
        if debug:
            print(e5.shape)
        e6 = F.relu(self.enc6(e5))
        if debug:
            print(e6.shape)
        e7 = F.relu(self.enc7(e6))
        if debug:
            print(e7.shape)
        
        # decode
        d0 = F.relu(self.dec0(e7))+e7
        if debug:
            print(d0.shape)
        d1 = F.relu(self.dec1(d0))+e6
        if debug:
            print(d1.shape)
        d2 = F.relu(self.dec2(d1))+e5
        if debug:
            print(d2.shape)
        d3 = F.relu(self.dec3(d2))+e4
        if debug:
            print(d3.shape)
        d4 = F.relu(self.dec4(d3))+e3
        if debug:
            print(d4.shape)
        d5 = F.relu(self.dec5(d4))+e2
        if debug:
            print(d5.shape)
        d6 = F.relu(self.dec6(d5))+e1
        if debug:
            print(d6.shape)
        d7 = F.relu(self.dec7(d6))+e0
        if debug:
            print(d7.shape)
        # x = F.relu(self.out(d7))
        x = torch.sigmoid(self.out(d7))
        # maxx=x.max()
        # x=x/maxx
        return x
net = Autoencoder()
print(net)