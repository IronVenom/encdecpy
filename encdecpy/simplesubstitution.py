import random

class simplesubstitution:

	def generate_random_key():
		string = "abcdefghijklmnopqrstuvwxyz"
		l = list(string)
		random.shuffle(l)
		random_key = ''.join(l)
		return random_key

	def encode(string, key):
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		encode_dict = {i:j for i,j in zip(alphabets, key)}
		encoded_string=""
		for char in string:
			if char in alphabets:
				encoded_string+=encode_dict[char]
			else:
				encoded_string+=char
		return encoded_string

	def decode(string, key):
		alphabets = "abcdefghijklmnopqrstuvwxyz"
		decode_dict = {i:j for i,j in zip(key, alphabets)}
		decoded_string=""
		for char in string:
			if char in alphabets:
				decoded_string+=decode_dict[char]
			else:
				decoded_string+=char
		return decoded_string
