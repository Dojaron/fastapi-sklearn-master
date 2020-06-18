# -*- coding: utf-8 -*-

import numpy as np
import h5py
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
import pandas as pd
from joblib import load,dump


X, y = make_blobs(n_samples=100, n_features=2, centers=2, random_state=3, cluster_std=2.5)
# print(X[:10])
# print(X.shape)
# print(type(X))


# 写入数据
with h5py.File('make_blobs.h5', 'w') as hf:
    hf.create_dataset("make_blobs-of-dataset", data=X)

# Xtrain = pd.DataFrame(X)
# Xtrain.to_csv("Xtrain.csv")
#
# ytrain = pd.DataFrame(y)
# ytrain.to_csv("ytrain.csv")
# 读取数据
with h5py.File('make_blobs.h5', 'r') as hf:
    data = hf["make_blobs-of-dataset"][:]
# print(data[:10])

# 对数据集进行分割
sz = 80
Xtrain, ytrain = X[0:sz], y[0:sz]
Xtest, ytest = X[sz:], y[sz:]

print(ytrain.shape)
Xtrain = pd.DataFrame(Xtrain)
Xtrain.to_csv("Xtrain.csv")

ytrain = pd.DataFrame(ytrain)
ytrain.to_csv("ytrain.csv")

Xtest = pd.DataFrame(Xtest)
Xtest.to_csv("Xtest.csv")

ytest = pd.DataFrame(ytest)
ytest.to_csv("ytest.csv")


with h5py.File('make_blobs_Xtrain.h5', 'w') as hf:
    hf.create_dataset("make_blobs-of-Xtrain", data=Xtrain)

with h5py.File('make_blobs_ytrain.h5', 'w') as hf:
    hf.create_dataset("make_blobs-of-ytrain", data=ytrain)

with h5py.File('make_blobs_Xtest.h5', 'w') as hf:
    hf.create_dataset("make_blobs-of-Xtest", data=Xtest)

with h5py.File('make_blobs_ytest.h5', 'w') as hf:
    hf.create_dataset("make_blobs-of-ytest", data=ytest)
#
# make model
clf = LogisticRegression(solver='lbfgs')
# # 拟合模型
# clf.fit(Xtrain, ytrain)
#
# # 模型预测
# print(clf.predict(Xtest))   # 返回预测结果，是标签值
#
# # 模型打分
# print(clf.score(Xtest, ytest))

# probs = np.around(clf.predict_proba(Xtest), 2)  # predict_probs返回的是一个 n 行 k 列的数组， 第 i 行 第 j 列上的数值是模型预测 第 i 个预测样本为某个标签的概率，并且每一行的概率和为1。
# print(probs)

# from joblib import dump, load
# dump(clf, 'model_1.joblib')
#
# print("****************************")
clf2 = load('model/clf.joblib')
print(Xtest[0].reshape(1,2))

