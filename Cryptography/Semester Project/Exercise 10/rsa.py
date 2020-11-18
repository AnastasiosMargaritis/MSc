# Returns the prime factors of the number N.
def factors_of_number(N):

    factors = [2, 3]

    for i in range(4, N + 1):
        if N % i == 0 and (i % 2 != 0 and i % 3 != 0): factors.append(i)
    
    return factors

# Potential key
def decryption_key(e, F):

    d = 1
    keys = []
    counter = 0

    while(counter < 15):
        if( (d * e) % F == 1): 
            keys.append(d)
            counter += 1

        d +=1
    
    return keys
    
# Calculates a^g mod N.
def fast(a, g, N):
    # Convert exponent to bits
    g = list(bin(g)[2:])
    g.reverse()

    x = a
    d = 1


    for i in range(0, len(g)):

        if g[i] == '1':
            d = (d*x) % N
        
        x = x**2 % N

    return d


# Decryption function
def decrypt(C, keys):
    
    d = {}
    for key in keys:
        d[key] = []
        for char in C:
           d[key].append(chr(fast(char, key, N)))

    return d 


# Public key of RSA.
N = 11413
e = 19

print(factors_of_number(N))

# Our encrypted text
C=[3203,909,3143,5255,5343,3203,909,9958,5278,5343,9958,5278,4674,909,9958,792,909,4132,3143,9958,3203,5343,792,3143,4443]

# Based on the prime factors I choose the
# pair of my prime number for the RSA.
p, q = 101, 113

# Calculates Φ(Ν)
F = (p - 1) * (q - 1)

# Potential keys
keys = decryption_key(e, F)

print(decrypt(C, keys))

# So, the final message is 'welcome to the real world'
