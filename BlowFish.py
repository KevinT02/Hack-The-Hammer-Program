from Crypto.Cipher import Blowfish
cipher = Blowfish.new("message must be between 4 and 56 bytes")
message2 = input()
message2_as_bytes = str.encode(message2)
type(message2_as_bytes)

encrypted_data = cipher.encrypt(message2_as_bytes)

decrypted_data = cipher.decrypt(encrypted_data)
decrypted_data = decrypted_data.decode("utf-8")

print ("Encrypted Text: ", encrypted_data)
print ("Decrypted Text: ", decrypted_data)
