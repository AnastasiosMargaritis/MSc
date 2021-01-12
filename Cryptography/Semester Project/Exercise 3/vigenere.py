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

# Breaks the cipher into key_length number of ciphers,
# taking every nth letter of the cipher.
def break_ciphers(cipher, key_length):
    dict = {}

    for i in range(0, key_length):

        counter = i;
        chars = []
        st = ""

        while(counter < len(cipher)):
            chars.append(cipher[counter])
            counter += key_length
        
        
        dict[i] = st.join(chars)
    
    return dict

# Counters chars in a string.
def Counter(cipher):

    dict ={}

    for i in range(65, 91):
        dict[chr(i)] = 0
    
    for char in cipher:
        dict[char] += 1

    return dict


# Calculates chi-gamma square for all cipher combinations.
# Each time it is called returns a char of our key.
def chi_gamma_square(combinations):

    dict = {}
    frequency = []

    for combo in combinations:
        frequency.append(Counter(combo))

    counter = 0
    for freq in frequency:
        sum = 0

        for i in range(0, 26):
            sum += ((freq[chr(65 + i)] - len(combinations[0]) * ENGLISH_FREQ[i]) ** 2) / (len(combinations[0]) * ENGLISH_FREQ[i])
        
        dict[counter] = sum
        counter += 1
    
    return chr(65 + min(dict, key = dict.get))
    
# Creates all different 26 combinations for each cipher. Calls chi-gamma square to 
# calculate chi-gamma and extract the key.
def cipher_combinations(ciphers):

    combinations = []
    combinations.append(ciphers)

    for i in range(1, 26):
        str1 = ""
        for cipher in ciphers:
            
            str1 += chr((ord(cipher) - i - 65) % 26 + 65)
        
        combinations.append(str1)
        
    return chi_gamma_square(combinations)

# Vigenere decryption function.
def decrypt(cipher, key):

    while(len(key) < len(cipher)):
        key += key

    print()

    m = ""

    for i in range(0, len(cipher)):
        m += chr((ord(cipher[i]) - ord(key[i])) % 26 + 65)

    return m


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
key_length = 14

ciphers = break_ciphers(cipher, key_length)

key = ""
for i in range(0, key_length):
    key += cipher_combinations(ciphers[i])


print('The Vigenere Key is: ' + key)
print('The initial message is: ' + decrypt(cipher, key))