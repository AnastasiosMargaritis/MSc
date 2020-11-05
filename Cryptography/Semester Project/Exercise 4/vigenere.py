def calculate_freq(cipher):
    
    freq = {}
    for c in cipher:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    freq.pop('\ufeff', None)
    freq.pop('\n', None)

    N = len(cipher) - 2
    sum = 0
    for k in freq:
        sum += freq[k] * (freq[k] - 1)

    return sum /(N * (N - 1))


with open('vigenere.txt', 'r') as f:
    cipher = f.read()


print(calculate_freq(cipher))