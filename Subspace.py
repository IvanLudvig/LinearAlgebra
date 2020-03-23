from itertools import chain
import Gauss


def basis(L):
    L1 = L.copy()
    i = len(L) - 1
    k = 1
    while Gauss.calcRank(L1) != len(L1):
        L1 = [L[j] for j in chain(range(i), range(i + k, len(L)))]
        i -= 1
        if i == 0:
            i = len(L) - 1
            k += 1
    return L1


def addition(L1, L2):
    return basis(L1+L2)


def intersection(L1, L2):
    F, c = Gauss.solve(Gauss.transpose(basis(L1) + ([Gauss.scaleRow(v, -1) for v in basis(L2)])), [0] * len(U[0]))
    dim = len(basis(L1)) + len(basis(L2)) - len(basis(L1 + L2))
    B = []
    for i in range(len(F[0])):
        temp = [0] * len(L1[0])
        for j in range(len(basis(L1))):
            temp = Gauss.addRows(temp, Gauss.scaleRow(basis(L1)[j], F[j][i]))
        B.append(temp)
    return B

# U = [[1, 1, 1], [4, 2, 1], [2, 0, -1]]
# V = [[-2, 3, 1], [1, 4, 1], [5, -2, -1]]
# U = [ [3, 5, 2], [5, 9, 6] ]
# V = [[1, 2, 2]]
# print(addition(U, V))
# print(intersection(U, V))
