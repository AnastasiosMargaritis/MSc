
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

print(fast(2, 1234567, 12345))
print(fast(130, 7654321, 567))


