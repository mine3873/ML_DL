import numpy as np

def matmul(A, B):
    """_summary_

    Args:
        A (np.array): m x n matrix
        B (np.array): n x p matrix
        
    return:
        C (np.array): m x p matrix
    """
    m = A.shape[0]
    p = B.shape[1]
    C = np.zeros([m,p])
    for i in range(m):
        for j in range(p):
            C[i,j] = np.dot(A[i,:],B[:,j])
    return C

A = np.array([[1,2,3],
              [4,5,6]])
B = np.array([[2,2],
              [1,3],
              [4,2]])
print(f"A : {A.shape}\nB : {B.shape}")
C = matmul(A,B)
Cvec = A @ B
print(f"C : {C.shape}\nCvec : {Cvec.shape}")
print(C)
print(Cvec)
