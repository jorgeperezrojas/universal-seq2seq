import numpy as np
import utils
from itertools import product
import sys

A = np.loadtxt('../data/evol_06.txt', dtype=int)
SL = []
ant_i = 0
for i in range(6,len(A)+1,6):
    SL.append(A[ant_i:i,:])
    ant_i = i

B = np.loadtxt('../data/evol_06.txt', dtype=int)
CL = []
ant_i = 0
for i in range(6,len(A)+1,6):
    CL.append(np.clip(B[ant_i:i,:],0,1))
    ant_i = i

def check(SL,CL,U,b1,b2):
    for i in range(len(SL)-1):
        change_map = utils.change_map(SL[i],U,b1,b2)
        if not (change_map == CL[i+1]).all():
            return False
    return True

bias = [-2,-1,1,2]
options = list(product(product(range(-2,3),repeat=9),bias,bias))
print(len(options))

YL = []

for i,D in enumerate(options):
    if i % 10000 == 0:
        sys.stdout.write(str(len(YL))+' so far ('+str(i)+'/50M)\r')
    U = np.array(D[:9]).reshape((3,3))
    b1 = D[9]
    b2 = D[10]
    if check(SL,CL,U,b1,b2):
        YL.append((i,U,b1,b2))

print(YL[0])