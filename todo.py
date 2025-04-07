import os

def adicionar():
    while True:
        os.system("cls")
        entradaTodo = input("Insira o lembrete: ")
        entradaData = input("Insira a data do lembrete: ")
        with open("todo.txt", "a") as f:
            f.write(entradaTodo)
            f.write(" ")
            f.write(entradaData)
            f.write("\n")
        x = input("Digite enter para adicionar outro lembrete ou 'q' para sair: ")
        if x == 'q':
            inicio()

def inicio():
    os.system("cls")
    x = input("Deseja adicionar ou visualizar (A/V) seus lembretes? ")
    x = x.lower()
    if x == "a":
        os.system("cls")
        adicionar()
    elif x == "v":
        os.system("cls")
        visualizar()
    elif x == "clear":
        with open("todo.txt", "w") as f:
            f.write("")
            inicio()
    else:
        os.system("cls")
        print("Escolha uma opção válida.")
        inicio()

def visualizar():
    os.system("cls")
    count = 0
    with open("todo.txt", "r") as f:
        for x in f.readlines():
            count +=1
            texto = x
            dadoTodo = texto.split(" ")
            print(f"{count}. {dadoTodo[0]} | {dadoTodo[1]}", end="")
    print("\n")
    deletar()

def deletar():
    x = input("Insira 'q' para sair ou o número do lembrete para removê-lo: ")
    if x.isdigit():
        linhasDeletar = x
        linhasDeletar = int(linhasDeletar)
        linhasDeletar -=1
        with open("todo.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
        if 0<= linhasDeletar < len(linhas):
            del linhas[linhasDeletar]
        with open("todo.txt", "w", encoding="utf-8") as f:
            f.writelines(linhas)
        visualizar()
    else:
        x = x.lower()
        if x == "q":
            inicio() 
    
    
        
def main() -> None:
    inicio()

if __name__ == '__main__':
    main()
