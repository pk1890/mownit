import numpy as np 
from matplotlib import pyplot as plt
import random
n = 8

def totalDist(state):
    (X, Y) = state
    dist = 0
    for i in range(len(X)-1):
        dist = dist + np.sqrt((X[i+1]-X[i])**2 + (Y[i+1]-Y[i])**2)
    return dist

# x,y = np.random.randint(0, 100, n), np.random.randint(0, 100, n)

######################### NORMAL 
# x, y = np.random.normal(35, 5, n), np.random.normal(35, 5, n)
# x = np.append(x, np.random.normal(5, 10, n))
# y = np.append(y, np.random.normal(10, 10, n))

# x = np.append(x, np.random.normal(0, 7, n))
# y = np.append(y, np.random.normal(20, 7, n))

# x = np.append(x, np.random.normal(5, 10, n))
# y = np.append(y, np.random.normal(40, 10, n))

##############################
x = np.array([])
y = np.array([])

for i in range(3):
    for j in range(3):
        x = np.append(x, np.random.uniform(20*i, 20*i+10, n))
        y = np.append(y, np.random.uniform(20*j, 20*j+10, n))
np.random.shuffle(x)
np.random.shuffle(y)

def neighbor(state):
    (X, Y) = state
    new_x = [x for x in X]
    new_y = [y for y in Y]
    a = random.randint(0, len(x) - 1)
    b = random.randint(0, len(x) - 1)
    new_x[a], new_x[b] = new_x[b], new_x[a] 
    new_y[a], new_y[b] = new_y[b], new_y[a] 
    return (new_x, new_y) 

def consecneighbor(state):
    (X, Y) = state
    new_x = [x for x in X]
    new_y = [y for y in Y]
    a = random.randint(0, len(x) - 2)
    new_x[a], new_x[a+1] = new_x[a+1], new_x[a] 
    new_y[a], new_y[a+1] = new_y[a+1], new_y[a] 
    return (new_x, new_y) 

def acceptanceProbability(old_cost, new_cost, T):
    # print("Old_cost: ", old_cost, "new: ", new_cost)
    return np.exp((-new_cost+old_cost)/T)

def anneal(state, T, isConsec):
    T_min = 0.000005
    alpha = 0.95
    old_cost = totalDist(state)
    while T > T_min:
        i = 1
        while i <= 100:
            new_state = neighbor(state) if not isConsec else consecneighbor(state)
            new_cost = totalDist(new_state)
            ap = acceptanceProbability(old_cost, new_cost, T)
            if ap > random.random():
                state = new_state
                old_cost = new_cost
            i += 1
        T = T*alpha
    return new_state, new_cost



fig = plt.figure(figsize=(14,6))
ax = fig.add_subplot(2, 2, 1)
bx = fig.add_subplot(2, 2, 2)
cx = fig.add_subplot(2, 2, 3)
dx = fig.add_subplot(2, 2, 4)

ax.scatter(x, y, c='r')
ax.plot(x, y)

new_state, new_cost = anneal((x, y), 10000, False)
bx.scatter(x, y, c='r')
(nx, ny) = new_state
bx.plot(nx, ny)
print("old_cost: ", totalDist((x, y)), "new_cost: ", new_cost)

new_state, new_cost = anneal((x, y), 10000, True)
cx.scatter(x, y, c='r')
(nx, ny) = new_state
cx.plot(nx, ny)
print("old_cost: ", totalDist((x, y)), "new_cost: ", new_cost)

new_state, new_cost = anneal((x, y), 1, False)
dx.scatter(x, y, c='r')
(nx, ny) = new_state
dx.plot(nx, ny)
print("old_cost: ", totalDist((x, y)), "new_cost: ", new_cost)
plt.show()
# new_state, new_cost = anneal(new_state)
# plt.scatter(x, y, c='r')
# (nx, ny) = new_state
# plt.plot(nx, ny)
# print("old_cost: ", totalDist((x, y)), "new_cost: ", new_cost)
# plt.show()

