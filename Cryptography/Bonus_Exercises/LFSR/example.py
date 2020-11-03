import re

#Function for completely remove duplicates
def rdups(variable):
    if primary_polynomial.count(variable) > 1:
        return False

    return True

x = PolynomialRing(GF(2), 'x').gen()

#Size of the problem, only even numbers will produce results
N = 6

divisor = divisors(2**(N)-1)[1:]

factors = []

#Calculate the factors of the polynomials for each divisor
for div in divisor:
    factors.append(str(factor(x**div - 1)))

primary_polynomial = []

for factor in factors:
    
    #Erasing the (x+1) factor from all polynomials
    factor = factor[10:]
    
    #Creating a list of each individual factor
    factor = re.split('[*]', factor)
    
    #Storing only the highest rank polynomials of each factorization
    for poly in factor:
        if(poly.find('x^' + str(N)) != -1): primary_polynomial.append(poly.replace(' ',''))
                
#Completely remove duplicates    
primary_polynomial = list(filter(rdups, primary_polynomial))

#Print primary_polynomials
primary_polynomial