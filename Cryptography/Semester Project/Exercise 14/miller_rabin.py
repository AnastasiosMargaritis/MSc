import random

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

# f( x ) =  x^2 + x - 1354363
def f(x):
    return x**2 + x - 1354363

prime, coprime = 0, 0

for i in range(1000):
    rand = random.randint(1, 10**5)

    if not Miller_Rabin(abs(f(rand))):
        coprime += 1
    else:
        prime += 1

print(prime, coprime)