import numpy as np
import matplotlib.pyplot as plt
import math


def graph(v):
    N = len(v)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.2  # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, v, width)

    plt.ylabel('Percentages')
    plt.title('Probabilities for a state vector')
    plt.xticks(ind)
    plt.yticks(np.arange(0, 1.1, 0.1))

    plt.show()


def mult(matriz, vector):
    v = [0 for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] += round(matriz[i][j] * vector[j],2)
    return v


def matrizProbabilities(slits, targets):
    dim = slits + targets + 1
    matriz = [[0.0 for j in range(dim)] for i in range(dim)]
    # loop
    for i in range(slits + 1, dim):
        matriz[i][i] = 1.0

    # slits
    for i in range(1, slits + 1):
        matriz[i][0] = round(1 / slits, 3)

    # targets
    j = 1
    i = slits + 1
    m = targets // 2
    m = m - m // 2
    while i <= len(matriz) - (targets // 2) and j < slits + 1:
        for k in range(i, i + targets // 2):
            matriz[k][j] = round(1 / (targets // 2), 2)
        i = i + m
        j += 1

    return matriz

def sumaComplejos(a, b):
    c = a[0] + b[0]
    d = a[1] + b[1]
    return (c, d)


def productoComplejos(a, b):
    c = a[0] * b[0] - a[1] * b[1]
    d = a[0] * b[1] + a[1] * b[0]
    return (c, d)


def multComplejos(matriz, vector):
    v = [(0, 0) for i in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector)):
            v[i] = sumaComplejos(v[i], productoComplejos(matriz[i][j], vector[j]))
    return v


def values(n):
    t = [(0, 0) for i in range(2 * n)]
    k = 0
    while k <= n:
        for i in range(2):
            for j in range(2):
                val = (round((-1) ** (i + 1) * (math.sqrt(n) / n), 3), round((-1) ** (j + i) * (math.sqrt(n) / n), 3))
                t[0 + k] = val
                k += 1
    return t


def matrizProbabilitiesC(slits, targets):
    dim = slits + targets + 1
    matriz = [[(0, 0) for j in range(dim)] for i in range(dim)]
    # loop
    for i in range(slits + 1, dim):
        matriz[i][i] = (1,0)

    # slits
    for i in range(1, slits + 1):
        val = round(1 / math.sqrt(slits), 3)
        matriz[i][0] = (val,0)

    # targets
    m = 0
    j = 1
    i = slits + 1
    m = targets // 2
    m = m - m // 2
    prob = values(targets)
    while i <= len(matriz) - (targets // 2) and j <= slits + 1:
        y= 0
        pr = prob[y]
        for k in range(i, i + targets // 2):
            matriz[k][j] = (round((1 / math.sqrt(targets // 2)) * pr[0],3),
                            round((1 / math.sqrt(targets // 2)) * prob[y][1],3))
            y += 1
        i = i + m
        j += 1

    return matriz



def clasToQuan(matriz, vector, clicks):
    for i in range(clicks):
        vector = mult(matriz, vector)
    graph(vector)
    return vector



def expRendijas(slits, targets, clicks):
    matriz = matrizProbabilities(slits, targets)
    v = [1] + [0 for i in range(len(matriz) - 1)]
    for i in range(clicks):
        v = mult(matriz, v)
    graph(v)
    return v

def expQuantic(slits, targets, clicks):
    matriz = matrizProbabilitiesC(slits,targets)
    state = [(1,0)] + [(0,0) for i in range(len(matriz)-1)]
    for i in range(clicks):
        state = multComplejos(matriz, state)
    return state
    #graph(state[0])

def main():
    print(expQuantic(3,7,1))


main()
