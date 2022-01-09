def gcd(a, b):
	    while b != 0:
	        a, b = b, a % b
	    return a

def coprime(a, b):
    return gcd(a, b) == 1

def checkFactors(m, a):
    if a > 25 or a < 0:
        return False
    elif not coprime(m, a):
        return False
    else:
        return True

def modinv(a, m):
    for i in range(0, m):
        if (a*i)%m == 1:
            return i

class affine:

	def encode(string, a, b):
	    m = 26
	    b = b%26
	    check = checkFactors(m,a)
	    if check:
	        charmap = {chr(j):i for i,j in enumerate(range(ord('a'),ord('z')+1))}
	        revcharmap = {j:i for i,j in charmap.items()}
	        encoded_string = ""
	        for ch in string:
	            if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
	                c = (a*charmap[ch.lower()] + b)%m
	                encoded_string+=revcharmap[c]
	            elif ord(ch)>=ord('a') and ord(ch)<=ord('z'):
	                c = (a*charmap[ch] + b)%m
	                encoded_string+=revcharmap[c]
	            else:
	                encoded_string+=ch
	        return encoded_string
	    else:
	        return "Error : a should be relatively prime to 26 and lie between 0 to 25 (both inclusive)."

	def decode(string, a, b):
	    m = 26
	    b = b%26
	    check = checkFactors(m,a)
	    if check:
	        charmap = {chr(j):i for i,j in enumerate(range(ord('a'),ord('z')+1))}
	        revcharmap = {j:i for i,j in charmap.items()}
	        decoded_string = ""
	        for ch in string:
	            if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
	                ainv = modinv(a, m)
	                p = ainv*(charmap[ch.lower()]-b)%26
	                decoded_string+=revcharmap[p]
	            elif ord(ch)>=ord('a') and ord(ch)<=ord('z'):
	                ainv = modinv(a, m)
	                p = ainv*(charmap[ch]-b)%26
	                decoded_string+=revcharmap[p]
	            else:
	                decoded_string+=ch
	        return decoded_string
	    else:
	        return "Error : a should be relatively prime to 26 and lie between 0 to 25 (both inclusive)."
