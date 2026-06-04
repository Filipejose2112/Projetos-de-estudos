
# Simulação de um sistema de pedidos em um restaurante;
# O programa apresenta um cardápio de comidas e bebidas, permite que o usuário faça pedidos, calcula o valor total e processa o pagamento;
# O programa também verifica o estoque dos itens e atualiza o estoque após cada pedido.

cardapio_comida = {
    'pizza': 20.00,
    'hamburguer': 15.00,
    'sanduiche': 10.00,
    'salada': 8.00,
    'sopa': 12.00
}

cardapio_bebida = {
    'refrigerante': 5.00,
    'suco': 4.00,
    'agua': 2.00,
    'cerveja': 6.00,
    'vinho': 10.00
}

estoque_geral = {
    'pizza': 5,
    'hamburguer': 5,
    'sanduiche': 5,
    'salada': 5,
    'sopa': 5,
    'refrigerante': 5,
    'suco': 5,
    'agua': 5,
    'cerveja': 5,
    'vinho': 5
}


total_comida = 0
total_bebida = 0
total_pedidos = []


def mostrar_cardapio():
    print("olá! Bem-vindo ao nosso restaurante SHIRIAOSNAIAH! Aqui está o nosso cardápio:")
    print('\nCOMIDAS:')
    for comida, preco in cardapio_comida.items():
        print(f'{comida.capitalize()}: R${preco:.2f}')

    print('\nBEBIDAS:')
    for bebida, preco in cardapio_bebida.items():
        print(f'{bebida.capitalize()}: R${preco:.2f}')


def fazer_pedido():  # função para fazer os pedidos.

    global total_comida, total_bebida, total_pedidos

    while True:
        pedido = input('\nDigite o nome do prato ou bebida: ').lower().strip()

        # para saber se o produto existe no estoque
        if pedido not in cardapio_comida and pedido not in cardapio_bebida:
            print('Desculpe, não temos esse item no cardápio.')
            continue

        # Depois, chega se tem no estoque
        if estoque_geral[pedido] <= 0:
            print(
                'Desculpe, esse item acaba de esgotar. Por favor, escolha outro item do cardápio.')
            continue

        # Caso o cliente digite uma letra e não um número, o programa não quebre e apresente erro
        try:
            quantidade = int(
                input(f'Quantas unidades de {pedido.capitalize()} você deseja comprar? '))
            if quantidade <= 0:
                print(
                    "Quantidade desejada é invalida. Digite um número que seja maior que zero.")
                continue

            # Caso aconteça do cliente pedir mais do que tem no estoque
            if quantidade > estoque_geral[pedido]:
                print(
                    f"Desculpe, mas só temos {estoque_geral[pedido]} no nosso estoque.")
                continue
        except ValueError:
            print(
                "Por favor, digite um número inteiro que seja válido para a quantidade do produto desejado.")
            continue

        # Para processar a o pedido do cliente
           # Comida
        if pedido in cardapio_comida:
            total_comida += cardapio_comida[pedido] * quantidade
            print(f'{quantidade}x {pedido.capitalize()} foram adicionado(s)!')

            # Bebida
        elif pedido in cardapio_bebida:
            total_bebida += cardapio_bebida[pedido] * quantidade
            print(f'{quantidade}x {pedido.capitalize()} foram adicionado(s)!')

            # Para atualizar o estoque sempre que o cliente fizer um pedido
        estoque_geral[pedido] -= quantidade
        for _ in range(quantidade):
            # Para adicionar na lista a quantidade de vezes que um produto foi pedido
            total_pedidos.append(pedido)

        # caso ele queria pedir mais alguma coisa ou então seguir para finalizar o pedido.
        continuar = input(
            'Deseja fazer mais um pedido? (s/n): ').lower().strip()
        if continuar != 's':
            break


def mostrar_resumo():  # função para mostrar o resumo dos pedidos.

    valor_total = total_comida + total_bebida
    print('\n' + '=' * 40)
    print('  RESUMO DOS SEUS PEDIDOS    ')
    print('\n' + '=' * 40)

    if not total_pedidos:  # Caso nenhum pedido seja feito
        print("Desculpe, mas nenhum pedido foi realizado.")
        return

    print('\nVocê pediu os seguintes itens e quantidades:')
    for item in set(total_pedidos):
        quantidade = total_pedidos.count(item)
        print(f'{item.capitalize()}: {quantidade}x')

    print(f'\nValor total a pagar: R${valor_total:.2f}')


def pagamento():  # Função para processar o pagamento.

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

# resumo do programa.


mostrar_cardapio()
fazer_pedido()
mostrar_resumo()
pagamento()
