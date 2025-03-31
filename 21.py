import os
os.system("cls")
import random
import time


CARTAS = [  "A", "A", "A", "A",
            "2", "2", "2", "2",
            "3", "3", "3", "3", 
            "4", "4", "4", "4",
            "5", "5", "5", "5",
            "6", "6", "6", "6", 
            "7", "7", "7", "7", 
            "8", "8", "8", "8", 
            "9", "9", "9", "9", 
            "10", "10", "10", "10",
            "J", "J", "J", "J",
            "Q", "Q", "Q", "Q",
            "K", "K", "K", "K"]

VALORES = {
    'A':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10,
    'J':10,
    'Q':10,
    'K':10    
}

cartasEscolhidas = []
cartasEscolhidasPC = []

def cartasJogador():
    cartasDisponiveis = CARTAS[:]
    cartaEscolhida = random.choice(cartasDisponiveis)
    cartasDisponiveis.remove(cartaEscolhida)
    cartasEscolhidas.append(cartaEscolhida)
    return cartaEscolhida

def cartasJogadorReset():
    cartasEscolhidas.clear()
    cartasEscolhida = ""
    cartasDisponiveis = CARTAS[:]

def cartasPC():
    cartasDisponiveisPC = CARTAS[:]
    cartaEscolhidaPC = random.choice(cartasDisponiveisPC)
    cartasDisponiveisPC.remove(cartaEscolhidaPC)
    cartasEscolhidasPC.append(cartaEscolhidaPC)
    return cartaEscolhidaPC


def cartasPCReset():
    cartasEscolhidasPC.clear()
    cartasEscolhidaPC = ""
    cartasDisponiveisPC = CARTAS[:]
     


def balanco():
    global valorBalanco
    valorBalanco = input("Insira o valor para adicionar ao seu balanço: ")
    while True:
            if valorBalanco.isdigit() == False:
                valorBalanco = input("O valor precisa ser um numero. Insira aqui um valor válido: ")
            else:
                valorBalanco = int(valorBalanco)
                if valorBalanco <= 0:
                      valorBalanco = input("O valor precisa ser maior que zero. Insira aqui um valor válido: ")
                else:
                     break
    return valorBalanco

def aposta():
    global valorAposta
    valorAposta = input("Digite o valor que você quer apostar: ")
    while True:
            if valorAposta.isdigit() == False:
                valorAposta = input("O valor precisa ser um numero. Insira aqui um valor válido: ")
            else:
                valorAposta = int(valorAposta)
                if valorAposta <= 0:
                      valorAposta = input("O valor precisa ser maior que zero. Insira aqui um valor válido: ")
                else:
                     break
    if valorAposta > valorBalanco:
        print("Você não tem esse dinheiro.")
        aposta()
    else:
        return valorAposta


def maisUma():
    if valorTotal() > 21:
         pass
    else:    
        x = input("Digite enter para pegar mais uma carta ou P para parar. ")
        x = x.lower()
        if x != "p":
            print(f"Sua nova carta foi {cartasJogador()} ({valorTotal()} pontos)")
            maisUma()
        else:
            os.system('cls')
            print(f"Você escolheu parar. Sua somativa de pontos foi {valorTotal()}")


def maisUmaPC():     
    if 21>valorTotalPC()>=19:
        rand = random.randint(0, 6)
        if rand == 0:
            cartasPC()
            maisUmaPC()
    elif 19>valorTotalPC()>=15:
        rand = random.randint(0, 2)
        if rand == 0:
            cartasPC()
            maisUmaPC()
    elif 15>valorTotalPC()>=12:
        rand = random.randint(0, 1)
        if rand == 0:
            cartasPC()
            maisUmaPC()
    elif valorTotalPC()<12:
        cartasPC()
        maisUmaPC()
        

def jogoPC():
    cartasPC(), cartasPC(), valorTotalPC()
    maisUmaPC()


def valorCarta(C):
     x = VALORES.get(C)
     return x


def valorTotal():
    soma = 0
    for x in range(len(cartasEscolhidas)):
        soma += (valorCarta(cartasEscolhidas[x - 1]))
    return soma  

def valorTotalPC():
    somaPC = 0
    for x in range(len(cartasEscolhidasPC)):
        somaPC += (valorCarta(cartasEscolhidasPC[x - 1]))
    return somaPC  


def resultado():
    if valorTotalPC() > 21 and valorTotal() > 21:
        print(f"Empate. O computador e você excederam 21. ({valorTotalPC()} e {valorTotal()})")
        draw()
    elif valorTotalPC() > valorTotal() and valorTotal() <= 21 and valorTotalPC() <= 21:
        print(f"O Computador venceu. ({valorTotalPC()} x {valorTotal()})")
        lose()
    elif valorTotalPC() < valorTotal() and valorTotal() <= 21 and valorTotalPC() <= 21:
        print(f"Você venceu. ({valorTotalPC()} x {valorTotal()})")
        win()
    elif valorTotalPC() > 21 and valorTotal() <= 21:
        print(f"Você venceu. ({valorTotalPC()} x {valorTotal()})")
        win()
    elif valorTotal() > 21 and valorTotalPC() <= 21:
        print(f"O Computador venceu. ({valorTotalPC()} x {valorTotal()})")
        lose()
    elif valorTotalPC() == valorTotal():
        print(f"Empate. Ambos tiveram o mesmo valor ({valorTotalPC()} x {valorTotal()})")
        draw()
    print(f"Seu novo balanço é R${valorBalanco}")

def draw():
    pass

def win():
    global valorBalanco
    global valorAposta
    valorBalanco = int(valorBalanco)
    valorBalanco += valorAposta


def lose():
    global valorBalanco
    global valorAposta
    valorBalanco = int(valorBalanco)
    valorBalanco -= valorAposta
     


def escolha():
    aposta()
    print(f"Suas cartas foram {cartasJogador()} e {cartasJogador()} ({valorTotal()} pontos)")
    jogoPC()
    maisUma()


def jogarDeNovo():
    if valorBalanco <=0:
        print("Você não tem mais dinheiro.")
    else:
        os.system('cls')
        time.sleep(0.3), print(".", end="")
        time.sleep(0.3), print(".", end="")
        time.sleep(0.3), print(".", end="")
        time.sleep(0.3), print(".", end="")
        time.sleep(0.3), print(".", end="\n")
        resultado()
        x = input("Digite enter para jogar de novo ou Q para sair. ")
        x = x.lower()
        if x != "q":
            cartasJogadorReset()
            cartasPCReset()
            escolha()
            jogarDeNovo()

def jogo():
    x = input("Digite enter para jogar ou Q para sair. ")
    x = x.lower()
    if x != "q":
        os.system('cls')
        escolha()
        jogarDeNovo()
        
print(f"Seu balanço é R${balanco()}")
jogo()


