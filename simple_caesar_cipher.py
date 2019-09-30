# A simple Caesar cipher
# Author: Kingsley Robertovich
# Caesar cipher is a type of substitution cipher in which each letter in the plaintext is
# 'shifted' a certain number of places down the alphabet. In this example we use the ASCII
# character set as our alphabet

def encipher(clearText, offset = 5):
    cipherText = ''
    for c in clearText:
        s = ord(c) + offset
        cipherText += chr(s)
    return cipherText

def decipher(ciphertext, offset = 5):
    clearText = ''
    for c in cipherText:
        s = ord(c) - offset
        clearText += chr(s)
    return clearText

if __name__ == '__main__':
    # get some input
    clearText = input("Please enter a message to encipher: ")
    cipherText = encipher(clearText)
    print(cipherText)
    newClear = decipher(cipherText)
    print(newClear)
    