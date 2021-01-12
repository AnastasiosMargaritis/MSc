
# Function to define if a number is composite.
def isComposite(n): 
  
    # Corner cases 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return False
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0): 
        return True
    i = 5
    while(i * i <= n): 
          
        if (n % i == 0 or n % (i + 2) == 0): 
            return True
        i = i + 6
          
    return False

# Function to check if a number n is strong pseudoprime 
# to base a. 
def isStrongPseudoprime(n, a):
    d, s = calculate_d_s(n)

    t = pow(a, int(d), n)
    if t == 1:
        return True
    while s > 0:
        if t == n - 1:
            return True
        t, s = pow(t, 2, n), s - 1
    return False

# Finds d,r so as n - 1 = d * 2^r
def calculate_d_s(n):
    r = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        r += 1
    
    return d, r


# Finding all odd composites from 1 to 1000
# and storing them in a list.
odd_copmposites = []
for i in range(1, 1000):
    if(isComposite(i) and i % 2 == 1):
        odd_copmposites.append(i)


for odd_copmposite in odd_copmposites:

    if(isStrongPseudoprime(odd_copmposite, 32)):
        print('Smallest possible strong pseudoprime with base 32 is: ')
        print(odd_copmposite)
        break



