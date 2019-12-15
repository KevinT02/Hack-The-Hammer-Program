from random import randrange
from Crypto.Cipher import AES
from Crypto.Cipher import Blowfish
from Crypto.PublicKey import RSA
from Crypto import Random
from cryptography.fernet import Fernet
txt = open('TEXT.txt', 'r+')
contents = []
order = []
cipherTxt = []
decoded = []
key = []
def algorithm1(text):
  my_str_as_bytes = str.encode(text)
  type(my_str_as_bytes)
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)
  cipher_text = cipher_suite.encrypt(my_str_as_bytes)
  plain_text = str(cipher_suite.decrypt(cipher_text))
  print(cipher_text)
  clean = plain_text.replace("b", "", 1)
  print (clean)
  return cipher_text, key
def algorithm2(text):
  my_str_as_bytes = str.encode(text)
  type(my_str_as_bytes)
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)
  cipher_text = cipher_suite.encrypt(my_str_as_bytes)
  plain_text = str(cipher_suite.decrypt(cipher_text))
  print(cipher_text)
  clean = plain_text.replace("b", "", 1)
  print (clean)
  return cipher_text, key
def chunks(lst, chunkSize):
  for i in range(0,len(lst), chunkSize):
    yield lst[i:i+chunkSize]
for words in txt:
  for i in words:
    contents.append(i)
chunkedlst = list(chunks(contents,16))
print(chunkedlst)
Rolls = len(list(chunks(contents,16)))
for i in range(0,Rolls, 1):
  order.append(randrange(1,3))
print (order)
for i in range(0, len(order)):
  if (order[i] == 1):
   results1 = algorithm1(str(order[i]))
   cipherTxt.append(results1[0])
   key.append(results1[1])
  else:
    results2= algorithm2(str(order[i]))
    cipherTxt.append(results2[0])
    key.append(results2[1])
print(cipherTxt)
'''
def algorithm3(text, key):
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)
  plain_text = str(cipher_suite.decrypt(text))
  print(cipher_text)
  clean = plain_text.replace("b", "", 1)
  print (clean)
  return clean
def algorithm4(text, key):
  key = Fernet.generate_key()
  cipher_suite = Fernet(key)
  plain_text = str(cipher_suite.decrypt(text))
  print(cipher_text)
  clean = plain_text.replace("b", "", 1)
  print (clean)
  return clean
for i in range(0,len(order)):
  if (order[i] == 1):
    decoded.append(algorithm3(cipherTxt[i], key[i]))
  else:
    decoded.append(algorithm4(cipherTxt[i], key[i]))
print(decoded)
'''
