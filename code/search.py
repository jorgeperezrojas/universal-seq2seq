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

def check_num(SL,CL,U,b1,b2):
    for i in range(len(SL)-1):
        change_map = utils.change_map(SL[i],U,b1,b2)
        if not (change_map == CL[i+1]).all():
            return i
    return len(SL)

YL = []

print('comenzando iteraciones...')
M = 0
j = 0
ind_M = -1
dat_M = None

for i,D in enumerate(product(range(-2,3),repeat=11)):
    if i % 10000 == 0:
        sys.stdout.write(str(len(YL))+' so far, max '+M+' ('+str(i)+'/50M)\r')
    U = np.array(D[:9]).reshape((3,3))
    b1 = D[9]
    b2 = D[10]
    j = check_num(SL,CL,U,b1,b2)
    if j > M:
        M = j
        dat_M = (i,j,U,b1,b2)
    if check_num(SL,CL,U,b1,b2) == len(SL):
        YL.append((i,U,b1,b2))

print(YL[0])