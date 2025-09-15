# Encrypt with Ceasar Cipher
text = input("Enter your message: ")
cipher = ''
for ch in text:
    if not ch.isalpha():
        continue

    char = ch.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')

    cipher += chr(code)

print(cipher)

# Decrypt
decrypted_text = ''
for ch in cipher:
    if not ch.isalpha():
        continue

    d_code = ord(ch) - 1
    if d_code < ord('A'):
        d_code = ord('Z')

    decrypted_text += chr(d_code)

print(decrypted_text)