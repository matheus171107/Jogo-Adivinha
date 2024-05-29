import random

def jogo_aidivinhacao():
    numeroS = random.randint(1, 100)
    tentativas = 0
    Ntentativas = 0

    while tentativas != numeroS:
        try:
            tentativas = int(input('Digite seu palpite :'))
            Ntentativas += 1
            if tentativas < numeroS:
                print("Digite um valor mais alto!")
            elif tentativas > numeroS:
                print("Digite um valor mais baixo!") 
        except ValueError:
            print("Por Favor, digite um número valido!")
    print(f'Parabéns! Você acertou, número: {numeroS} com {Ntentativas} tentativas')

if __name__ == "__main__":
    jogo_aidivinhacao()