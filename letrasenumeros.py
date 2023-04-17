import random
import string
def gerarsenha():
    print("escolha o tamanho da sua senha:")
    tamanho = int(input(">>>"))
    senha = "".join(random.choice(string.ascii_letters + string.digits) for i in range(tamanho))
    print(senha)
    input("aperte enter para prosseguir")
    
