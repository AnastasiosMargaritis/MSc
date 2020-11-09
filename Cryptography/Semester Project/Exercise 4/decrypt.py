arr = {  'A' : 1,
         'B' : 2,
         'C' : 3,
         'D' : 4,
         'E' : 5,
         'F' : 6,
         'G' : 7,
         'H' : 8,
         'I' : 9,
         'J' : 10,
         'K' : 11,
         'L' : 12,
         'M' : 13,
         'N' : 14,
         'O' : 15,
         'P' : 16,
         'Q' : 17,
         'R' : 18,
         'S' : 19,
         'T' : 20,
         'U' : 21,
         'V' : 22,
         'W' : 23,
         'X' : 24,
         'Y' : 25 ,
         'Z' : 0 }


message = 'AJZBPMDLHYDBTSMFDXTQJ'
key = 'KYEKYEKYEKYEKYEKYEKYE'

K_decryption = []
Y_decryption = []
E_decryption = []


for c in message:
    K_decryption.append(list(arr.keys())[list(arr.values()).index((arr[c] - arr[key[0]]) % 26)])
    Y_decryption.append(list(arr.keys())[list(arr.values()).index((arr[c] - arr[key[1]]) % 26)])
    E_decryption.append(list(arr.keys())[list(arr.values()).index((arr[c] - arr[key[2]]) % 26)])

print(K_decryption)
print(Y_decryption)
print(E_decryption)

c = 'Y'
print(K_decryption[9], Y_decryption[9], E_decryption[9])

final_message = 'PEACE BEGINS WITH A SMILE'