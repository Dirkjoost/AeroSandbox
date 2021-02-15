import numpy as onp
import casadi as cas
from aerosandbox.numpy.array import length


def sum(x):
    """Returns the sum of a vector x."""
    try:
        return onp.sum(x)
    except Exception:
        return cas.sum1(x)


def mean(x):
    """Returns the mean of a vector x."""
    return sum(x) / length(x)

def cumsum(x, **kwargs):
    """Return the cumulative sum of the elements."""
    
    try:
        return onp.cumsum(x, **kwargs)
    except Exception:
        return cas.cumsum(x, **kwargs)