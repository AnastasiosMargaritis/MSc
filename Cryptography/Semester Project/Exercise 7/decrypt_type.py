import itertools
from bitstring import BitArray
from random import randint


def encrypt(m):
    return m ^ (m << 6) ^ (m << 10) 

def decrypt(cipher):
    return cipher ^ (cipher << 6 ^ cipher << 12) ^ (cipher << 10)

lst = [list(i) for i in itertools.product([0, 1], repeat=16)]
lst = lst[1:]

# Make a list for all letter combinations.
letter_combination = []
for comb in lst:
    letter_combination.append(BitArray(comb))

index = randint(0, len(letter_combination))
print()


cipher = encrypt(letter_combination[index])

print('Plaintext is: %s' %letter_combination[index])
print('Cipher is: %s' %cipher)
print('Decrypted is: %s' %decrypt(cipher))