from Crypto.Cipher import Blowfish
cipher = Blowfish.new("key must be 4 to 56 bytes")
encrypted_data = cipher.encrypt("1234hack")

decrypted_data = cipher.decrypt(encrypted_data)
decrypted_data = decrypted_data.decode("utf-8")

print ("Encrypted Text: ", encrypted_data)
print ("Decrypted Text: ", decrypted_data)







from Crypto.Cipher import Blowfish

def PKCS5Padding(string):
    byteNum = len(string)
    packingLength = 8 - byteNum % 8
    if packingLength == 8:
        return string
    else:
        appendage = chr(packingLength) * packingLength
        return string + appendage

def PandoraEncrypt(string):
    from Crypto.Cipher import Blowfish
    key = b'6#26FRL$ZWD'
    c1  = Blowfish.new(key, Blowfish.MODE_ECB)
    packedString = PKCS5Padding(string)
    return c1.encrypt(packedString)
