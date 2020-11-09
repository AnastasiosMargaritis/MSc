#Frequencies of English letters.
ENGLISH_FREQ = (0.0749, 0.0129, 0.0354, 0.0362, 0.1400, 0.0218, 0.0174, 0.0422, 0.0665, 0.0027, 0.0047,
                0.0357, 0.0339, 0.0674, 0.0737, 0.0243, 0.0026, 0.0614, 0.0695, 0.0985, 0.0300, 0.0116,
                0.0169, 0.0028, 0.0164, 0.0004)

#Calculating frequencies of letters in a text.
def calculate_freq(cipher):
    freq = {}
    for c in cipher:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    
    return freq

# Function calculating index of coincidence for cipher text.
def index_of_coincidence(cipher):    

    freq = calculate_freq(cipher)

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
        for i in range(0, len(cipher), length):
            sub_cipher += cipher[i]
        
        ICs[length] = index_of_coincidence(sub_cipher)

    return ICs

# Calculate chi-squared statistic
d

def decipher(cipher):
    letter_freq = calculate_freq(cipher).values()
    english_freq = [i * len(cipher) for i in ENGLISH_FREQ]
    chi_square(letter_freq, english_freq)

with open('vigenere.txt', 'r') as f:
    cipher = f.read()

cipher = cipher.rstrip('\n')
cipher = cipher[1:]


min_key_length = 2
max_key_length = 40

# Calculating probabilities for min_key_length to max_key_length.
prob_key_length = calculate_key_length(cipher, min_key_length, max_key_length)

# Extracting biggest probability, so key_length.
values = prob_key_length.values()
key_length = list(prob_key_length.keys())[list(prob_key_length.values()).index(max(values))]
decipher(cipher)

# key = ''
# for i in range(0, key_length):

#     decipher_sequence = ''
#     for j in range(i, len(cipher), key_length):
#         decipher_sequence += cipher[j]

#     key += decipher(decipher_sequence)

# print(key)



