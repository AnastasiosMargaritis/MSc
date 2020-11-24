

def calculate(prime):
    maxDivisionsByTwo = 0
    ec = prime-1
    while ec % 2 == 0: 
        # ec = ec / 2
        ec >>= 1
        print(ec)
        maxDivisionsByTwo += 1
    print(ec, maxDivisionsByTwo)



prime = 193
calculate(prime)

print(pow(2, 2, 5))