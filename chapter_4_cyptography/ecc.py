"""
Taken from: 
https://medium.com/asecuritysite-when-bob-met-alice/adding-points-in-elliptic-curve-cryptography-a1f0a1bce638

Nomenclature:

a, b, p refer to the coefficients in an elliptic curve: y^2 % p = (x^3 + ax + b) % p

"""

import sys
from typing import Tuple


def modular_sqrt(a, p):
    """Find a quadratic residue (mod p) of 'a'. p
    must be an odd prime.

    Solve the congruence of the form:
        x^2 = a (mod p)
    And returns x. Note that p - x is also a root.

    0 is returned if no square root exists for
    these a and p.

    The Tonelli-Shanks algorithm is used (except
    for some simple cases in which the solution
    is known from an identity). This algorithm
    runs in polynomial time (unless the
    generalized Riemann hypothesis is false).
    """
    # Simple cases
    #
    if legendre_symbol(a, p) != 1:
        return 0
    elif a == 0:
        return 0
    elif p == 2:
        return p
    elif p % 4 == 3:
        return pow(a, (p + 1) / 4) % p

    # Partition p-1 to s * 2^e for an odd s (i.e.
    # reduce all the powers of 2 from p-1)
    #
    s = p - 1
    e = 0
    while s % 2 == 0:
        s /= 2
        e += 1

    # Find some 'n' with a legendre symbol n|p = -1.
    # Shouldn't take long.
    #
    n = 2
    while legendre_symbol(n, p) != -1:
        n += 1

    # Here be dragons!
    # Read the paper "Square roots from 1; 24, 51,
    # 10 to Dan Shanks" by Ezra Brown for more
    # information
    #

    # x is a guess of the square root that gets better
    # with each iteration.
    # b is the "fudge factor" - by how much we're off
    # with the guess. The invariant x^2 = ab (mod p)
    # is maintained throughout the loop.
    # g is used for successive powers of n to update
    # both a and b
    # r is the exponent - decreases with each update
    #
    x = pow(a, (s + 1) / 2) % p
    b = pow(a, s) % p
    g = pow(n, s) % p
    r = e

    while True:
        t = b
        m = 0
        for m in range(r):
            if t == 1:
                break
            t = pow(t, 2) % p

        if m == 0:
            return x

        gs = pow(g, 2 ** (r - m - 1)) % p
        g = (gs * gs) % p
        x = (x * gs) % p
        b = (b * g) % p
        r = m


def legendre_symbol(a, p):
    """Compute the Legendre symbol a|p using
    Euler's criterion. p is a prime, a is
    relatively prime to p (if p divides
    a, then a|p = 0)

    Returns 1 if a has a square root modulo
    p, -1 otherwise.
    """
    ls = pow(a, (p - 1) / 2) % p
    return -1 if ls == p - 1 else ls


def modinv(a, m):
    """Inverse of a mod m."""

    if a == 0:  # pragma: no branch
        return 0

    lm, hm = 1, 0
    low, high = a % m, m
    while low > 1:  # pragma: no branch
        r = high // low
        lm, low, hm, high = hm - lm * r, high - low * r, lm, low

    return lm % m


def find_y(x: int, p: int, a: int = 0, b: int = 7) -> int:
    z = (x ** 3 + a * x + b) % p
    return int(modular_sqrt(z, p))


def ecc_addition_no_y(x1: int, x2: int, p: int, a: int = 0, b: int = 7):
    y1, y2 = find_y(x1, a, b, p), find_y(x2, a, b, p)
    s = (y2 - y1) * modinv(x2 - x1, p)
    x3 = (s ** 2 - x2 - x1) % p
    y3 = ((s * (x2 - x3) - y2)) % p
    return x3, y3


def ecc_addition(
    p1: Tuple[int, int], p2: Tuple[int, int], p: int, a: int = 0, b: int = 7
):
    x1, y1 = p1
    x2, y2 = p2
    if p1 == p2:
        s = 0
    else:
        s = (y2 - y1) * modinv(x2 - x1, p)
    x3 = (s ** 2 - x2 - x1) % p
    y3 = ((s * (x2 - x3) - y2)) % p
    return x3, y3


def _is_on_curve(
    x: int,
    y: int,
    p: int,
    a: int = 0,
    b: int = 7,
):
    return ((x ** 3 + x * a + b - y ** 2) % p) == 0


def main():
    # k = 0xf8f8a2f43c8376ccb0871305060d7b27b0554d2cc72bccf41b2705608452f315
    g = (
        0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
        0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
    )
    p = 115792089237316195423570985008687907853269984665640564039457584007908834671663

    print(_is_on_curve(ecc_addition(g, g, p)))


if __name__ == "__main__":
    import logging

    logging.basicConfig(level=logging.INFO)
    main()
