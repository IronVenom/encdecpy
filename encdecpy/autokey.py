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

class autokey:

	def encode(string, key):
	    plaintext = strip(string)
	    key = strip(key)
	    keystream = None
	    if len(plaintext) > len(key):
	        keystream = key + plaintext[:len(plaintext) - len(key)]
	    elif len(plaintext) < len(key):
	        keystream = key[:len(plaintext)]
	    else:
	        keystream = key
	    encoded_string=""
	    for i, j in zip(plaintext, keystream):
	        encoded_string+=tabula_recta[ord(i) - ord('A')][ord(j) - ord('A')]
	    return encoded_string

	def decode(string, key):
	    decoded_string=""
	    key = strip(key)
	    for i in range(len(string)):
	        char = key[i]
	        decodecol = alphabets[ord(char)-ord('A'):] + alphabets[:ord(char)-ord('A')]
	        decodedchar = chr(decodecol.index(string[i]) + ord('A'))
	        decoded_string+=decodedchar
	        key+=decodedchar
	    return decoded_string