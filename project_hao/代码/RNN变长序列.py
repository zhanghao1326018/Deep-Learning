import tensorflow as tf
import numpy as np

X = np.random.randn(2,4,5)
print(X)
X[1,1:]=0
print(X)