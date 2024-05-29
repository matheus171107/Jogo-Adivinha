import random

numeroS = random.randint(1, 100)
tentativas = 0
Ntentativas = 0

while tentativas != numeroS:
    tentativas = int(input('Digite seu palpite :'))
    Ntentativas += 1
    if tentativas < numeroS:
        print("Digite um valor mais alto!")
    elif tentativas > numeroS:
        print("Digite um valor mais baixo!") 

print(f'Você acertou, número: {numeroS} com {Ntentativas} tentativas')