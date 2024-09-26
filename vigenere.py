import sys
import string

ASCII_LOWERCASE_OFFSET = 97

# Argument format: vigenere.py -[action] [plaintext] [key]
action = sys.argv[1][1:] # slice to remove dash
ptext = sys.argv[2].lower()
key = sys.argv[3].lower()
ciphertext = ''

def encrypt_vigenere(plaintext, key, ciphertext):
    return ciphertext

def decrypt_vigenere(plaintext, key, ciphertext):
    return ciphertext

def main():
    if (action == 'encrypt' or action == 'e'):
        print(f"{encrypt_vigenere(ptext, key, ciphertext)}")

    elif (action == 'decrypt' or action == 'd'):
        print(f"{decrypt_vigenere(ptext, key, ciphertext)}")
    print(f"key used: {key}\nplaintext: {ptext}") 
    
if __name__ == '__main__': 
    main()
    