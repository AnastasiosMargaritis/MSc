import numpy as np

# Key-scheduling algorithm
def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S
    
# Pseudo-random generation algorithm
def PRGA(S, n):
    i, j = 0, 0
    key = []

    while n > 0:
        n = n - 1
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        key.append(K)
    return key


#RC4 Encryption Process
def encrypt(plaintext, keystream):
    plaintext = np.array([ord(i) for i in plaintext])
    return keystream ^ plaintext

#RC4 Decryption Process
def decrypt(cipher, keystream):
    return cipher ^ keystream


# Convert text to ASCII
def text_to_ascii(s):
    return [ord(c) for c in s]

# Convert ASCII to text
def ascii_to_text(s):
    return ''.join([chr(i) for i in s])

# Key to ASCII code
key = text_to_ascii('HOUSE')

# Input plaintext
plaintext = input("Enter your message: ").upper().replace(' ','')

S = KSA(key)
keystream = np.array(PRGA(S, len(plaintext)))


#Encrypted Cipher
cipher = encrypt(plaintext, keystream)

#Hex Representation of cipher
print('Your HEX cipher representation is: ' + cipher.astype(np.uint8).data.hex())

#Decrypted message representation
print('Your decrypted message is: ' + ascii_to_text(decrypt(cipher, keystream)))




