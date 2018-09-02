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
    
def mult(S,U,i,j,b=0):
    K = get(S,i,j)
    K = K * U
    return np.sum(K) + b

def conv(S,U,b1=0,b2=0):
    out = np.array([
        [mult(S,U,i,0,b1) for i in range(len(S))],
        [mult(S,U,i,1,b2) for i in range(len(S))]
    ]).T
    return out