#Meu primeiro prograna
from random import randint # IMporta a funao de gerar números aleatórios 

print("Jodos do dado:")

dado1 = randint(1,6) # gera um númeroentre entre 1 e 5 aleatóriamente  
print("Dado 1: ", dado1)

dado2 = randint(1,6)
print("Dado 2: ", dado2)

dado3 = randint(1,6)
print("Dado3: ", dado3)

dado4 = randint (1,6)
print("Dado4: ", dado4)

Jogador1 = dado1 + dado2
Jogador2 = dado3 + dado4

print("Jogador 1: ", Jogador1)
print("Jogador 2: ", Jogador2)

if Jogador1 > Jogador2:
    print("Jogador 1 venceu!")
elif Jogador2 > Jogador1:
      print("Jogador 2 venceu!")
else:
        print("Empate!")