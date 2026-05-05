import json
import os

ARQUIVO = "pedidos.json"

CARDAPIO = {
    1: {"item": "Coxinha", "preco": 8.00},
    2: {"item": "Pão de queijo", "preco": 6.00},
    3: {"item": "Misto quente", "preco": 12.00},
    4: {"item": "Suco natural", "preco": 10.00},
    5: {"item": "Refrigerante", "preco": 7.00},
    6: {"item": "Água", "preco": 4.00},
    7: {"item": "Café", "preco": 5.00},
    8: {"item": "Chocolate", "preco": 6.50}
}

def carregar_pedidos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_pedidos(pedidos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

def mostrar_cardapio():
    print("\n===== CARDÁPIO DA CANTINA =====")
    for codigo, produto in CARDAPIO.items():
        print(f"{codigo} - {produto['item']} | R$ {produto['preco']:.2f}")
    print("0 - Voltar")

def escolher_item_cardapio():
    mostrar_cardapio()

    try:
        codigo = int(input("Escolha o número do item: "))

        if codigo == 0:
            return None

        if codigo not in CARDAPIO:
            print("❌ Item inválido.")
            return None

        return CARDAPIO[codigo]

    except ValueError:
        print("❌ Digite apenas números.")
        return None

def listar_pedidos():
    pedidos = carregar_pedidos()

    if not pedidos:
        print("\n⚠️ Nenhum pedido encontrado.\n")
        return

    print("\n📋 Pedidos:")
    for i, p in enumerate(pedidos):
        print(
            f"{i} - {p['nome']} | {p['item']} | "
            f"Qtd: {p['quantidade']} | Total: R$ {p['total']:.2f} | {p['status']}"
        )

def criar_pedido():
    nome = input("Nome do aluno: ").strip()

    if not nome:
        print("❌ Informe o nome do aluno.")
        return

    produto = escolher_item_cardapio()

    if produto is None:
        print("Pedido cancelado.")
        return

    try:
        quantidade = int(input("Quantidade: "))

        if quantidade <= 0:
            print("❌ Quantidade inválida.")
            return

    except ValueError:
        print("❌ Digite uma quantidade válida.")
        return

    total = produto["preco"] * quantidade

    pedidos = carregar_pedidos()

    pedidos.append({
        "nome": nome,
        "item": produto["item"],
        "preco_unitario": produto["preco"],
        "quantidade": quantidade,
        "total": total,
        "status": "Preparando"
    })

    salvar_pedidos(pedidos)
    print(f"✅ Pedido criado! Total: R$ {total:.2f}")

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

    except ValueError:
        print("❌ Digite apenas números.")

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

    except ValueError:
        print("❌ Digite apenas números.")

def buscar_pedido():
    nome = input("Nome do aluno: ").strip()
    pedidos = carregar_pedidos()

    encontrados = [p for p in pedidos if p["nome"].lower() == nome.lower()]

    if not encontrados:
        print("❌ Nenhum pedido encontrado.")
        return

    print("\n🔎 Pedidos encontrados:")
    for p in encontrados:
        print(
            f"{p['nome']} | {p['item']} | Qtd: {p['quantidade']} | "
            f"Total: R$ {p['total']:.2f} | {p['status']}"
        )

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

        print("\nEscolha o novo item do cardápio:")
        produto = escolher_item_cardapio()

        if produto is None:
            print("Edição cancelada.")
            return

        quantidade = int(input("Nova quantidade: "))

        if quantidade <= 0:
            print("❌ Quantidade inválida.")
            return

        total = produto["preco"] * quantidade

        pedidos[index]["item"] = produto["item"]
        pedidos[index]["preco_unitario"] = produto["preco"]
        pedidos[index]["quantidade"] = quantidade
        pedidos[index]["total"] = total

        salvar_pedidos(pedidos)

        print(f"✅ Pedido atualizado! Novo total: R$ {total:.2f}")

    except ValueError:
        print("❌ Digite apenas números.")

def menu():
    while True:
        print("\n===== CANTINA FIAP =====")
        print("1 - Ver cardápio")
        print("2 - Criar pedido")
        print("3 - Listar pedidos")
        print("4 - Atualizar status")
        print("5 - Cancelar pedido")
        print("6 - Buscar pedido")
        print("7 - Editar pedido")
        print("0 - Sair")

        op = input("Escolha: ")

        if op == "1":
            mostrar_cardapio()
        elif op == "2":
            criar_pedido()
        elif op == "3":
            listar_pedidos()
        elif op == "4":
            atualizar_status()
        elif op == "5":
            cancelar_pedido()
        elif op == "6":
            buscar_pedido()
        elif op == "7":
            editar_pedido()
        elif op == "0":
            print("Saindo do sistema...")
            break
        else:
            print("❌ Opção inválida")

menu()