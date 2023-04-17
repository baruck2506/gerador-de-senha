import random
import string
def gerarnumeros():
    print("escolha o tamanho da sua senha:")
    tamanho = int(input(">>>"))
    senha = "".join(random.choice(string.digits) for i in range(tamanho))
    print("A senha gerada:", senha)