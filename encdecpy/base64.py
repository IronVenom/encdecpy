# Dictionaries for base64 encoding and decoding.

encode_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',
			  23:'X',24:'Y',25:'Z',26:'a',27:'b',28:'c',29:'d',30:'e',31:'f',32:'g',33:'h',34:'i',35:'j',36:'k',37:'l',38:'m',39:'n',40:'o',41:'p',42:'q',43:'r',44:'s'
			  ,45:'t',46:'u',47:'v',48:'w',49:'x',50:'y',51:'z',52:'0',53:'1',54:'2',55:'3',56:'4',57:'5',58:'6',59:'7',60:'8',61:'9',62:'+',63:"/"}

decode_dict = {a:b for b,a in encode_dict.items()}


class base64:

	def encode(string):

		binstream = ''
		for i in string:
			binstream+='0'*(8-len(f"{ord(i):b}"))+f"{ord(i):b}"
		extra = 0
		if len(binstream)%3!=0:
			if len(binstream)%3 == 2:
				binstream = '0'*16 + binstream
				extra = 1
			else:
				binstream = '0'*8 + binstream
				extra = 2
		encode_bin = []
		for i in range(0,int(len(binstream)//6)):
			encode_bin.append(binstream[6*i:6*(i+1):1])
		encoded_string = ''
		for i in encode_bin:
			encoded_string+=encode_dict[int(i,2)]
		return encoded_string+'='*extra

	def decode(string):

		decode_stream = ''
		newstring = ''
		if string[-1] == '=':
			if string[-2] == '=':
				newstring = string[:-2]
				for i in newstring:
					decode_stream+='0'*(6-len(f"{decode_dict[i]:b}"))+f"{decode_dict[i]:b}"
				decode_l = []
				decode_stream = '0'*8 + decode_stream
				for i in range(0,int(len(decode_stream)/8)):
					decode_l.append(chr(int(decode_stream[i*8:8*(i+1):1],2)))
				return ''.join(decode_l[2:])
			else:
				newstring = string[:-1]
				for i in newstring:
					decode_stream+='0'*(6-len(f"{decode_dict[i]:b}"))+f"{decode_dict[i]:b}"
				decode_l = []
				decode_stream = '0'*16 + decode_stream
				for i in range(0,int(len(decode_stream)/8)):
					decode_l.append(chr(int(decode_stream[i*8:8*(i+1):1],2)))
				return ''.join(decode_l[4:])
		else:
			for i in string:
				decode_stream+='0'*(6-len(f"{decode_dict[i]:b}"))+f"{decode_dict[i]:b}"
			decode_l = []
			for i in range(0,int(len(decode_stream)/8)):
				decode_l.append(chr(int(decode_stream[i*8:8*(i+1):1],2)))
			return ''.join(decode_l)