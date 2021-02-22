"""
Created on Sun Dec 13 21:02:02 2020

@author: ishan

Cryptography Project
This an implementation of basic operations on Homomorphic Encrypted data from basic libraries 
"""


"""
First define the operations that we we need on our ring, a ring takes two operations. As is usually
taken, we take addition and multiplication as the two operations tp define our ring. As these are 
defined over a ring we need to consider a modulus and a polynomial modulus
"""

import numpy as np
from numpy.polynomial import polynomial as poly

def mul_poly(x, y, mod_coeff, mod_poly):
    """
    Takes:
        x, y: the two polynoms to be added.
        mod_coeff: coefficient modulus.
        mod_poly: polynomial modulus.
    Returns:
        A polynomial in Z_modulus[X]/(poly_mod).
        
    Multiplies the two polynoms x and y.
    """
    # It is important to explicitly typecast the sum returned as 64-bit
    return np.int64(
        np.round(poly.polydiv(poly.polymul(x, y) % mod_coeff, mod_poly)[1] % mod_coeff)
    )


def add_poly(x, y, mod_coeff, mod_poly):
    """
    Takes:
        x, y: the two polynoms to be multiplied.
        mod_coeff: coefficient modulus.
        mod_poly: polynomial modulus.
    Returns:
        A polynomial in Z_modulus[X]/(poly_mod).
        
    Adds the two polynoms x and y.
    """
    return np.int64(
        np.round(poly.polydiv(poly.polyadd(x, y) % mod_coeff, mod_poly)[1] % mod_coeff)
    )

"""
Next we need to generate our keys, that we will use for HE. Our secret key sk will be randomly sampled
from a uniform distribution over R2 and public key will be of the form ([-(a . sk) + e] mod q, a)
"""

def poly_binary_gen(size):
    """
    Takes:
        size: number of coeffcients, size-1 being the degree of the
            polynomial.
    Returns:
        array of coefficients with the coeff[i] being 
        the coeff of x ^ i.
    Generates a polynomial with coeffecients in [0, 1]
    """
    return np.random.randint(0, 2, size, dtype=np.int64)


def poly_uniform_gen(size, modulus):
    """
    Takes:
        size: number of coeffcients, size-1 being the degree of the
            polynomial.
    Returns:
        array of coefficients with the coeff[i] being 
        the coeff of x ^ i.
    Generates a polynomial with coeffecients being integers in Z_modulus
    """
    return np.random.randint(0, modulus, size, dtype=np.int64)


def poly_normal_gen(size):
    """
    Takes:
        size: number of coeffcients, size-1 being the degree of the
            polynomial.
    Returns:
        array of coefficients with the coeff[i] being 
        the coeff of x ^ i.
    Generates a polynomial with coeffecients in a normal distribution
    of 0 mean and a standard deviation of 2, then discretize it by converting to integer.
    """
    return np.int64(np.random.normal(0, 2, size=size))

def gen_key(size, modulus, mod_poly):
    """
    Takes:
        size: size of the polynoms for the public and secret keys.
        modulus: coefficient modulus.
        poly_mod: polynomial modulus.
    Returns:
        Public and secret key.
    Generates a public and secret key
    """
    sk = poly_binary_gen(size)
    a = poly_uniform_gen(size, modulus)
    e = poly_normal_gen(size)
    b = add_poly(mul_poly(-a, sk, modulus, mod_poly), -e, modulus, mod_poly)
    return (b, a), sk

"""
Finally we define our encryption and decryption functions
"""

def encrypt(pk, size, q, t, mod_poly, pt):
    """
    Takes:
        pk: public-key.
        size: size of polynomials.
        q: ciphertext modulus.
        t: plaintext modulus.
        mod_poly: polynomial modulus.
        pt: integer to be encrypted.
    Returns:
        Tuple representing a ciphertext. 
    Encrypts a plaintext(integer in this case)
    """
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    delta = q // t
    scaled_m = delta * m  % q
    e1 = poly_normal_gen(size)
    e2 = poly_normal_gen(size)
    u = poly_binary_gen(size)
    ct0 = add_poly(
            add_poly(
                mul_poly(pk[0], u, q, mod_poly),
                e1, q, mod_poly),
            scaled_m, q, mod_poly
        )
    ct1 = add_poly(
            mul_poly(pk[1], u, q, mod_poly),
            e2, q, mod_poly
        )
    return (ct0, ct1)

def decrypt(sk, size, q, t, mod_poly, ct):
    """
    Takes:
        sk: secret-key.
        size: size of polynomials.
        q: ciphertext modulus.
        t: plaintext modulus.
        mod_poly: polynomial modulus.
        ct: ciphertext.
    Returns:
        Integer representing the plaintext.
    Decrypts a ciphertext
    """
    scaled_pt = add_poly(
            mul_poly(ct[1], sk, q, mod_poly),
            ct[0], q, mod_poly
        )
    decrypted_poly = np.round(scaled_pt * t / q) % t
    return int(decrypted_poly[0])

"""
We still need to define our functions for computation on encrypted data
"""

def add_plain(ct, pt, q, t, mod_poly):
    """
    Takes:
        ct: ciphertext.
        pt: integer to add.
        q: ciphertext modulus.
        t: plaintext modulus.
        mod_poly: polynomial modulus.
    Returns:
        Tuple representing a ciphertext.
    Adds a ciphertext and a plaintext.
    """
    size = len(mod_poly) - 1
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    delta = q // t
    scaled_m = delta * m  % q
    new_ct0 = add_poly(ct[0], scaled_m, q, mod_poly)
    return (new_ct0, ct[1])

def mul_plain(ct, pt, q, t, mod_poly):
    """
    Takes:
        ct: ciphertext.
        pt: integer to multiply.
        q: ciphertext modulus.
        t: plaintext modulus.
        mod_poly: polynomial modulus.
    Returns:
        Tuple representing a ciphertext.
    Multiplies a ciphertext and a plaintext.
    """
    size = len(mod_poly) - 1
    # encode the integer into a plaintext polynomial
    m = np.array([pt] + [0] * (size - 1), dtype=np.int64) % t
    new_c0 = mul_poly(ct[0], m, q, mod_poly)
    new_c1 = mul_poly(ct[1], m, q, mod_poly)
    return (new_c0, new_c1)

"""
Running the program
Sample code:
# Scheme's parameters
# polynomial modulus degree
n = 2**4
# ciphertext modulus
q = 2**15
# plaintext modulus
t = 2**8
# polynomial modulus
mod_poly = np.array([1] + [0] * (n - 1) + [1])
# Keygen
pk, sk = gen_key(n, q, mod_poly)
# Encryption
pt1, pt2 = 73, 20
cst1, cst2 = 7, 5
ct1 = encrypt(pk, n, q, t, mod_poly, pt1)
ct2 = encrypt(pk, n, q, t, mod_poly, pt2)

print("[+] Ciphertext ct1({}):".format(pt1))
print("")
print("\t ct1_0:", ct1[0])
print("\t ct1_1:", ct1[1])
print("")
print("[+] Ciphertext ct2({}):".format(pt2))
print("")
print("\t ct1_0:", ct2[0])
print("\t ct1_1:", ct2[1])
print("")

# Evaluation
ct3 = add_plain(ct1, cst1, q, t, mod_poly)
ct4 = mul_plain(ct2, cst2, q, t, mod_poly)

# Decryption
decrypted_ct3 = decrypt(sk, n, q, t, mod_poly, ct3)
decrypted_ct4 = decrypt(sk, n, q, t, mod_poly, ct4)

print("[+] Decrypted ct3(ct1 + {}): {}".format(cst1, decrypted_ct3))
print("[+] Decrypted ct4(ct2 * {}): {}".format(cst2, decrypted_ct4))
"""
