class polybiussquare:

    def encode(string, key):
        polybius_matrix = []
        index = 0
        for _ in range(0,5):
            row = []
            for _ in range(0,5):
                row.append(key[index])
                index+=1
            polybius_matrix.append(row)
        polybius_dict = {}
        for ch in key:
            vals = [(index, row.index(ch)) for index, row in enumerate(polybius_matrix) if ch in row]
            (r, c) = vals[0]
            polybius_dict[ch] = str(r+1)+str(c+1)
        encrypted_string = ""
        for ch in string:
            if ord(ch)>=ord('A') and ord(ch)<=ord('Z'):
                encrypted_string+=polybius_dict[ch.lower()]
            elif ord(ch)>=ord('a') and ord(ch)<=ord('z'):
                encrypted_string+=polybius_dict[ch]
            else:
                encrypted_string+=ch
        return encrypted_string
    
    def decode(string, key):
        polybius_matrix = []
        index = 0
        for _ in range(0,5):
            row = []
            for _ in range(0,5):
                row.append(key[index])
                index+=1
            polybius_matrix.append(row)
        polybius_dict = {}
        for ch in key:
            vals = [(index, row.index(ch)) for index, row in enumerate(polybius_matrix) if ch in row]
            (r, c) = vals[0]
            polybius_dict[ch] = str(r+1)+str(c+1)
        polybius_dict = {value:key for key, value in polybius_dict.items()}
        decrypted_string = ""
        index = 0
        while index < len(string):
            if ord(string[index])>=ord('1') and ord(string[index])<=ord('9'):
                ch = string[index] + string[index+1]
                index+=2
                decrypted_string+=polybius_dict[ch]
            else:
                decrypted_string+=string[index]
                index+=1
        return decrypted_string