from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes 
import Crypto
import sympy


# Generates RSA keys.
# Generate random prime number p, q.
# Generate e = 65537 and calculate modulus inverse for d, dP, dQ, qInv with sympy.mod_inverse function. 
# Return all keys.
def RSA_keys(bits = 2048):

    # Generate p, q with Crypto.getPrime.
    p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
    e = 65537

    # Calculate d with sympy.mod_inverse.
    d = sympy.mod_inverse(e, (p - 1) * (q - 1))
    N = p * q

    # Calculate dP, dQ, qInv.
    dP = sympy.mod_inverse(e, p - 1)
    dQ = sympy.mod_inverse(e, q - 1)
    qInv = sympy.mod_inverse(1, p)

    return [p, q, e, d, N, dP, dQ, qInv]


# RSA Encryption function.
def RSA_encryption(m, e, N):
    return pow(m, e, N)


# RSA Decrypt using CRT.
def RSA_CRT_decryption(c, dP, dQ, qInv, p, q):

    m1 = pow(c, dP, p) 
    m2 = pow(c, dQ, q)
    h =  pow(qInv * (m1 - m2), 1, p)
    
    return m2 + h * q

#------------------------------------- MAIN -------------------------------
bits = int(input('How many bits you want your RSA key to be: '))
[p, q, e, d, N, dP, dQ, qInv] = RSA_keys(bits)


# Message Input. Decrypt message wit RSA_encryption function.
m = int(input('Your plaintext is: '))
c = RSA_encryption(m, e, N)
print('Your encrypted message is: ')
print(c)

# Message Decryption using RSA_CRT_decryption function.
m = RSA_CRT_decryption(c, dP, dQ, qInv, p, q)
print('Your decrypted message using CRT is: ')
print(m)




