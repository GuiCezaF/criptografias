from vigenere import Vigenere
import sys
 
versao = sys.version_info[0]
 
if versao == 2:
    leitura = raw_input
elif versao == 3:
    leitura = input
 
txt_in = leitura('Texto a ser cifrado: ')
password = leitura('Senha: ')
 
cifra = Vigenere()
txt_cifrado = cifra.encrypt(txt_in, password)

print('Texto cifrado: {0}'.format(txt_cifrado))
print('  Texto plano: {0}'.format(cifra.decrypt(txt_cifrado, password)))
