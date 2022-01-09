class rot13:

	def encode(string):

		encoded_string = ''
		for i in string:
			if ord(i)>=ord('A') and ord(i)<=ord('Z'):
				if ord(i)+13>ord('Z'):
					encoded_string+=chr(ord('A')+ord(i)+13-ord('Z')-1)
				else:
					encoded_string+=chr(ord(i)+13)
			elif ord(i)>=ord('a') and ord(i)<=ord('z'):
				if ord(i)+13>ord('z'):
					encoded_string+=chr(ord('a')+ord(i)+13-ord('z')-1)
				else:
					encoded_string+=chr(ord(i)+13)
			else:
				encoded_string+=i
		return encoded_string

	def decode(string):

		decoded_string = ''
		for i in string:
			if ord(i)>=ord('A') and ord(i)<=ord('Z'):
				if ord(i)-13<ord('A'):
					decoded_string+=chr(ord('Z')-13+ord(i)-ord('A')+1)
				else:
					decoded_string+=chr(ord(i)-13)
			elif ord(i)>=ord('a') and ord(i)<=ord('z'):
				if ord(i)-13<ord('a'):
					decoded_string+=chr(ord('z')-13+ord(i)-ord('a')+1)
				else:
					decoded_string+=chr(ord(i)-13)
			else:
				decoded_string+=i
		return decoded_string