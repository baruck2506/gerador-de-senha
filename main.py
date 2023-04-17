import letrasenumeros
import numeros
import time

while True:
    print("selecione o tipo de senha que deseja gerar:")
    print("1.Letras e numeros")
    print("2.Apenas numeros")
    print("3.Sair")
    escolha = input(">>>")
    opcoes = ["1", "2", "3"]

    if escolha not in opcoes:
        print("por favor escolha uma opção valida")

    if escolha == "1":
        letrasenumeros.gerarsenha()
        input("Aperte enter para prosseguir")
    elif escolha == "2":
        numeros.gerarnumeros()
        input("Aperte enter para prosseguir")
    elif escolha == "3":
        print("saindo...")
        time.sleep(3)
        break