![PyPI - Downloads](https://img.shields.io/pypi/dm/encdecpy.svg) ![PyPI - Version](https://img.shields.io/pypi/v/encdecpy.svg) ![PyPI - Version](https://img.shields.io/pypi/l/encdecpy.svg)      

## encdecpy
Python package to encode and decode strings using ciphers.

### Installation

```
$ pip install encdecpy
```

### Usage

1. Base64 encoding-decoding: Parameter is a string. A string is returned.

Do

```
from encdecpy import base64

string = 'lorem ipsum ...'

print(base64(string).encode())
print(base64(string).decode())
```

* base64(string).encode() : To encode a string.
* base64(string).decode() : To decode a string.

2. Atbash encoding-decoding: Parameter is a string. A string is returned.

Do 

```
from encdecpy import atbash

string = 'lorem ipsum ...'

print(atbash(string).encode())
print(atbash(string).decode())
```

* atbash(string).encode() : To encode a string.
* atbash(string).decode() : To decode a string.

3. ROT13 encoding-decoding: Parameter is a string. A string is returned.

Do 

```
from encdecpy import rot13

string = 'lorem ipsum ...'

print(rot13(string).encode())
print(rot13(string).decode())
```

* rot13(string).encode() : To encode a string.
* rot13(string).decode() : To decode a string.

4. Caesar encoding-decoding: Parameters are a string and a key(integer) . A string is returned.

Do 

```
from encdecpy import caesar

string = 'lorem ipsum ...'

key = 8

print(caesar(string,key).encode())
print(caesar(string,key).decode())
```

* caesar(string,key).encode() : To encode a string.
* caesar(string,key).decode() : To decode a string.
