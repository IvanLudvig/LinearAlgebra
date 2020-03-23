from itertools import chain


def scaleRow(row, scl):
    return [a * scl for a in row]


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]


def addRows(row1, row2):
    return [a + b for a, b in zip(row1, row2)]


def substractRows(row1, row2):
    return addRows(row1, scaleRow(row2, -1))


def swapRows(A, b, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    temp = b[i]
    b[i] = b[j]
    b[j] = temp
    return A, b


def isNull(row):
    return all(a == 0 for a in row)


def isERow(row, n, rank):
    for i in range(rank):
        if i != n:
            if row[i] != 0:
                return False
        else:
            if row[i] != 1:
                return False
    return True


def isECol(A, i, n):
    return isERow([A[j][i] for j in range(len(A))], n, len(A))


def Gauss(A, b):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            if(A[i][j]<=1e-8):
                A[i][j]=0
            if A[i][j] != 0:
                b[i] /= A[i][j]
                A[i] = scaleRow(A[i], 1 / A[i][j])
                for k in chain(range(i), range(i + 1, n)):
                    b[k] -= A[k][j] * b[i]
                    A[k] = substractRows(A[k], scaleRow(A[i], A[k][j]))
                break
    return A, b


def delNullRows(A, b):
    n = len(A)
    for i in range(n):
        if isNull(A[i]):
            A = [A[j] for j in chain(range(i), range(i + 1, n))]
            b = [b[j] for j in chain(range(i), range(i + 1, n))]
            return delNullRows(A, b)
    return A, b


def getERank(A):
    n = len(A)
    m = len(A[0])
    r = 0
    for i in range(min(m, n)):
        t = 0
        for j in range(m):
            if isECol(A, i, j):
                t = 1
                break
        if t == 1:
            r += 1
    return r


def calcRank(M):
    A = M.copy()
    A, b = Gauss(A, [0] * len(A))
    A, b = delNullRows(A, b)
    return getERank(A)


def sortRows(A, b):
    n = len(A)
    m = len(A[0])
    rank = getERank(A)
    for j in range(n):
        for i in range(n):
            if isERow(A[i], j, rank):
                A, b = swapRows(A, b, i, j)
    return A, b


def solution(A, b):
    n = len(A)
    m = len(A[0])
    rank = getERank(A)
    F = []
    c = [round(b[i], 6) for i in range(rank)]
    for i in range(rank):
        temp = []
        for j in range(rank, m):
            temp.append(-1 * round(A[i][j], 6))
        F.append(temp)
    for i in range(rank, m):
        c.append(0)
        temp = []
        for j in range(rank, m):
            temp.append(1 if j == i else 0)
        F.append(temp)
    return F, c


def solve(A, b):
    A, b = Gauss(A, b)
    A, b = delNullRows(A, b)
    A, b = sortRows(A, b)
    return solution(A, b)

#F, c = solve([[-1, -3, 1, -4], [-3, -5, -1, -8], [0, 2, -2, 2], [3, 3, 3, 6]], [0, 0, 0, 0])
# F, c = solve( [ [8, -2, -2], [0, 1, -1] ], [0, 0] )
# print("F: ", F)
# print("c: ", c)
