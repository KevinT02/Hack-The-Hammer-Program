import random
txt = open('TEXT.txt', 'r+')
contents = []
def algorithm1():
  from Crypto.PublicKey import RSA
  from Crypto import Random
  random_generator = Random.new().read
  key = RSA.generate(1024, random_generator)
  key
  enc_data = key.publickey().encrypt(b'abcd', 32)
  print(enc_data)
  b = key.decrypt(enc_data)
  message = str(b)
  clean = message.replace("b", "", 1)
  print (clean)
def algorithm2 (): #this only works with 16 characters.
  from Crypto.Cipher import AES
  obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  message = "ds8888hiytuhjbgh"
  ciphertext = obj.encrypt(message)
  print(ciphertext)
  obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
  decrypted = obj2.decrypt(ciphertext)
  decrypted = decrypted.decode("utf-8")
  print(decrypted)
def algorithm3(text):
  from Crypto.Cipher import Blowfish
  cipher = Blowfish.new("key must be 4 to 56 bytes")
  encrypted_data = cipher.encrypt(text)

  decrypted_data = cipher.decrypt(encrypted_data)
  decrypted_data = decrypted_data.decode("utf-8")

  print ("Encrypted Text: ", encrypted_data)
  print ("Decrypted Text: ", decrypted_data)
for words in txt:
  for i in words:
    contents.append(i)
print(len(contents))
groups = round(len(contents)/16)
for i in range(0,groups):
  print(random(1,3))
