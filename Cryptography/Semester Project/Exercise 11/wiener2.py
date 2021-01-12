import math
import base64


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
        f = (e * pair[1] -1) // pair[0]
        if (f % 1 == 0.0):
            Fn.append(f)
            possible_keys.append(pair)
       
    
    return Fn, possible_keys

# Calculates roots of quadradic equation.
def quadratic_roots(N, Fn):

    roots = []

    for fn in Fn:
        a = 1
        b = (N - fn) + 1
        c = N

        # Calculate the discriminant.
        d = (b ** 2) - (4 * a * c)

        if d >= 0 and (int(math.sqrt(d) + 0.5) ** 2 == d):
            root1 = (-b + math.sqrt(d))/ 2 * a
            root2 = (-b - math.sqrt(d))/ 2 * a
            f = fn
            
    return [abs(root1), abs(root2)], Fn.index(f)

# Decryption function
def decrypt(C, N, key):
    d = []

    for char in C:
        d.append(chr(fast(int(char), key, N)))

    return d 


# Public key of RSA. 
N = 22009517030106990383763465105609899090941157494196382925533444156480589292450396529663642850138695190588855805260835175270086166355060564256148792439233592472232233056950905840539154677121486094877597472487300649250039699499067065703656740364634411636945242292939908153976592139191106268327154757211809894086104466154946604045715191337979340318964774322733014276440202233403512948667806285436385349767243073268946721052707444588507283401697641243190019700333343119537943616295162029028870293037484015297179234631401220439538481352300280727764959004584544520437625051512885404930600391580169572809550082972986630285267
e = 65537

# Cipher text.
C = 'Qz1bNDc0MDYyNjMxOTI2OTM1MDksNTEwNjUxNzgyMDExNzIyMjMsMzAyNjA1NjUyMzUxMjg3MDQsODIzODU5NjMzMzQ0MDQyNjgNCjgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDksMTc4Mjc1OTc3MzM2Njk2NDQyLDEzNDQzNDI5NTg5NDgwMzgwNg0KMTEyMTExNTcxODM1NTEyMzA3LDExOTM5MTE1MTc2MTA1MDg4MiwzMDI2MDU2NTIzNTEyODcwNCw4MjM4NTk2MzMzNDQwNDI2OA0KMTM0NDM0Mjk1ODk0ODAzODA2LDQ3NDA2MjYzMTkyNjkzNTA5LDQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OA0KMzAyNjA1NjUyMzUxMjg3MDQsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDQ3NDA2MjYzMTkyNjkzNTA5DQoxMTIxMTE1NzE4MzU1MTIzMDcsNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMTkzOTExNTE3NjEwNTA4ODIsMTEyMTExNTcxODM1NTEyMzA3LDgxNjkxNTY2NjM5Mjc5MjksMTM0NDM0Mjk1ODk0ODAzODA2DQo1NzIwODA3Nzc2NjU4NTMwNiw0NzQwNjI2MzE5MjY5MzUwOSwxODU1ODIxMDUyNzUwNTA5MzIsMTc0NjMyMjI5MzEyMDQxMjQ4DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsODIzODU5NjMzMzQ0MDQyNjgsMTcyNTY1Mzg2MzkzNDQzNjI0LDEwNjM1NjUwMTg5MzU0NjQwMQ0KODE2OTE1NjY2MzkyNzkyOSw0NzQwNjI2MzE5MjY5MzUwOSwxMDM2MTA1OTcyMDYxMDgxNiwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjExOTM5MTE1MTc2MTA1MDg4MiwxNzI1NjUzODYzOTM0NDM2MjQsNDc0MDYyNjMxOTI2OTM1MDksODE2OTE1NjY2MzkyNzkyOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDkNCjQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OCwzMDI2MDU2NTIzNTEyODcwNCw0NzQwNjI2MzE5MjY5MzUwOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDExMTUyMzQwODIxMjQ4MTg3OSwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjQ3NDA2MjYzMTkyNjkzNTA5LDExMjExMTU3MTgzNTUxMjMwNyw1Mjg4Mjg1MTAyNjA3MjUwNywxMTkzOTExNTE3NjEwNTA4ODINCjU3MjA4MDc3NzY2NTg1MzA2LDExOTM5MTE1MTc2MTA1MDg4MiwxMTIxMTE1NzE4MzU1MTIzMDcsODE2OTE1NjY2MzkyNzkyOQ0KMTM0NDM0Mjk1ODk0ODAzODA2LDU3MjA4MDc3NzY2NTg1MzA2XQ=='

# Base64 Decoding (ASCII)
base64_bytes = C.encode('ascii')
message_bytes = base64.b64decode(base64_bytes)
C = message_bytes.decode('ascii')
    
# variable cipher is string, so we should format it into a list
C = C[3:-1]
C = C.replace('\r\n', ',').strip()
C = C.split(',')

# Calculate the fraction vector.
fractions = calc_fractions(N, e)

# Extract all the continued fractions from the fraction vector.
continued_fractions = calc_continued_fractions(fractions)

# Calculate Φ(Ν) and eliminate non valiable pairs.
Fn, possible_keys = calc_f(continued_fractions, e)

# For each Φ(Ν) calculate the roots of the quadratic equation.
prime_numbers, index = quadratic_roots(N, Fn)

# Decryption message.
decryption = decrypt(C, N, possible_keys[index][1])
print(''.join(decryption))


print(possible_keys)