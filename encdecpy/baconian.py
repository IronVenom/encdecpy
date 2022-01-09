encode_dict = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}

decode_dict = {a:b for b,a in encode_dict.items()}

class baconian:

	def encode(string):
		encrypted_string=""
		string = string.upper()
		for character in string:
			if(character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
				encrypted_string+=encode_dict[character]
			else:
				encrypted_string+=' '
		return encrypted_string

	def decode(string):
		decrypted_string=""
		idx = 0
		while True:
			if idx<len(string)-4:
				substring=string[idx:idx+5]
				if substring[0]!=' ':
					decrypted_string+=decode_dict[substring]
					idx+=5
				else:
					decrypted_string+=' '
					idx+=1
			else:
				break
		return decrypted_string