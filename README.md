# KG for relation

夏令营成果，LSTM+attention模型训练关系

## 文件描述

entity.py 查表获得实体

extract.py 获得关系

graphic.py 获得三元组

nlp.py 使用斯坦福工具获得实体

train.py 训练

data目录中每个子目录有data_util用于将输入文本结构化

## 训练数据

数据集提供十万条标注好的数据。选择两万数据用以训练（包含测试集）

格式： 实体  实体  关系  句子


## 结果

80EPOCH结果：

不使用词向量      F1=43%

使用词向量       F1=34%




