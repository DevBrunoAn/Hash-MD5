import hashlib

def cript():
    cript_key = input('Digite o que você quer criptografar: ')
    resultado = hashlib.md5(cript_key.encode())
  

    print(resultado.hexdigest())