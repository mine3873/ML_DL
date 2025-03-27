import numpy as np
import math

X = np.array([[200, 17]])
W = np.array([[1, -3, 5],
			[-2, 4, -6]])
B = np.array([-1, 1, 2])

print(f"X : {X.shape}\n W : {W.shape}\nB : {B.shape}")

def g(z):
    return 1 / ( 1 + np.exp(-z))


def dense(a_in, W, B):
    Z = np.matmul(a_in, W) + B
    a_out = g(Z)
    return a_out

def sequential(X, W1, B1):
    A1 = dense(X, W1, B1)
    return A1

output = sequential(X, W, B)
print(output)
