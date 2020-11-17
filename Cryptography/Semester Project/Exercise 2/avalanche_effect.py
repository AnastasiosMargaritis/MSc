from random import randint
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto import Random
from bitstring import BitArray


BIT_MESSAGE = 64 # bits of the message

# Converts bitstrings to bytes.
def bitstring_to_bytes(x):
    s = ''.join(str(e) for e in x)
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

# Create messages differ to 1 bit, their final one.
def create_message_pairs(length):
    m1 = []

    for i in range(length):
        m1.append(randint(0, 1))

    m2 = m1.copy()
    randIndex = randint(0, 63)

    if m2[randIndex] == 0:
        m2[randIndex] = 1
    else:
        m2[randIndex] = 0

    return bitstring_to_bytes(m1), bitstring_to_bytes(m2)

# Calculates amount of different bits for each pair of messages.
# All messages are converted to 128 bits.
def count_different_bits(x, y):
    x = (bin(int.from_bytes(x, byteorder="big"))[2:])
    y = (bin(int.from_bytes(y, byteorder="big"))[2:]) 

    # Adding zeros for len() = 128 and split them.
    x = list((BIT_MESSAGE - len(x)) * str(0) + x)
    y = list((BIT_MESSAGE - len(y)) * str(0) + y)

    counter = 0

    for i in range(0, BIT_MESSAGE):
        if ( x[i] != y[i]):
            counter +=1
    
    return counter
#......................................MAIN.............................
AES_ECB = 0
AES_CBC = 0
Blowfish_ECB = 0
Blowfish_CBC = 0

num_of_messages = 180


for i in range(num_of_messages):
    # Create a pair of messages
    m1, m2 = create_message_pairs(BIT_MESSAGE)
# ................................... AES ECB MODE........................
    key_AES_ECB = b'This is my key for today'
    cipher = AES.new(key_AES_ECB, AES.MODE_ECB)


    # Encrypt the two messages.
    m1Enc = cipher.encrypt(pad(m1, AES.block_size))
    m2Enc = cipher.encrypt(pad(m2, AES.block_size))

    AES_ECB += count_different_bits(m1Enc, m2Enc) / 64


#.............................. AES CBC MODE............................
    key_AES_CBC = b'This is my key for today'
    bs = AES.block_size
    iv = Random.new().read(bs)
    cipher = AES.new(key_AES_CBC, AES.MODE_CBC, iv)
   

    # Encrypt the two messages.
    m1Enc = iv + cipher.encrypt(pad(m1, AES.block_size))
    m2Enc = iv + cipher.encrypt(pad(m2, AES.block_size))

    AES_CBC += count_different_bits(m1Enc, m2Enc) / 64


#............................ BLOWFISH ECB MODE..........................
    key_BLOWFISH_ECB = b'This is my key for today'
    cipher = Blowfish.new(key_BLOWFISH_ECB, Blowfish.MODE_ECB)

    # Encrypt the two messages.
    m1Enc = cipher.encrypt(m1)
    m2Enc = cipher.encrypt(m2)

    Blowfish_ECB += count_different_bits(m1Enc, m2Enc) / 64


#.............................. BLOWFISH CBC MODE.........................
    bs = Blowfish.block_size
    key_BLOWFISH_CBC = b'This is my key for today'
    iv = Random.new().read(bs)
    cipher = Blowfish.new(key_BLOWFISH_CBC, Blowfish.MODE_CBC, iv)

    # Encrypt the two messages.
    m1Enc = iv + cipher.encrypt(m1)
    m2Enc = iv + cipher.encrypt(m2)

    Blowfish_CBC += count_different_bits(m1Enc, m2Enc) / 64


print(AES_ECB / num_of_messages)
print(AES_CBC / num_of_messages)
print(Blowfish_ECB / num_of_messages)
print(Blowfish_CBC / num_of_messages)





