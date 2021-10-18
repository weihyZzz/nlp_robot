
#导入库
from model.model import *
from model.pre_process import *
import torch
#读入数据
print("############")
dataClass = Corpus('./data/qingyun.tsv', maxSentenceWordsNum=25)
#weihaoyang对train的第二次修改
#指定模型和一些超参
model = Seq2Seq(dataClass, featureSize=256, hiddenSize=256,
                attnType='L', attnMethod='concat',
                encoderNumLayers=5, decoderNumLayers=3,
                encoderBidirectional=True,
                device=torch.device('cuda:0'))
#训练
model.train(batchSize=1024, epoch=1000)
#保存模型
model.save('modelB.pkl')

# weihaoyang 2021.10.18对train进行修改