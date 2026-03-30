import json
import os

ARQUIVO = "pedidos.json"

def carregar_pedidos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_pedidos(pedidos):
    with open(ARQUIVO, "w") as f:
        json.dump(pedidos, f, indent=4)

def listar_pedidos():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("\nNenhum pedido encontrado.\n")
        return

    print("\nPedidos:")
    for i, p in enumerate(pedidos):
        print(f"{i} - {p['nome']} | {p['item']} | Status: {p['status']}")

def criar_pedido():
    nome = input("Nome do aluno: ")
    item = input("Item pedido: ")

    pedidos = carregar_pedidos()

    pedidos.append({
        "nome": nome,
        "item": item,
        "status": "Preparando"
    })

    salvar_pedidos(pedidos)
    print("Pedido criado!")

def cancelar_pedido():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("Não há pedidos.")
        return

    listar_pedidos()

    try:
        index = int(input("Número do pedido: "))
        pedidos.pop(index)
        salvar_pedidos(pedidos)
        print("Pedido cancelado!")
    except:
        print("Erro.")

def atualizar_status():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("Nenhum pedido.")
        return

    listar_pedidos()

    try:
        index = int(input("Número do pedido: "))
        pedidos[index]["status"] = "Pronto"
        salvar_pedidos(pedidos)
        print("Status atualizado!")
    except:
        print("Erro.")

def menu():
    while True:
        print("\n===== CANTINA FIAP =====")
        print("1 - Listar pedidos")
        print("2 - Fazer pedido")
        print("3 - Cancelar pedido")
        print("4 - Atualizar status")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            listar_pedidos()
        elif op == "2":
            criar_pedido()
        elif op == "3":
            cancelar_pedido()
        elif op == "4":
            atualizar_status()
        elif op == "0":
            break
        else:
            print("Opção inválida")

menu()