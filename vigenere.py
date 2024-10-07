import sys

ASCII_OFFSET = 97
ASCII_LIMIT = 122

# Argument format: vigenere.py -[action] "[plaintext]" [key]
ciphertext = []
action = sys.argv[1][1:] # slice to remove dash
ptext = sys.argv[2].lower()
key = sys.argv[3].lower()

def encrypt_vigenere(plaintext, key, ciphertext):
    key_iterator = 0
    for i in plaintext: #iterating, i is current char
        if key_iterator >= len(key): #our key repeats if len(ptext) > len(key)
            key_iterator = 0
        
        #if non-letters, don't encrypt
        if ord(i) < ASCII_OFFSET or ord(i) > ASCII_LIMIT:
            ciphertext.append(i)
            continue

        #if chr(ord(i)) + ord(key) > 'z', we loop back over
        if ord(i) + (ord(key[key_iterator]) - ASCII_OFFSET) > ASCII_LIMIT: 
            ciphertext.append(chr(ord(i) + (ord(key[key_iterator]) - ASCII_LIMIT - 1)))
            key_iterator += 1
            continue

        ciphertext.append(chr(ord(i) + (ord(key[key_iterator]) - ASCII_OFFSET)))
        key_iterator += 1
    return ''.join(ciphertext)

def decrypt_vigenere(plaintext, key, ciphertext):
    key_iterator = 0
    for j in plaintext:
        if key_iterator >= len(key):
            key_iterator = 0

        if ord(j) < ASCII_OFFSET or ord(j) > ASCII_LIMIT:
            ciphertext.append(j)
            continue

        if ord(j) - (ord(key[key_iterator]) - ASCII_OFFSET) < ASCII_OFFSET:
            ciphertext.append(chr(ord(j) - (ord(key[key_iterator]) - ASCII_OFFSET) + (ASCII_LIMIT - ASCII_OFFSET + 1)))
            key_iterator += 1
            continue
        
        ciphertext.append(chr(ord(j) - (ord(key[key_iterator]) - ASCII_OFFSET)))
        key_iterator += 1

        ''' if char j and (key char - offset) difference < 'a', 
            add to ciphertext this difference, plus the NUMBER of alphabet letters (limit - offset + 1)
        '''
    return ''.join(ciphertext)

def main():
    if (action == 'encrypt' or action == 'e'):
        print(f"{encrypt_vigenere(ptext, key, ciphertext)}")

    elif (action == 'decrypt' or action == 'd'):
        print(f"{decrypt_vigenere(ptext, key, ciphertext)}")
    
if __name__ == '__main__': 
    main()
