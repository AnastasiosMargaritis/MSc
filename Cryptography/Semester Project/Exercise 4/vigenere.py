# Function calculating index of coincidence for cipher text.
def index_of_coincidence(cipher):    
    freq = {}
    for c in cipher:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    N = len(cipher) - 1
    sum = 0
    for k in freq:
        sum += freq[k] * (freq[k] - 1)

    return sum /(N * (N - 1))

# Calculate IC's for several key lengths.
# Returns a dict with periods and IC's.
def calculate_key_length(cipher, min_length, max_length):

    ICs = {}

    for length in range(min_length, max_length):
        sub_cipher = ''
        for i in range(1, len(cipher), length):
            sub_cipher += cipher[i]
        
        ICs[length] = index_of_coincidence(sub_cipher)

    return ICs

with open('vigenere.txt', 'r') as f:
    cipher = f.read()

cipher = cipher.rstrip('\n')

min_key_length = 2
max_key_length = 40

print(calculate_key_length(cipher, min_key_length, max_key_length))