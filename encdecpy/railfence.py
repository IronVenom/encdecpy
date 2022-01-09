class railfence:

	def encode(string, key):
		rails = [['\n' for _ in range(len(string))] for _ in range(key)]
		direction = False
		row = 0
		col = 0
		for i in range(len(string)):
			if row==0 or row==key-1:
				direction = not direction
			rails[row][col] = string[i]
			col+=1
			if direction:
				row+=1
			else:
				row-=1
		encrypted_string=""
		for i in range(key):
			for j in range(len(string)):
				if rails[i][j]!='\n':
					encrypted_string+=rails[i][j]
		return encrypted_string
	
	def decode(string, key):
		rails = [['\n' for _ in range(len(string))] for _ in range(key)]
		direction = None
		row = 0
		col = 0
		for i in range(len(string)):
			if row==0:
				direction = True
			if row==key-1:
				direction = False
			rails[row][col]='^'
			col+=1
			if direction:
				row+=1
			else:
				row-=1
		idx = 0
		for i in range(key):
			for j in range(len(string)):
				if rails[i][j]=='^' and idx<len(string):
					rails[i][j] = string[idx]
					idx+=1
		decrypted_string=""
		row = 0
		col = 0
		for i in range(len(string)):
			if row==0:
				direction=True
			if row==key-1:
				direction=False
			if rails[row][col]!='^':
				decrypted_string+=rails[row][col]
				col+=1
			if direction:
				row+=1
			else:
				row-=1
		return decrypted_string