![PyPI - Version](https://img.shields.io/pypi/v/encdecpy.svg) ![PyPI - Version](https://img.shields.io/pypi/l/encdecpy.svg)      

# encdecpy
Python package to encode and decode strings using ciphers.

## Installation

```
$ pip install encdecpy
```

## Usage

The package provides the following ciphers to encode and decode strings - 

1. [Affine Cipher](###affine-cipher)
2. [Atbash Cipher](###atbash-cipher)
3. [Autokey Cipher](###autokey-cipher)
4. [Baconian Cipher](###baconian-cipher)
5. [Base64 Cipher](###base64-cipher)
6. [Beaufort Cipher](###beaufort-cipher)
7. [Caesar Cipher](###caesar-cipher)
8. [Columnar Transposition Cipher](###columnar-transposition-cipher)
9. [Polybius Square Cipher](###polybius-square-cipher)
10. [Rail Fence Cipher](###rail-fence-cipher)
11. [ROT13 Cipher](###rot13-cipher)
12. [Running Key Cipher](###running-key-cipher)
13. [Simple Substitution Cipher](###simple-substitution-cipher)
14. [Vignere Cipher](###vignere-cipher)

### Affine Cipher
```python
from encdecpy import affine
```
* affine.encode(string, a, b) - Returns the encoded string.
* affine.decode(string, a, b) - Returns the decoded string.
> a and b are integers between 0 and 25. a should be relatively prime to 26 and lie between 0 to 25 (both inclusive).

### Atbash Cipher
```python
from encdecpy import atbash
```
* atbash.encode(string) - Returns the encoded string.
* atbash.decode(string) - Returns the decoded string.

### Autokey Cipher
```python
from encdecpy import autokey
```
* autokey.encode(string, key) - Returns the encoded string.
* autokey.decode(string, key) - Returns the decoded string.
> key is a string.

### Baconian Cipher
```python
from encdecpy import baconian
```
* baconian.encode(string) - Returns the encoded string.
* baconian.decode(string) - Returns the decoded string.

### Base64 Cipher
```python
from encdecpy import base64
```
* base64.encode(string) - Returns the encoded string.
* base64.decode(string) - Returns the decoded string.

### Beaufort Cipher
```python
from encdecpy import beaufort
```
* beaufort.encode(string, key) - Returns the encoded string.
* beaufort.decode(string, key) - Returns the decoded string.
> key is a string.

### Caesar Cipher
```python
from encdecpy import caesar
```
* caesar.encode(string, key) - Returns the encoded string.
* caesar.decode(string, key) - Returns the decoded string.
> key is a whole number.

### Columnar Transposition Cipher
```python
from encdecpy import columnartransposition
```
* columnartransposition.encode(string, key) - Returns the encoded string.
* columnartransposition.decode(string, key) - Returns the decoded string.
> key is a string and should contain unique characters between A-Z.

### Polybius Square Cipher
```python
from encdecpy import polybiussquare
```
* polybiussquare.encode(string, key) - Returns the encoded string.
* polybiussquare.decode(string, key) - Returns the decoded string.
> key is a string and should contain unique characters between a-z with one alphabet missing. Length of key should be 25. An example key - phqgiumeaylnofdxkrcvstzwb.

### Rail Fence Cipher
```python
from encdecpy import railfence
```
* railfence.encode(string, key) - Returns the encoded string.
* railfence.decode(string, key) - Returns the decoded string.
> key is a positive number denoting the number of rails.

### ROT13 Cipher
```python
from encdecpy import rot13
```
* rot13.encode(string) - Returns the encoded string.
* rot13.decode(string) - Returns the decoded string.

### Running Key Cipher
```python
from encdecpy import runningkey
```
* runningkey.encode(string, key) - Returns the encoded string.
* runningkey.decode(string, key) - Returns the decoded string.
> key is a large string, usually a paragraph taken from a book.

### Simple Substitution Cipher
```python
from encdecpy import simplesubstitution
```
* simplesubstitution.encode(string, key) - Returns the encoded string.
* simplesubstitution.decode(string, key) - Returns the decoded string.
* simplesubstitution.generate_random_key() - Returns a randomly generated key.
> key is a string containing a permutation of the alphabets (a-z), with no other characters. String should contain only unique characters.

### Vignere Cipher
```python
from encdecpy import vignere
```
* vignere.encode(string, key) - Returns the encoded string.
* vignere.decode(string, key) - Returns the decoded string.
> key is a string, usually a single word.
