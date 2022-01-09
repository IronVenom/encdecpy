tabula_recta = []
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(26):
    temp = ['']*26
    shiftedalphabets = alphabets[i:] + alphabets[:i]
    for j in range(26):
        temp[j] = shiftedalphabets[j]
    tabula_recta.append(temp)

def strip(string):
    string = ''.join(string.split(' '))
    string = string.upper()
    plaintext = ""
    for x in string:
        if x in alphabets:
            plaintext+=x
    return plaintext

def generate_keystream(string, key):
    length = len(string)
    key = strip(key)
    i = 0
    keystream=""
    for j in range(length):
        if i >= len(key):
            i = 0
        keystream+=key[i]
        i+=1
    return keystream

class beaufort:

    def encode(string, key):
        string = strip(string)
        keystream = generate_keystream(string, key)
        encoded_string=""
        for i in range(len(string)):
            char = string[i]
            encodecol = alphabets[ord(char)-ord('A'):] + alphabets[:ord(char)-ord('A')]
            encodedchar = chr(encodecol.index(keystream[i]) + ord('A'))
            encoded_string+=encodedchar
        return encoded_string

    def decode(string, key):
        decoded_string = ""
        keystream = generate_keystream(string, key)
        for i in range(len(string)):
            char = string[i]
            decoderow = alphabets[ord(char)-ord('A'):] + alphabets[:ord(char)-ord('A')]
            decodedchar = chr(decoderow.index(keystream[i]) + ord('A'))
            decoded_string+=decodedchar
        return decoded_string