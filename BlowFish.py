from Crypto.Cipher import Blowfish
cipher = Blowfish.new("key must be 4 to 56 bytes")
encrypted_data = cipher.encrypt("1234hack")

decrypted_data = cipher.decrypt(encrypted_data)
decrypted_data = decrypted_data.decode("utf-8")

print ("Encrypted Text: ", encrypted_data)
print ("Decrypted Text: ", decrypted_data)
