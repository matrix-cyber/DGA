import keras
import pandas as pd
import numpy as np
from keras import layers
import matplotlib.pyplot as plt
%matplotlib inline

dga = 'D:\WorkSpace\Python\DGA\data\dga.txt'
alexa = 'D:\WorkSpace\Python\DGA\data\\alexa.txt'

dga_data = pd.read_table(dga,encoding='utf-8',skiprows=17,sep='\s+')
alexa_data = pd.read_table(alexa,encoding='utf-8',sep=',')

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
    
    model = build_model()
    model.fit()
