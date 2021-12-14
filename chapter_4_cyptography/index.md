# Chapter 4: Cryptography

## Elliptic Curve Arithmetic

$P_3 = P_1 + P_2$

Each point is `(x, y int)`

The `+` operator works like:
* Draw a line from $P_1$ to $P_2$ 
* This will interset the elliptic curve in only one place, (x, y)
* $P_3 = (x, -y)$