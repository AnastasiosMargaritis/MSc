def isStrongPseudoprime(n, a):
    d, s = n-1, 0
    while d % 2 == 0:
        d, s = d/2, s+1

    t = pow(a, int(d), n)
    if t == 1:
        return True
    while s > 0:
        if t == n - 1:
            return True
        t, s = pow(t, 2, n), s - 1
    return False


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


# Finding all odd composites from 1 to 100
# and storing them in a list.
odd_copmposites = []
for i in range(1, 100):
    if(isComposite(i) and i % 2 == 1):
        odd_copmposites.append(i)

for odd_copmposite in odd_copmposites:
    print(isStrongPseudoprime(odd_copmposite, 32))
