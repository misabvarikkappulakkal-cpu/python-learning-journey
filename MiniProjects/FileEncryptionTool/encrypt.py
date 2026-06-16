from cryptography.fernet import Fernet

# Generate key
key = Fernet.generate_key()

# Save key
with open("secret.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

# Read file
with open("sample.txt", "rb") as file:
    data = file.read()

# Encrypt
encrypted_data = cipher.encrypt(data)

# Save encrypted file
with open("encrypted_files/encrypted_sample.txt", "wb") as file:
    file.write(encrypted_data)

print("File encrypted successfully!")
print("Key saved as secret.key")