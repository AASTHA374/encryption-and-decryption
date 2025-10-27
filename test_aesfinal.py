from aes import AES
from Crypto.Util.Padding import pad, unpad  # pip install pycryptodome

def encrypt_and_decrypt_text():
    plaintext = input("Enter the original text: ").encode()
    key = b"thisisakey123456"  # must be 16 bytes

    aes = AES(key)

    # Padding plaintext to 16-byte multiple
    padded_plaintext = pad(plaintext, 16)
    encrypted = aes.encrypt(padded_plaintext)

    # Decryption
    decrypted_padded = aes.decrypt(encrypted)
    decrypted = unpad(decrypted_padded, 16)

    print("Original Text   :", plaintext)
    print("Encrypted Bytes :", encrypted)
    print("Decrypted Text  :", decrypted)

if __name__ == "__main__":
    encrypt_and_decrypt_text()



