"""Exact timing values for independently encoded commitments."""
from fractions import Fraction as F


def values(rows, lottery):
    blind=max(sum(w*r[a] for w,r in zip(lottery,rows)) for a in range(len(rows[0])))
    informed=sum(w*max(r) for w,r in zip(lottery,rows))
    return blind,informed


def common_maximizers(rows):
    return set.intersection(*({a for a,v in enumerate(r) if v==max(r)} for r in rows))


def reversal(prior):
    return ((prior,1-prior),(1-prior,prior))
