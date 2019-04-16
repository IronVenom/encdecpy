class caesar:

	def __init__(self,string,key):
		
		self.string = string
		self.key = key

	def encode(self):

		if self.key > 26:
			self.key = self.key%26
		encoded_string = ''
		for i in self.string:
			if ord(i)>=ord('A') and ord(i)<=ord('Z'):
				if ord(i)+self.key>ord('Z'):
					encoded_string+=chr(ord('A')+ord(i)+self.key-ord('Z')-1)
				else:
					encoded_string+=chr(ord(i)+self.key)
			elif ord(i)>=ord('a') and ord(i)<=ord('z'):
				if ord(i)+self.key>ord('z'):
					encoded_string+=chr(ord('a')+ord(i)+self.key-ord('z')-1)
				else:
					encoded_string+=chr(ord(i)+self.key)
			else:
				encoded_string+=i
		return encoded_string

	def decode(self):

		if self.key > 26:
			self.key = self.key%26
		decoded_string = ''
		for i in self.string:
			if ord(i)>=ord('A') and ord(i)<=ord('Z'):
				if ord(i)-self.key<ord('A'):
					decoded_string+=chr(ord('Z')-self.key+ord(i)-ord('A')+1)
				else:
					decoded_string+=chr(ord(i)-self.key)
			elif ord(i)>=ord('a') and ord(i)<=ord('z'):
				if ord(i)-self.key<ord('a'):
					decoded_string+=chr(ord('z')-self.key+ord(i)-ord('a')+1)
				else:
					decoded_string+=chr(ord(i)-self.key)
			else:
				decoded_string+=i
		return decoded_string
