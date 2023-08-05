import random
from secret import getCurveParam
from Crypto.Util.number import inverse
from sympy.ntheory.residue_ntheory import nthroot_mod


class EllipticCurve:
    def __init__(self, p, a, b):
        self.p = p
        self.a = a
        self.b = b

    def __str__(self):
        return f'EllipticCurve({self.p},{self.a},{self.b})'

    def add(self, P1, P2):
        x1, y1 = P1
        x2, y2 = P2
        if x1 == 0:
            return P2
        elif x2 == 0:
            return P1
        elif x1 == x2 and (y1 + y2) % self.p == 0:
            return (0, 0)
        if P1 == P2:
            lamb = (3 * x1 * x1 + self.a) * inverse(2 * y1, self.p) % self.p
        else:
            lamb = (y2 - y1) * inverse(x2 - x1, self.p) % self.p
        x3 = (lamb * lamb - x1 - x2) % self.p
        y3 = (lamb * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def mul(self, P, k):
        assert k >= 0
        Q = (0, 0)
        while k > 0:
            if k % 2:
                k -= 1
                Q = self.add(P, Q)
            else:
                k //= 2
                P = self.add(P, P)
        return Q


def genCurve():
    p, a, b = getCurveParam()
    curve = EllipticCurve(p, a, b)
    return curve


def genPoint(curve):
    a, b, p = curve.a, curve.b, curve.p
    while True:
        try:
            x = random.randint(1, p)
            y = nthroot_mod(x**3 + a * x + b, 2, p, all_roots=False)
            assert y * y % p == (x**3 + a * x + b) % p
            break
        except:
            continue
    G = (x, y)
    return G
