import matplotlib.pyplot as plt
import math

def mag(x, y):
    return math.sqrt(x**2 + y**2)

def evalMatrix(fn, numpoints=10):
    mat = createMatrix(numpoints, numpoints)
    for i in range(len(mat)):
            for j in range(len(mat)):
                    y = i / float(numpoints-1) * 2 - 1
                    x = j / float(numpoints-1) * 2 - 1
                    mat[i][j] = fn(x, y)
    return mat

def createMatrix(rows, cols):
    mat = []
    for _ in range(rows):
            row = []
            for _ in range(cols):
                    row.append([])
            mat.append(row)
    return mat

def toColors(mat):
    return list(map(lambda x: map(lambda y: y / math.sqrt(2), x), mat))

def y_grid(numpoints):
    mat = createMatrix(numpoints, numpoints)
    for i in range(numpoints):
            for j in range(numpoints):
                    y = i / float(numpoints-1) * 2 - 1
                    mat[i][j] = y
    return mat

def x_grid(numpoints):
    mat = createMatrix(numpoints, numpoints)
    for i in range(numpoints):
            for j in range(numpoints):
                    x = j / float(numpoints-1) * 2 - 1
                    mat[i][j] = x
    return mat


def plot3d(fn, numpoints=100):
    plt.scatter(x_grid(numpoints), y_grid(numpoints), cmap="plasma", c=toColors(evalMatrix(fn, numpoints)), edgecolors='face', vmin=0, vmax=1)
    plt.show()

def plot2d(fn, numpoints=1000):
    mat = createMatrix(1, numpoints)
    x_mat = createMatrix(1, numpoints)
    for i in range(numpoints):
        x = i / float(numpoints - 1) * 2 - 1
        x_mat[0][i] = x
        mat[0][i] = fn(x)
    plt.scatter(x_mat, mat, c=mat, edgecolors='face', cmap="plasma", vmin=-1, vmax=1)
    plt.show()

    
