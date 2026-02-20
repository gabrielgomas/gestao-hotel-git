from clientes import Cliente
from quartos import Quarto
from reservas import Reserva

# Simulação de base de dados em memória
lista_quartos = [Quarto(101, "Single", 50), Quarto(102, "Double", 80)]
lista_clientes = []
lista_reservas = []

def menu():
    print("\n--- HOTEL GEST PRO ---")
    print("1. Registar Cliente")
    print("2. Ver Quartos Disponíveis")
    print("3. Criar Reserva")
    print("4. Listar Reservas")
    print("0. Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()
    
    if opcao == "1":
        id_c = len(lista_clientes) + 1
        nome = input("Nome do cliente: ")
        email = input("Email: ")
        novo_cliente = Cliente(id_c, nome, email)
        lista_clientes.append(novo_cliente)
        print("Cliente registado com sucesso!")

    elif opcao == "2":
        print("\n--- Quartos ---")
        for q in lista_quartos:
            print(q)

    elif opcao == "3":
        if not lista_clientes:
            print("Erro: Precisa de registar um cliente primeiro.")
            continue
        
        # Mostra quartos livres
        disponiveis = [q for q in lista_quartos if q.disponivel]
        if not disponiveis:
            print("Não há quartos disponíveis.")
            continue
            
        for q in disponiveis: print(q)
        num_q = int(input("Número do quarto para reservar: "))
        
        # Encontra o quarto e o cliente (simplificado: usa o último cliente)
        quarto_escolhido = next((q for q in disponiveis if q.numero == num_q), None)
        if quarto_escolhido:
            noites = int(input("Quantas noites? "))
            res = Reserva(len(lista_reservas)+1, lista_clientes[-1], quarto_escolhido, noites)
            lista_reservas.append(res)
            print("Reserva confirmada!")
        else:
            print("Quarto inválido.")

    elif opcao == "4":
        for r in lista_reservas:
            print(r)

    elif opcao == "0":
        break