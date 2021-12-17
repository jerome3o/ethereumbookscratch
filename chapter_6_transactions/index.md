# Chapter 6: Transactions

## Notes

* Web3 no longer injest web3?

## Helpful links

* [ETH Gas Station](https://ethgasstation.info/)
* [Explanation of ECDSA](https://www.instructables.com/Understanding-how-ECDSA-protects-your-data/)
* Slightly more detailed ECDSA descriptions
  * [Lecture 14](https://engineering.purdue.edu/kak/compsec/NewLectures/Lecture14.pdf)
  * [cs miami edu](https://www.cs.miami.edu/home/burt/learning/Csc609.142/ecdsa-cert.pdf)

## ECDSA Arithmetic

### Definitions

$a$: Elliptic curve parameter (order 1)

$b$: Elliptic curve parameter (order 0)

$p$: Prime number modulo

$N$: Number of points in the elliptic curve

$G$: Generator / Reference point

$dA$: Private key (random number)

$Qa$: Public key ($Qa = G * dA$)

$k$: Ephemeral private key (random number)

$P$: Ephemeral public key ($P = k * G$)

$R$: The x value of $P$

$S$: Second component of the signature, defined by:

$S = k^{-1} (z + dA * R) mod p$

### Verification

To verify the signature, the public key $Qa$ is used:

$P = S^{-1}*z*G + S^{-1}*R*Qa$

### Simplification

We have:

$P = S^{-1}*z*G + S^{-1}*R*Qa$

But $Qa = dA * G$ so:

$P = S^{-1}*z*G + S^{-1}*R*dA*G = S^{-1}(z + dA*R)*G$

And if the signature is valid, then $P=k*G$ so:

$k*G = S^{-1}(z + dA*R)*G$

Simply by cancelling $G$

$k = S^{-1}(z + dA*R)$

Invert $k$ and $S$

$S = k^{-1}(z + dA*R)$

This is the original equation for $S$