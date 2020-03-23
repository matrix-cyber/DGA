import os
import keras
import pandas as pd
import numpy as np
from keras import layers
import matplotlib.pyplot as plt
%matplotlib inline


def get_data():
    "获取数据集"
    path = os.getcwd()
    dga = path + '\data\dga.txt'
    alexa = path + '\data\\alexa.txt'

    dga_data = pd.read_table(dga,encoding='utf-8',skiprows=17,sep='\s+')
    alexa_data = pd.read_table(alexa,encoding='utf-8',sep=',')
    #
    return train_dga,train_alexa

def train_test_split(train_dga, train_alexa, test_train = 0.2, seed = None):
    """将原始数据X、y分割为X_train、y_train、X_test、y_test"""

    assert X.shape[0] == y.shape[0],\
        "the size of X must be equal to the size of y"
    assert 0.0 <= test_train <= 1.0,\
        "test_train must be valid"
    # seed为随机数的种子，为了两次随机数取值相同
    if seed:
        np.random.seed(seed)
    # 先对原始数据的indexes做乱序处理
    shuffle_indexes = np.random.permutation(len(X))
    # 分配训练数据和测试数据的比例和大小
    test_ratio = test_train
    test_size = int(len(X) * test_ratio)
    test_indexes = shuffle_indexes[:test_size]
    train_indexes = shuffle_indexes[test_size:]
    # 分割原始数据
    X_train = X[train_indexes]
    y_train = y[train_indexes]

    X_test = X[test_indexes]
    y_test = y[test_indexes]

    return X_train, X_test, y_train, y_test


def build_model():
    "构建模型"
    model = keras.Sequential()
    model.add(layers.Embedding())
    model.add(layers.recurrent.LSTM(128))
    model.add(layers.core.Dropout(0.5))
    model.add(layers.core.Dense(1))
    model.add(layers.core.Activation('sigmoid'))
    model.compile(loss='binary_crossentropy',optimizer='rmsprop')
    
    return model
    
def run():
    "训练"
    train_dga = get_data()
    
    model = build_model（）
    model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=1)
