import cmath


# Calculates the fractions of e/N.
# Returns a list of fractions.
def calc_fractions(N, e):

    fractions = []

    while(e % N != 0):
        fractions.append(e // N)
        e -= (e // N) * N
        e, N = N, e

    fractions.append(e // N)

    return fractions

# Calculates continued fractions based on a
# list of fractions.
def calc_continued_fractions(fractions):

    # First two elements don't need recursion.
    cf = [[1, fractions[1]]]

    for i in range(2, len(fractions)):

        numenator = fractions[i]
        denominator = numenator * fractions[i - 1] + 1

        for j in range(i - 1, 1, -1):
            t = numenator
            numenator = denominator
            denominator = denominator * fractions [j-1] + t
        
        cf.append([numenator, denominator])
    
    return cf


# Calculates Φ(Ν) and stores only integer values.
# Cleans continued_fractions list from pairs that doesn't
# produce integer Φ(Ν).
def calc_f(continued_fractions, e):

    Fn = []
    possible_keys = []

    for pair in continued_fractions:
        f = (e * pair[1] -1) / pair[0]
        if (f % 1 == 0.0):
            Fn.append(f)
            possible_keys.append(pair)
       
    
    return Fn, possible_keys

# Calculates roots of quadradic equation.
def quadradic_roots(N, Fn):

    roots = []

    for fn in Fn:
        a = 1
        b = N - fn + 1
        c = N

        # Calculate the discriminant.
        d = (b ** 2) - (4 * a * c)

        root1 = (-b-cmath.sqrt(d))/(2*a)
        root2 = (-b+cmath.sqrt(d))/(2*a)

        roots.append([root1, root2])

    
    return roots


# Public key of RSA. 
N = 194749497518847283
e = 50736902528669041

# Calculate the fraction vector.
fractions = calc_fractions(N, e)

# Extract all the continued fractions from the fraction vector.
continued_fractions = calc_continued_fractions(fractions)

# Calculate Φ(Ν) and eliminate non valiable pairs.
Fn, possible_keys = calc_f(continued_fractions, e)

# For each Φ(Ν) calculate the roots of the quadradic equation.
prime_numbers = quadradic_roots(N, Fn)

