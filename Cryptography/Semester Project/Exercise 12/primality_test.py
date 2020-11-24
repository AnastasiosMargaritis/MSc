import random
import math

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

# Generates a random n-bit number.
def nBitRandom(n): 
    return random.randrange(2**(n-1)+1, 2**n - 1) 

# Fermat's primality test.
def fermat(n):

    while(True):
        p = nBitRandom(n)
        a = 2

        if(math.gcd(a, p) == 1 and fast(a, p - 1, p) == 1):
            return p


# Finds d,r so as n - 1 = d * 2^r
def calculate_d_r(n):
    r = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        r += 1
    
    return d, r

# Examines Miller-Rabin conditions for prime numbers:
# Returns False if conditions are met and True if number is
# coprime.
def Miller_Rabin_conditions(rand_num, d, r, a):
    if pow(rand_num, d, a) == 1: 
        return False
    for i in range(r): 
        if pow(rand_num, 2**i * d, a) == a-1: 
            return False
    return True

# Miller-Rabin primality test.
def Miller_Rabin(a): 

    # Calculates d,r such as a - 1 = d * 2^r
    d, r = calculate_d_r(a)
    
    # Pick 20 random number rand_num in [2, a) and check:
    # if rand_num ^ d % a == 1 and for j in 0 <= j <= r - 1
    # rand_num ^ (2^i * d) % a == a - 1, which are the 
    # Miller-Rabin conditions for primality.
    for i in range(20): 
        rand_num = random.randrange(2, a) 
        if Miller_Rabin_conditions(rand_num, d, r, a): 
            return False
    return True

# Safe prime calculator.
def safe_prime(n):

    while(True):
        a = nBitRandom(n)

        if(Miller_Rabin(a) and Miller_Rabin(2*a + 1)):
            return a


#---------------------------------Fermat's primality test------------------------------------------
# Since we want 2048 bits, n = 2048
# n = 2048

# print('A prime number of 2048 bits with Fermat primality test is: ')
# print(fermat(n))


#------------------------------Miller Rabin method-------------------------------------------------

#For 1300 bits.
n = 1300
while True:
    a = nBitRandom(n)
    if not Miller_Rabin(a):
        continue
    else:    
        print('A prime number of 1300 bits with Miller-Rabin primality test is: ')
        print(a)
        break


#-----------------------------Safe prime-----------------------------------------------------------
# For 3000 bits
# n = 3000
# print('A safe prime number of 3000 bits is: ')
# print(safe_prime(n))

