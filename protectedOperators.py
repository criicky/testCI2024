import numpy as np

EPS = 1e-12

def protected_divide(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    # elementwise safe divide: 0 where denominator is (near) zero
    with np.errstate(divide='ignore', invalid='ignore'):
        out = np.where(np.abs(b) > EPS, a / b, 0.0)
    return out

def protected_log(a):
    a = np.asarray(a)
    # use a lower bound so log receives positive arguments
    safe = np.where(a > EPS, a, EPS)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.log(safe)

def protected_log2(a):
    a = np.asarray(a)
    safe = np.where(a > EPS, a, EPS)
    return np.log2(safe)

def protected_log10(a):
    a = np.asarray(a)
    safe = np.where(a > EPS, a, EPS)
    return np.log10(safe)

def protected_sqrt(a):
    a = np.asarray(a)
    safe = np.where(a >= 0, a, 0.0)
    return np.sqrt(safe)

def protected_power(a, b):
    a = np.asarray(a); b = np.asarray(b)
    with np.errstate(invalid='ignore', over='ignore'):
        return np.power(a, b)

def protected_mod(a, b):
    a = np.asarray(a); b = np.asarray(b)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(np.abs(b) > EPS, np.mod(a, b), 0.0)

# You can tune this list: only include the safe/protected versions you want GP to use.
unary_ops = [
    np.negative,
    np.abs,
    protected_sqrt,
    np.exp,
    protected_log,
    protected_log2,
    protected_log10,
    np.sin,
    np.cos,
    np.tan,
    np.arcsin,
    np.arccos,
    np.arctan,
    np.sinh,
    np.cosh,
    np.tanh,
    np.square,
    np.cbrt,
    np.reciprocal,
]

binary_ops = [
    np.add,
    np.subtract,
    np.multiply,
    protected_divide,
    protected_power,
    np.maximum,
    np.minimum,
    protected_mod
]
