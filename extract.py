import numpy as np
import pickle
import torch
import torch.nn as nn
import torch.optim as optim

import torch.utils.data as D
from torch.autograd import Variable
from BiLSTM_ATT import BiLSTM_ATT

with open('./data/XCAQ.pkl', 'rb') as inp:
    test = pickle.load(inp)
    labels_t = pickle.load(inp)
    position1_t = pickle.load(inp)
    position2_t = pickle.load(inp)

BATCH = 128
EPOCHS = 100
learning_rate=0.05

model = torch.load('model/model_epoch80.pkl')
optimizer = optim.Adam(model.parameters(), lr=learning_rate, weight_decay=1e-5)
criterion = nn.CrossEntropyLoss(size_average=True)

test = torch.LongTensor(test[:len(test)-len(test)%BATCH])
position1_t = torch.LongTensor(position1_t[:len(test)-len(test)%BATCH])
position2_t = torch.LongTensor(position2_t[:len(test)-len(test)%BATCH])
labels_t = torch.LongTensor(labels_t[:len(test)-len(test)%BATCH])
test_datasets = D.TensorDataset(test,position1_t,position2_t,labels_t)
test_dataloader = D.DataLoader(test_datasets,BATCH,num_workers=2)

print(test_dataloader)
#out=open('relation.txt','wb')
out=[]
for sentence, pos1, pos2, tag in test_dataloader:
    sentence = Variable(sentence)
    pos1 = Variable(pos1)
    pos2 = Variable(pos2)
    y = model(sentence, pos1, pos2)
    y = np.argmax(y.data.numpy(), axis=1)
    out.append(y)
out=np.array(out)
np.save('data/XCAQ/temp/relation.npy',out)
        #out.write(np.dtype(str,y1))
#out.close()