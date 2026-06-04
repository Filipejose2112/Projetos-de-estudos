
# Dicionário onde a CHAVE é o produto e o VALOR é o preço por unidade
estoque = {
    "banana": 1.50,
    "maça": 2.00,
    "tomate": 3.50,
    "alface": 2.50
}

# CARRINHO DE COMPRAS
carrinho = {}


def mostrar_produtos():  # Função para mostrar os produtos do estoque.
    print("=" * 40)
    print("BEM-VINDO AO HORTIFRÚTI SHIRIAOSNAIAH!")
    print("=" * 40)
    print('\nAqui está os nossos produtos e valores: ')
    for produto, preco in estoque.items():
        print(f'{produto.capitalize()}: R${preco:.2f}')


def escolhendo_pro_carinho():  # funcão para adicionar produtos ao carrinho.

    global carrinho

    while True:

        escolha = input(
            '\nDiga o nome do produto que você deseja comprar e a quantidade desejada: ').strip().lower()

        if escolha not in estoque:
            print(
                "Não temos esse produto no nosso estoque. Digite outro: ")
            continue

        print(escolha + " adicionado ao carrinho!")

        try:
            quantidade_pedida = int(input(
                'Diga quantas unidades de ' + escolha + ' você quer adicionar ao carrinho: '))
            if quantidade_pedida <= 0:
                print("quantidade pedida inválida. Informe um número maior que zero.")
                continue
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
            continue

        carrinho[escolha] = quantidade_pedida
        print(f'{quantidade_pedida} unidades de {escolha} adicionado ao carrinho!')

        continuar = input(
            'Deseja adicionar mais alguma coisa ao seu carrinho? ').strip().lower()
        if continuar != 'sim':
            break


def gerenciando_carrinho():  # Para gerenciar os itens que estão dentro do carrinho.

    global quantidade_pedida, carrinho

    while True:

        if not carrinho:
            print('\nCarrinho vazio.')

        else:
            print("\nvocê pediu os seguintes itens: ")
            for escolha, quantidade_pedida in carrinho.items():
                print(f"{escolha} - {quantidade_pedida} unidades")

        print("\n[1] Adicionar/Alterar quantidade de um produto")
        print("[2] Remover totalmente um produto")
        print("[3] Continuar para o pagamento")

        modificar = input("Qual opção você escolhe? ").strip()

        if modificar == '1':  # caso tenha interesse em remover unidades do produto ou adicionar um novo produto

            item = input("Diga o nome do produto: ").strip().lower()

            if item not in estoque:
                print("O item não se encontra no nosso estoque. Por favor, diga outro: ")
                continue

            try:
                quantidade_pedida = int(
                    input(f'Quantas unidades de {item} você quer no carrinho? '))
                if quantidade_pedida <= 0:
                    print("Quantidade inválida!")
                    continue

                carrinho[item] = quantidade_pedida
                print(f"Foi atualizado para {quantidade_pedida} unidades!")
            except ValueError:
                print("Por favor, digite um número que seja válido.")

        # para remover totalmente totalmente um item do carrinho.
        elif modificar == '2':
            if not carrinho:
                print("O seu carrinho está vazio, e não há o que ser removido.")
                continue

            item = input(
                "Digite o nome do produto que deseja remover: ").strip().lower()

            if item not in carrinho:
                print("Esse produto não está no seu carrinho.")
            else:
                del carrinho[item]
                print(f"{item} foi removido do carrinho.")

        elif modificar == '3':  # para ir pra seção de mostrar o valor a ser pago e depois ir pro pagamento

            print("Saindo do gerenciamento de carrinho...")
            break

        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")


def mostrar_carrinho_atual():  # mostrar o que tem no carrinho antes de ir pro pagamento

    carrinho_valor = 0

    print('  SEU CARRINHO:    ')
    print('\n' + '=' * 40)
    for escolha, quantidade_pedida in carrinho.items():
        valor_item = estoque[escolha] * quantidade_pedida
        print(f"{escolha.capitalize()} x {quantidade_pedida} = R${valor_item:.2f}")
        carrinho_valor += valor_item
    print(f'\nValor do pagamento será de : R${carrinho_valor:.2f}')


def pagamento_final():  # opçoes de pagamentos

    while True:
        metodo_pagamento = input(
            'Escolha o método de pagamento (dinheiro/cartão): ').lower().strip()

        if metodo_pagamento == 'dinheiro':
            print(
                'Pagamento em dinheiro selecionado. Por favor, pague o valor total ao garçom.')
            break
        elif metodo_pagamento == 'cartão':
            print(
                'Pagamento com cartão selecionado. Por favor, insira seu cartão na máquina.')
            break
        else:
            print(
                'Método de pagamento inválido. Por favor, escolha entre dinheiro ou cartão.')


mostrar_produtos()
escolhendo_pro_carinho()
gerenciando_carrinho()
mostrar_carrinho_atual()
pagamento_final()
