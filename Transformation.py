import Gauss
import Subspace


def ker(A):
    M = A.copy()
    F, c = Gauss.solve(M, [0]*len(M))
    return F

def Im(A):
    M = A.copy()
    return Subspace.basis(Gauss.transpose(M))


# A = [[0, 1, 1], [1, 1, 0], [-1, 0, 1]]
# print(ker(A))
# print(Im(A))