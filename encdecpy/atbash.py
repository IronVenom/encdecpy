class atbash:

	def encode(string):

		list_1 = [chr(i) for i in range(ord('A'),ord('Z')+1)]
		list_2 = [chr(i) for i in range(ord('a'),ord('z')+1)]
		listr_1 = list_1[::-1]
		listr_2 = list_2[::-1]
		encode_dict_upper = {x:y for x,y in zip(list_1,listr_1)}
		encode_dict_lower = {x:y for x,y in zip(list_2,listr_2)}


		encoded_string=''
		for i in string:
			if ord(i)>=ord('a') and ord(i)<=ord('z'):
				encoded_string+=encode_dict_lower[i]
			elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
				encoded_string+=encode_dict_upper[i]
			else:
				encoded_string+=i
		return encoded_string

	def decode(string):
		
		list_1 = [chr(i) for i in range(ord('A'),ord('Z')+1)]
		list_2 = [chr(i) for i in range(ord('a'),ord('z')+1)]
		listr_1 = list_1[::-1]
		listr_2 = list_2[::-1]
		encode_dict_upper = {x:y for x,y in zip(list_1,listr_1)}
		encode_dict_lower = {x:y for x,y in zip(list_2,listr_2)}

		decoded_string=''
		for i in string:
			if ord(i)>=ord('a') and ord(i)<=ord('z'):
				decoded_string+=encode_dict_lower[i]
			elif ord(i)>=ord('A') and ord(i)<=ord('Z'):
				decoded_string+=encode_dict_upper[i]
			else:
				decoded_string+=i
		return decoded_string


