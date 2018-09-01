import numpy as np
from itertools import product

def get(S,i,j):
    K = np.zeros((3,3))
    K[1,1] = S[i,j]
    if i > 0:
        K[0,1] = S[i-1,j]
    if i < len(S) - 1:
        K[2,1]  = S[i+1,j]
    if j > 0:
        K[1,0] = S[i,j-1]
        if i > 0:
            K[0,0] = S[i-1,j-1]
        if i < len(S) - 1:
            K[2,0] = S[i+1,j-1]
    if j < 1:
        K[1,2] = S[i,j+1]
        if i > 0:
            K[0,2] = S[i-1,j+1]
        if i < len(S) - 1:
            K[2,2] = S[i+1,j+1]
    return K
    
        

def mult(S,U,i,j):
    K = get(S,i,j)
    K = K * U
    return np.sum(K)

def conv(S,U):
    out = np.array([
        [mult(S,U,i,0) for i in range(len(S))],
        [mult(S,U,i,1) for i in range(len(S))]
    ]).T
    return out

def decide_change(S,U):
    return np.clip(conv(S,U),0,1)

def apply_change_line(X,Y,c):
    out = []
    for (x,y) in zip(X,Y):
        if y == 0.0:
            out.append(c)
        else:
            out.append(x)
    return np.array(out)

def apply_change(S,C,cx,cy):
    out1 = apply_change_line(S[:,0],C[:,0],cx)
    out2 = apply_change_line(S[:,1],C[:,1],cy)
    return np.array([out1,out2]).T

def iterar(S,U,n,cx,cy):
    L = []
    L.append(S)
    for _ in range(n):
        C = decide_change(S,U)
        S = apply_change(S,C,cx,cy)
        L.append(S)
    return np.array(L)

def mostrar_evol(L):
    for l in L:
        print(l.T)
        print()

S = np.array([[1,-1] for _ in range(10)])
print(S)

O = S
L_O = [O]
for i in range(10):
    N = np.copy(L_O[-1])
    N[i,0] = -1
    N[i,1] = 1
    L_O.append(N)
L_O = np.array(L_O)    
L = iterar(S,U,10,-1,1)

YL = []
options = list(product(range(-2,3),repeat=9))
init = 0
end = -1

for i,pU in enumerate(options[init:end]):
    if i % 10000 == 0:
        print(len(YL),'so far')
    U = np.array(pU).reshape((3,3))
    L = iterar(S,U,10,-1,1)
    if (L == L_O).all():
        YL.append((i+init,U))

with open('out_arr_01.txt','wb') as outfile_arr, open('out_ind_01.txt','w') as outfile_ind:
    for (i,y) in YL:
        np.savetxt(outfile_arr,y,'%d')
	outfile_ind.write(str(i)+'\n')


