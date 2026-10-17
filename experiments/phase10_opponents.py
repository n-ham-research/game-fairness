"""Exact finite hidden-order security; common action chosen before class."""
from fractions import Fraction as F
from itertools import combinations


def hidden_value_two_actions(classes, prior):
    """Piecewise-linear enumeration for two actions, any finite classes."""
    points={F(0),F(1)}
    for matrix in classes:
        for j,k in combinations(range(len(matrix[0])),2):
            slope=(matrix[0][j]-matrix[1][j])-(matrix[0][k]-matrix[1][k])
            if slope:
                p=F(matrix[1][k]-matrix[1][j])/slope
                if 0<=p<=1:points.add(p)
    def guarantee(p):
        return sum(w*min(p*x+(1-p)*y for x,y in zip(matrix[0],matrix[1])) for w,matrix in zip(prior,classes))
    return max((guarantee(p),p) for p in points)


def reactive_value(classes, prior):
    return max(sum(w*min(matrix[a]) for w,matrix in zip(prior,classes)) for a in range(len(classes[0])))


def common_minimizers(matrix):
    return set.intersection(*({t for t,x in enumerate(row) if x==min(row)} for row in matrix))


def hidden_plan(matrix, sigma):
    return min(sum(p*row[t] for p,row in zip(sigma,matrix)) for t in range(len(matrix[0])))


def reactive_plan(matrix,sigma):return sum(p*min(row) for p,row in zip(sigma,matrix))
