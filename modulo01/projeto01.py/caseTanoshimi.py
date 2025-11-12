import random
import time

# --------------------------
# CARDÁPIO DO RESTAURANTE 🍣
# --------------------------

cardapio = {
    "Entradas": {
        "1": {
            "nome": "Sunomono",
            "descricao": "Salada de pepino com vinagre de arroz e gergelim.",
            "preco": 12.90
        },
        "2": {
            "nome": "Guioza (6 unid)",
            "descricao": "Pastel japonês recheado com carne e legumes.",
            "preco": 18.50
        },
        "3": {
            "nome": "Shimeji na manteiga",
            "descricao": "Cogumelos salteados na manteiga com molho shoyu.",
            "preco": 22.90
        }
    },
    "Sushis e Sashimis": {
        "4": {
            "nome": "Combinado 12 peças",
            "descricao": "Mix de sushis e sashimis variados.",
            "preco": 35.90
        },
        "5": {
            "nome": "Combinado 20 peças",
            "descricao": "Seleção premium de peixes frescos e nigiris.",
            "preco": 52.90
        },
        "6": {
            "nome": "Sashimi de salmão (10 unid)",
            "descricao": "Fatias frescas de salmão norueguês.",
            "preco": 38.90
        }
    },
    "Pratos quentes": {
        "7": {
            "nome": "Yakissoba tradicional",
            "descricao": "Macarrão oriental com legumes e carne ao molho shoyu.",
            "preco": 32.00
        },
        "8": {
            "nome": "Tempurá de legumes",
            "descricao": "Legumes empanados e fritos na massa leve japonesa.",
            "preco": 27.50
        },
        "9": {
            "nome": "Lámen de carne",
            "descricao": "Sopa japonesa com macarrão, carne e caldo especial.",
            "preco": 29.90
        }
    },
    "Bebidas": {
        "10": {
            "nome": "Água",
            "descricao": "Garrafa 500ml - sem gás.",
            "preco": 4.00
        },
        "11": {
            "nome": "Refrigerante",
            "descricao": "Lata 350ml - diversas opções.",
            "preco": 6.00
        },
        "12": {
            "nome": "Saquê",
            "descricao": "Bebida alcoólica tradicional japonesa.",
            "preco": 15.00
        }
    }
}

pedidos = []
numeros_usados = set()

# --------------------------
# FUNÇÕES DO SISTEMA
# --------------------------

def gerar_numero_pedido():
    """Gera número de pedido único"""
    while True:
        numero = random.randint(1000, 9999)
        if numero not in numeros_usados:
            numeros_usados.add(numero)
            return numero

def mostrar_cardapio():
    """Exibe o cardápio formatado"""
    print("\n🍱 CARDÁPIO DIGITAL 🍱")
    for categoria, itens in cardapio.items():
        print(f"\n=== {categoria} ===")
        for codigo, info in itens.items():
            print(f"{codigo}. {info['nome']} - R${info['preco']:.2f}")
            print(f"   {info['descricao']}")
    print()

def fazer_pedido():
    """Cliente informa mesa e escolhe itens pelo número"""
    mesa = input("\nDigite o número da sua mesa: ").strip()
    mostrar_cardapio()

    selecionados = input("Digite os números dos itens desejados separados por vírgula: ")
    selecionados = [x.strip() for x in selecionados.split(",")]

    pedido_itens = []
    total = 0.0

    for codigo in selecionados:
        for categoria in cardapio.values():
            if codigo in categoria:
                item = categoria[codigo]
                pedido_itens.append(item)
                total += item["preco"]

    if pedido_itens:
        numero_pedido = gerar_numero_pedido()
        pedido = {
            "numero": numero_pedido,
            "mesa": mesa,
            "itens": pedido_itens,
            "total": total,
            "status": "Pendente"
        }
        pedidos.append(pedido)
        print("\n🧾 Pedido registrado com sucesso!")
        print(f"📌 Número do pedido: {numero_pedido}")
        print(f"💰 Total: R${total:.2f}\n")
    else:
        print("❌ Nenhum item válido selecionado.")

def listar_pedidos():
    """Lista todos os pedidos registrados"""
    print("\n📋 PEDIDOS REGISTRADOS")
    if not pedidos:
        print("Nenhum pedido encontrado.")
    else:
        for p in pedidos:
            print(f"\nPedido #{p['numero']} | Mesa {p['mesa']} | Status: {p['status']}")
            for item in p["itens"]:
                print(f" - {item['nome']} (R${item['preco']:.2f})")
            print(f"Total: R${p['total']:.2f}")

def efetuar_pagamento():
    """Processa o pagamento de um pedido existente"""
    numero = input("\nDigite o número do pedido: ").strip()
    for pedido in pedidos:
        if str(pedido["numero"]) == numero:
            if pedido["status"] == "Pago":
                print("⚠️ Este pedido já foi pago.")
                return
            print(f"\nMesa {pedido['mesa']} - Total: R${pedido['total']:.2f}")
            forma = input("Forma de pagamento (cartão, pix, dinheiro): ").lower()

            if forma == "pix":
                codigo_pix = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=15))
                print(f"\n📱 Código PIX gerado: {codigo_pix}")
                print("Aguardando confirmação do pagamento...")
                time.sleep(2)
                print("✅ Pagamento via PIX confirmado!")
            
            elif forma == "cartão":
                print("\n💳 Aproximando o cartão...")
                time.sleep(2)
                print("✅ Pagamento via cartão aprovado!")

            elif forma == "dinheiro":
                print("\n💵 Aguarde o garçom com o troco...")
                time.sleep(2)
                print("✅ Pagamento em dinheiro confirmado!")

            else:
                print("❌ Forma de pagamento inválida.")
                return

            pedido["status"] = "Pago"
            pedido["forma_pagamento"] = forma.capitalize()
            print("🍣 Obrigado pela preferência!\n")
            return
    print("❌ Pedido não encontrado.")

# --------------------------
# MENU PRINCIPAL
# --------------------------

def menu():
    while True:
        print("\n====== RESTAURANTE TANOSHIMI ======")
        print("1. Ver cardápio")
        print("2. Fazer pedido")
        print("3. Ver pedidos")
        print("4. Efetuar pagamento")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                mostrar_cardapio()
            case "2":
                fazer_pedido()
            case "3":
                listar_pedidos()
            case "4":
                efetuar_pagamento()
            case "0":
                print("👋 Encerrando o sistema. Até logo!")
                break
            case _:
                print("Opção inválida, tente novamente.")

menu()