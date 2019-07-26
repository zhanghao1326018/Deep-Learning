import sys
import time
from keras.datasets import cifar10
from keras.layers import Convolution2D, MaxPooling2D, AveragePooling2D
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import np_utils

# 开始下载数据集
t0 = time.time()  # 打开深度学习计时器
# CIFAR10 图片数据集
(X_train, Y_train), (X_test, Y_test) = cifar10.load_data()  # 32×32