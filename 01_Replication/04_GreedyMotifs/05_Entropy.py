import math
# Profile
A = [ .2,  .2,  0,   0,   0,   0,   .9,  .1,  .1,  .1,  .3,  0]
C = [ .1,  .6,  0,   0,   0,   0,   0,   .4,  .1,  .2,  .4,  .6]
G = [  0,   0,  1,   1,   .9,  .9,  .1,  0,   0,   0,   0,   0]
T = [ .7,  .2,  0,   0,   .1,  .1,  0,   .5,  .8,  .7,  .3,  .4]

entropy = 0
for i in range(len(A)):
    logA = 0
    logC = 0
    logG = 0
    logT = 0
    if A[i] != 0:
        logA = math.log2(A[i])
    if C[i] != 0:
        logC = math.log2(C[i])
    if G[i] != 0:
        logG = math.log2(G[i])
    if T[i] != 0:
        logT = math.log2(T[i])
    entropy = entropy - ( A[i]* logA + C[i] * logC + G[i] * logG + T[i] * logT )

print(entropy)
