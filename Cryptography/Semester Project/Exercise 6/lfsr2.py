from bitstring import BitArray
from langdetect import detect
import itertools

arr = {
  'A': BitArray(bin='00000'),
  'B': BitArray(bin='00001'),
  'C': BitArray(bin='00010'),
  'D': BitArray(bin='00011'),
  'E': BitArray(bin='00100'),
  'F': BitArray(bin='00101'),
  'G': BitArray(bin='00110'),
  'H': BitArray(bin='00111'),
  'I': BitArray(bin='01000'),
  'J': BitArray(bin='01001'),
  'K': BitArray(bin='01010'),
  'L': BitArray(bin='01011'),
  'M': BitArray(bin='01100'),
  'N': BitArray(bin='01101'),
  'O': BitArray(bin='01110'),
  'P': BitArray(bin='01111'),
  'Q': BitArray(bin='10000'),
  'R': BitArray(bin='10001'),
  'S': BitArray(bin='10010'),
  'T': BitArray(bin='10011'),
  'U': BitArray(bin='10100'),
  'V': BitArray(bin='10101'),
  'W': BitArray(bin='10110'),
  'X': BitArray(bin='10111'),
  'Y': BitArray(bin='11000'),
  'Z': BitArray(bin='11001'),
  '.': BitArray(bin='11010'),
  '!': BitArray(bin='11011'),
  '?': BitArray(bin='11100'),
  '(': BitArray(bin='11101'),
  ')': BitArray(bin='11110'),
  '-': BitArray(bin='11111')
}


class LFSR:

    def __init__(self, feedback):
        self.feedback = feedback
    
    # Takes a string as an input and returns a 
    # BitArray.
    def msgtobits(self, message):

        bits = ''

        for c in message:
            bits += arr[c]

        return bits

    # Takes the feedback function and takes us
    # to the next LFSR state.
    def next_state(self, current_state):

        bits = [current_state[i] for i in self.feedback]

        xor = bits[0] 
        for i in range(1, len(bits)):
            xor = xor ^ bits[i]

        current_state = current_state >> 1
        current_state[0] = xor
        
        return current_state, xor

    # Takes a BitArray as an input and returns a 
    # string.
    def bitstomsg(self, bits):
        ans = ''
        for i in range(0, len(bits), 5):
            ans += list(arr.keys())[list(arr.values()).index(bits[i:i+5])]

        return ans




lfsr = LFSR([5, 6, 8, 9])

cipher = lfsr.msgtobits('i!))aiszwykqnfcyc!?secnncvch'.upper())

# Converts given chars to bits based on the array given.
m = lfsr.msgtobits('ab'.upper())

# Converts given cipher to bits based on the array given.
c = lfsr.msgtobits('.s'.upper())

# Calculating Encryption key for the above message and cipher.
state = m ^ c
key = ''

print(state)

while(len(key) < 140):
    state, k = lfsr.next_state(state)
    key += '1' if k else '0'

key = BitArray(bin = key)
print(lfsr.bitstomsg(key ^ cipher))

