import numpy as np
from math import log2

# Calculates joint chance for our array.
def joint_chance(allocation):
    px = [0] * len(allocation)
    py = [0] * len(allocation)

    for i in range(0, len(allocation)):
        for j in range(0, len(allocation[i])):
            px[j] += allocation[i][j]
            py[i] += allocation[i][j]
    
    return px, py

# Calculates entropy for X, Y.
def entropy(allocation):

    px, py = joint_chance(allocation)

    Hx, Hy = 0, 0

    for i in range(0, len(px)):

        Hx += (-px[i]) * log2(px[i])
        Hy += (-py[i]) * log2(py[i])
    
    return [Hx, Hy]

# Calculates joint entropy.
def joint_entropy(allocation):

    Hxy = 0

    for i in range(0, len(allocation)):
        for j in range(0, len(allocation[i])):

            # log2 0  skipped
            if allocation[i][j] != 0: Hxy += (-allocation[i][j]) * log2(allocation[i][j])
    
    return Hxy

# Calculates commited entropy
def commited_entropy(entropies, joint_entropy):
    return [joint_entropy - entropies[1], joint_entropy - entropies[0]]

 
# Caculates mutual information.
def mutual_information(entropy, commited):
    return entropy - commited
    
    
    



allocation = [[1/7, 1/7, 1/7], [0, 1/7, 1/7], [2/7, 0, 0]]

entropies = entropy(allocation)
print('[H(X), H(X)] values are: ' + str(entropies))
joint = joint_entropy(allocation)
print('H(X,Y) value is=: ' + str(joint))
commited = commited_entropy(entropies, joint)
print('[H(Y|X), H(X|Y)] values are: ' + str(commited))
mutual = mutual_information(entropies[0], commited[0])
print('I(X,Y) value is: ' + str(mutual))
