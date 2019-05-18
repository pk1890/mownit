import numpy as np
import matplotlib.pyplot as plt
import random
from matplotlib import colors
import numpy as np

G = 0.01
N = 50


# def energy(p0,p1):
#     (x0,y0) = p0
#     (x1,y1) = p1
#     return


def neighbor(points):
    # newPoints = np.copy(points)
    # np.random.shuffle(newPoints)
    # return newPoints
    new_points = np.copy(points)
    swapped = False
    while not swapped:
        a = random.randint(0, N - 1)
        b = random.randint(0, N - 1)
        if new_points[(a, b)] == 1:
            i = 0
            while not swapped and i < 10:
                c = random.randint(0, N - 1)
                d = random.randint(0, N - 1)
                if new_points[(c, d)] == 0:
                    swapped = True
                    new_points[(a, b)] = 0
                    new_points[(c, d)] = 1
    return new_points


# Listy przesuniec dlo sasiadow
dx4 = list([0, 1, 0, -1])
dy4 = list([1, 0, -1, 0])

dx8 = list([0, 0, 1, 1, 1, -1, -1, -1])
dy8 = list([1, -1, -1, 0, 1, -1, 0, 1])

dx16 = list([-2, -2, -2, -2, -2, 2, 2, 2, 2, 2, -1, 0, 1, -1, 0, 1])
dy16 = list([-2, -1, 0, 1, 2, -2, -1, 0, 1, 2, -2, -2, -2, 2, 2, 2])
###############

def cost4(points):
    def newCoord(coord, offset):
        return min(N - 1, max(0, coord + offset))
    cost = 0
    for a in range(0, N):
        for b in range(0, N):
            if points[(a, b)] == 1:
                j = 0
                for i in range(3):
                    c = newCoord(a, dx4[i]) 
                    d = newCoord(b, dy4[i]) 
                    if c != a or b != d:
                        j += 1
                        cost += points[(c, d)]  # * 2 ** j

    return cost


def cost8(points):
    def newCoord(coord, offset):
        return min(N - 1, max(0, coord + offset))
    cost = 0
    for a in range(0, N):
        for b in range(0, N):
            if points[(a, b)] == 1:
                j = 0
                for i in range(7):
                    c = newCoord(a, dx8[i]) 
                    d = newCoord(b, dy8[i]) 
                    if c != a or b != d:
                        j += 1
                        cost += points[(c, d)]  # * 2**j

    return cost


def cost816(points):
    def newCoord(coord, offset):
        return min(N - 1, max(0, coord + offset))
    cost = 0
    for a in range(0, N):
        for b in range(0, N):
            if points[(a, b)] == 1:
                j = 0
                for i in range(7):
                    c = newCoord(a, dx8[i]) 
                    d = newCoord(b, dy8[i]) 
                    if c != a or b != d:
                        j += 0.5
                        cost += points[(c, d)] / 2 ** j
                j = 0
                for i in range(0, 15):
                    c = newCoord(a, dx16[i]) 
                    d = newCoord(b, dy16[i]) 
                    if c != a or b != d:
                        j += 1
                        cost += points[(c, d)] / 2 ** j

    return cost


def acceptance_probability(old_cost, new_cost, T):
    # print("Old_cost: ", old_cost, "new: ", new_cost)
    return np.exp((new_cost - old_cost) / T)


def anneal(sol, cost):
    old_cost = cost(sol)
    T = 1.0
    T_min = 0.01
    alpha = 0.9
    while T > T_min:
        i = 1
        while i <= 100:
            new_sol = neighbor(sol)
            new_cost = cost(new_sol)
            ap = acceptance_probability(old_cost, new_cost, T)
            # print(old_cost, new_cost)

            if ap > random.random():
                sol = new_sol
                old_cost = new_cost

            i += 1
        T = T * alpha
    return sol, new_cost


def zad1(N, val):
    fig = plt.figure(figsize=(14,6))
    ax = fig.add_subplot(2, 2, 1)
    bx = fig.add_subplot(2, 2, 2)
    cx = fig.add_subplot(2, 2, 3)
    dx = fig.add_subplot(2, 2, 4)
    map = np.zeros((N, N), dtype=int)
    for i in range(0, N):
        for j in range(0, N):
            if (np.random.random() < val):
                map[(i, j)] = 1
    # create discrete colormap
    cmap = colors.ListedColormap(['white', 'black'])
    bounds = [0, 0.00000001, 1]
    norm = colors.BoundaryNorm(bounds, cmap.N)

    ax.imshow(map, cmap=cmap, norm=norm)

    (map4, newCost4) = anneal(map, cost4)
    print("Cost4:", cost4(map), newCost4)
    bx.imshow(map4, cmap=cmap, norm=norm)

    (map8, newCost8) = anneal(map, cost8)
    print("Cost8:", cost8(map), newCost8)
    cx.imshow(map8, cmap=cmap, norm=norm)
    #
    (map16, calc_cost816) = anneal(map, cost816)
    print("Cost816:", cost816(map), calc_cost816)
    dx.imshow(map16, cmap=cmap, norm=norm)
    plt.show()


zad1(N, 0.1)
