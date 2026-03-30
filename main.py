import json
import os

ARQUIVO = "pedidos.json"

def carregar_pedidos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_pedidos(pedidos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

def listar_pedidos():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("\n⚠️ Nenhum pedido encontrado.\n")
        return

    print("\n📋 Pedidos:")
    for i, p in enumerate(pedidos):
        print(f"{i} - {p['nome']} | {p['item']} | {p['status']}")

def criar_pedido():
    nome = input("Nome do aluno: ").strip()
    item = input("Item: ").strip()

    if not nome or not item:
        print("❌ Preencha todos os campos.")
        return

    pedidos = carregar_pedidos()

    pedidos.append({
        "nome": nome,
        "item": item,
        "status": "Preparando"
    })

    salvar_pedidos(pedidos)
    print("✅ Pedido criado!")

def cancelar_pedido():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("❌ Nenhum pedido.")
        return

    listar_pedidos()

    try:
        index = int(input("Número do pedido: "))

        if index < 0 or index >= len(pedidos):
            print("❌ Número inválido.")
            return

        pedidos.pop(index)
        salvar_pedidos(pedidos)

        print("✅ Pedido cancelado!")

    except:
        print("❌ Erro.")

def atualizar_status():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("❌ Nenhum pedido.")
        return

    listar_pedidos()

    try:
        index = int(input("Número do pedido: "))

        if index < 0 or index >= len(pedidos):
            print("❌ Número inválido.")
            return

        pedidos[index]["status"] = "Pronto"
        salvar_pedidos(pedidos)

        print("✅ Status atualizado!")

    except:
        print("❌ Erro.")

def buscar_pedido():
    nome = input("Nome do aluno: ").strip()
    pedidos = carregar_pedidos()

    encontrados = [p for p in pedidos if p["nome"].lower() == nome.lower()]

    if not encontrados:
        print("❌ Nenhum pedido encontrado.")
        return

    for p in encontrados:
        print(f"{p['nome']} | {p['item']} | {p['status']}")

def editar_pedido():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("❌ Nenhum pedido.")
        return

    listar_pedidos()

    try:
        index = int(input("Número do pedido: "))

        if index < 0 or index >= len(pedidos):
            print("❌ Número inválido.")
            return

        novo_item = input("Novo item: ").strip()

        if not novo_item:
            print("❌ Item inválido.")
            return

        pedidos[index]["item"] = novo_item
        salvar_pedidos(pedidos)

        print("✅ Pedido atualizado!")

    except:
        print("❌ Erro.")

def menu():
    while True:
        print("\n===== CANTINA FIAP =====")
        print("1 - Criar pedido")
        print("2 - Listar pedidos")
        print("3 - Atualizar status")
        print("4 - Cancelar pedido")
        print("5 - Buscar pedido")
        print("6 - Editar pedido")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            criar_pedido()
        elif op == "2":
            listar_pedidos()
        elif op == "3":
            atualizar_status()
        elif op == "4":
            cancelar_pedido()
        elif op == "5":
            buscar_pedido()
        elif op == "6":
            editar_pedido()
        elif op == "0":
            break
        else:
            print("❌ Opção inválida")

menu()