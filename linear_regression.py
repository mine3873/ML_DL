import numpy as np



feature = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
label = np.array([5,7,9,11,13,15,17,19,21,23,25,27])

"""
fwb_x = wx + b

"""


def cost_function(m,w,b, x, y):
    cost = 0
    for i in range(m):
        prediction = w * x[i] + b
        cost += (prediction - y[i])**2
    
    cost = cost / (2*m)
    return cost



def gradient_descent_each_step(w_init,b_init, m, a, x, y):
    dj_dw = 0
    dj_db = 0
    
    for i in range(m):
        fwb_x = w_init * x[i] + b_init
        dj_dw += (fwb_x - y[i]) * x[i]
        dj_db += fwb_x - y[i]
    w = w_init - a * dj_dw / m
    b = b_init - a * dj_db / m
    
    return w, b

def gradient_descent(m , w_init, b_init, features, labels, iteration, a):
    w, b = w_init, b_init
    cur_cost = cost_function(m,w,b,features,labels)
    for iter in range(iteration):
        w, b = gradient_descent_each_step(w,b,m,a,features,labels)
        new_cost = cost_function(m,w,b,features,labels)
        if new_cost > cur_cost:
            break
        print(f"{iter} : cost = {new_cost} prev_cost = {cur_cost}, w = {w}, b = {b}")
        cur_cost = new_cost
    return w, b

w_init = 1
b_init = 1
size = len(feature)  
    
###w, b = gradient_descent(size, w_init, b_init, feature, label, 30000, 0.0005)

def predict(w,b,x):
    label_hat = w * x + b
    return label_hat

"""
print(f"x = 1.5 ? : {predict(w,b,1.5)}")
print(f"x = 3.5 ? : {predict(w,b,3.5)}")
print(f"x = 8.9 ? : {predict(w,b,8.9)}")
print(f"x = 14 ? : {predict(w,b,14)}")
"""
print(f"{feature+label}")