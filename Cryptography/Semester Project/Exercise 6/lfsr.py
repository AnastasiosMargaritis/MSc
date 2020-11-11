# Initial array of bits given
arr = {  'A' : '00000',
         'B' : '00001',
         'C' : '00010',
         'D' : '00011',
         'E' : '00100',
         'F' : '00101',
         'G' : '00110',
         'H' : '00111',
         'I' : '01000',
         'J' : '01001',
         'K' : '01010',
         'L' : '01011',
         'M' : '01100',
         'N' : '01101',
         'O' : '01110',
         'P' : '01111',
         'Q' : '10000',
         'R' : '10001',
         'S' : '10010',
         'T' : '10011',
         'U' : '10100',
         'V' : '10101',
         'W' : '10110',
         'X' : '10111',
         'Y' : '11000' ,
         'Z' : '11001' ,
         '_' : '11010',
         '!' : '11011',
         '?' : '11100',
         '(' : '11101',
         ')' : '11110',
         '-' : '11111'}

# Creates lfsr with initial seed.
# def create_lfsr(seed):

#     feedback = [9, 8, 6, 5]

#     c = seed

#     while(len(c) < 140):




#XOR function for same length strings. String must represent bits.
def xor(s1, s2):
    ans = ''

    for i in range(len(s1)):
        if(s1[i] == s2[i]):
            ans += '0'
        else:
            ans += '1'
    
    return ans

#Convert message to bits based on the given dictionary.
def msgtobits(message):
    bits = ''
    for char in message:
        bits += arr[char]
    return bits

#Convert bits to letters based on the given dictionary.
def bitstomsg(bits):
    ans = ''
    for i in range(0, len(bits), 5):
        ans += list(arr.keys())[list(arr.values()).index(bits[i:i+5])]

    return ans

#Message decryption using the encrypted message transformed into bit.
def decrypt(c, k):
    return xor(c, k)


# Given message to decrypt.
c = msgtobits('i!))aiszwykqnfcyc!?secnncvch'.upper())

seed = '1101010010'
c = c[0:10]
print(bitstomsg(xor(c, seed)))
# k = create_lfsr(seed)
