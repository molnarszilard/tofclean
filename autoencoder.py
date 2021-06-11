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
        self.enc0 = nn.Conv2d(3, 1024, kernel_size=3, padding=1, stride=2)
        self.enc1 = nn.Conv2d(1024, 512, kernel_size=3, padding=1)
        self.enc2 = nn.Conv2d(512, 256, kernel_size=3, padding=1, stride=2)
        self.enc3 = nn.Conv2d(256, 128, kernel_size=3, padding=1)
        self.enc4 = nn.Conv2d(128, 64, kernel_size=3, padding=1, stride=2)
        self.enc5 = nn.Conv2d(64, 32, kernel_size=3, padding=1)
        self.enc6 = nn.Conv2d(32, 16, kernel_size=3, padding=1, stride=2)
        self.enc7 = nn.Conv2d(16, 8, kernel_size=3, padding=1)
        self.enc8 = nn.Conv2d(8, 4, kernel_size=3, padding=1, stride=2)
        # self.pool = nn.MaxPool2d(2, 2)        
        
        # decoder layers
        self.dec0 = nn.ConvTranspose2d(4, 8, kernel_size=2, stride=2)  
        self.dec1 = nn.ConvTranspose2d(8, 16, kernel_size=3, padding=1)
        self.dec2 = nn.ConvTranspose2d(16, 32, kernel_size=2, stride=2)
        self.dec3 = nn.ConvTranspose2d(32, 64, kernel_size=3, padding=1)
        self.dec4 = nn.ConvTranspose2d(64, 128, kernel_size=2, stride=2)
        self.dec5 = nn.ConvTranspose2d(128, 256, kernel_size=3, padding=1)
        self.dec6 = nn.ConvTranspose2d(256, 512, kernel_size=2, stride=2)
        self.dec7 = nn.ConvTranspose2d(512, 1024, kernel_size=3, padding=1)
        
        # self.upsample = nn.Upsample(scale_factor=2, mode='nearest')
        self.out = nn.ConvTranspose2d(1024, 1, kernel_size=2, stride=2)

    def forward(self, x0):
        # encode

        x = F.relu(self.enc0(x0))
        x = F.relu(self.enc1(x))
        x = F.relu(self.enc2(x))
        x = F.relu(self.enc3(x))
        x = F.relu(self.enc4(x))
        x = F.relu(self.enc5(x))
        x = F.relu(self.enc6(x))
        x = F.relu(self.enc7(x))
        x = F.relu(self.enc8(x))
        
        # decode
        x = F.relu(self.dec0(x))
        x = F.relu(self.dec1(x))
        x = F.relu(self.dec2(x))
        x = F.relu(self.dec3(x))
        x = F.relu(self.dec4(x))
        x = F.relu(self.dec5(x))
        x = F.relu(self.dec6(x))
        x = F.relu(self.dec7(x))
        x = self.out(x)
        return x
net = Autoencoder()
print(net)