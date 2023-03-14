## Polynomials
Notice that genPoly creates a polynomial of degree 64 with random 1024 bit coefficients. However, at the end, it sets the constant term to $p-f(iv)%p$, where f(iv) is the polynomial that was generated.
Thus our final polynomial evaluated at iv turns out to be divisible by p. And therefore iv is a root of the polynomial mod p. 
## But the polynomial is evaluated mod n!
This is the final observation that will allow us to crack these two polynomials. 
Since iv is a common root (oh that's what the typo was!!) of both polynomials mod p, the **resultant** of the two polynomials will be congruent to 0 mod p. However, since iv is not a common root mod **n** (at least highly unlikely) the resultant of the polynomial will be incongruent to 0 mod n. 
Therefore by calculating the resultant of the two polynomials, we get a value which we can take its gcd with n to recover p, and then use it to decrypt the flag.
