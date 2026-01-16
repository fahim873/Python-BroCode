import random
import string

chars = " " + string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)
#print(f"Chars: {chars}")
#print(f"Keys: {key}")

#DECRYPT

cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in  cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message : {cipher_text}")
print(f"Decrypted Message : {plain_text}")

