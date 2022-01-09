import math

class columnartransposition:

	def encode(string, key):
		if len(set(key))!=len(key):
			raise Exception("Key should contain unique characters!")
		encoded_string=""
		idx = 0
		col = len(key)
		row = int(math.ceil(float(len(string))/col))
		padding = int((row*col)-len(string))
		string_list = list(string) + ['_']*padding
		matrix = [string_list[i:i+col] for i in range(0, len(string_list), col)]
		key_list = sorted(list(key))
		for _ in range(col):
			current_idx = key.index(key_list[idx])
			for i in range(row):
				encoded_string+=matrix[i][current_idx]
			idx+=1
		return encoded_string

	def decode(string, key):
		if len(set(key))!=len(key):
			raise Exception("Key should contain unique characters!")
		decoded_string=""
		idx = 0
		string_idx = 0
		col = len(key)
		row = int(math.ceil(float(len(string))/col))
		key_list = sorted(list(key))
		decode_matrix = []
		for _ in range(row):
			decode_matrix+=[['*']*col]
		for _ in range(col):
			current_idx = key.index(key_list[idx])
			for j in range(row):
				decode_matrix[j][current_idx] = list(string)[string_idx]
				string_idx+=1
			idx+=1
		decoded_string = ''.join(sum(decode_matrix, []))
		padding_count = decoded_string.count('_')
		if padding_count>0:
			return decoded_string[: -padding_count]
		else:
			return decoded_string