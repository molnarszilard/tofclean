import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from depthdiffloss import DDDDepthDiff

class StDevLoss(nn.Module):
    def __init__(self):
        super(StDevLoss, self).__init__()

    def test(self):
        a = torch.ones(10,10)
        pad = nn.ConstantPad2d(4,0)
        b=pad(a)
        print(b)
        i=4
        b=b[i-4:i+4,i-4:i+4]
        print(b)


    def forward(self, depthin, gt):
        # self.test()
        ddd = DDDDepthDiff()
        ddd_loss=ddd(depthin,gt)

        K = [582.62448167737955, 0.0, 313.04475870804731, 0.0, 582.69103270988637, 238.44389626620386, 0.0, 0.0, 1.0] # nyu_v2_dataset
        # K = [582.624, 0.0, 313.045, 0.0, 582.691, 238.444, 0.0, 0.0, 1.0] # nyu_v2_dataset
        fx = K[0]
        fy = K[4]
        cx = K[2]
        cy = K[5]
        
        depth = depthin.cpu().detach()
        rows, cols = depth[0,0].shape
        c = torch.meshgrid(torch.arange(cols))
        new_c = c[0].reshape([1,cols])
        r = torch.meshgrid(torch.arange(rows))
        new_r = r[0].unsqueeze(-1)
        valid = (depth[0,0] > 0) & (depth[0,0] < 1.01)
        nan_number = torch.tensor(np.nan)
        eps_number = torch.tensor(1e-7)
        zero_number = torch.tensor(0.)
        z = torch.where(valid, depth[0,0]/1000.0, zero_number)
        x = torch.where(valid, z * (new_c - cx) / fx, zero_number)
        y = torch.where(valid, z * (new_r - cy) / fy, zero_number)
        # dimension = rows * cols
        # valid = torch.reshape(valid,(-1,))
        # z = torch.reshape(z,(-1,))
        # x = torch.reshape(x,(-1,))
        # y = torch.reshape(y,(-1,))
        sample_size=7
        padding_size=int((sample_size-1)/2)
        dev = torch.zeros(rows,cols)
        

        for i in range(rows):
            # print(i)
            for j in range(cols):
                
                if valid[i,j]:
                    idif=0
                    if i<padding_size:
                        idif=padding_size-i
                    else:
                        if i>rows-padding_size-1:
                            idif = rows-padding_size-1-i
                    jdif=0
                    if j<padding_size:
                        jdif=padding_size-j
                    else:
                        if j>cols-padding_size-1:
                            jdif = cols-padding_size-1-j
                    istart=i-padding_size+idif
                    jstart=j-padding_size+jdif
                    iend=i+padding_size+idif
                    jend=j+padding_size+jdif                    
                    zpadded = z[istart:iend+1,jstart:jend+1]
                    xpadded = x[istart:iend+1,jstart:jend+1]
                    ypadded = y[istart:iend+1,jstart:jend+1]
                    dist=((x[i,j]-xpadded).pow(2)+(y[i,j]-ypadded).pow(2)+(z[i,j]-zpadded).pow(2)).pow(0.5)
                    # print("tac")
                    # print(zpadded)

                    # dist = torch.ones(dimension)*10
                    # for j in range(dimension):
                    #     if i!=j and valid[j]:
                    #         dist[j]=((x[i]-x[j]).pow(2)+(y[i]-y[j]).pow(2)+(z[i]-z[j]).pow(2)).pow(0.5)
                    # knn, index = torch.topk(dist, 50, largest=False)
                    dev[i,j]=torch.std(dist)
        
        stdloss = dev.to('cuda').sum()
        loss = stdloss*100+ddd_loss
        return loss