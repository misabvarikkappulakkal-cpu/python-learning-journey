from cryptography.fernet import Fernet

# Load key
with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# Read encrypted file
with open("encrypted_files/encrypted_sample.txt", "rb") as file:
    encrypted_data = file.read()

# Decrypt
decrypted_data = cipher.decrypt(encrypted_data)

# Save decrypted file
with open("decrypted_files/decrypted_sample.txt", "wb") as file:
    file.write(decrypted_data)

print("File decrypted successfully!")