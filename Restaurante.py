
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
    'pizza': 2,
    'hamburguer': 2,
    'sanduiche': 2,
    'salada': 2,
    'sopa': 2,
    'refrigerante': 2,
    'suco': 2,
    'agua': 2,
    'cerveja': 2,
    'vinho': 2
}


# Variáveis para controlar os pedidos e o valor total.

total_comida = 0
quantidade_pedida = 0
total_bebida = 0
quantidade_bebida = 0
valor_total = 0
total_pedidos = []


def mostrar_cardapio():
    print("olá! Bem-vindo ao nosso restaurante! Aqui está o nosso cardápio:")
    print('\nCOMIDAS:')
    for comida, preco in cardapio_comida.items():
        print(f'{comida.capitalize()}: R${preco:.2f}')

    print('\nBEBIDAS:')
    for bebida, preco in cardapio_bebida.items():
        print(f'{bebida.capitalize()}: R${preco:.2f}')


def fazer_pedido():  # função para fazer os pedidos.

    global total_comida, quantidade_pedida, total_bebida, quantidade_bebida, total_pedidos

    while True:
        pedido = input('\nDigite o nome do prato ou bebida: ').lower().strip()

        if pedido not in cardapio_comida and pedido not in cardapio_bebida:
            print('Desculpe, não temos esse item no cardápio.')
            continue

        if estoque_geral[pedido] <= 0:
            print(
                'Desculpe, esse item acaba de esgotar. Por favor, escolha outro item do cardápio.')
            continue

        # para pedidos de comida.

        if pedido in cardapio_comida:
            quantidade_pedida += 1
            total_comida += cardapio_comida[pedido]
            estoque_geral[pedido] -= 1
            total_pedidos.append(pedido)
            print(
                f'Você pediu {pedido.capitalize()} por R${cardapio_comida[pedido]:.2f}.')

            # para pedir bebidas.

        elif pedido in cardapio_bebida:
            quantidade_bebida += 1
            total_bebida += cardapio_bebida[pedido]
            estoque_geral[pedido] -= 1
            total_pedidos.append(pedido)
            print(
                f'Você pediu {pedido.capitalize()} por R${cardapio_bebida[pedido]:.2f}.')

        continuar = input(
            # caso ele queria pedir mais alguma coisa ou então seguir para finalizar o pedido.
            'Deseja fazer mais um pedido? (s/n): ').lower().strip()
        if continuar != 's':
            break


def mostrar_resumo():  # função para mostrar o resumo dos pedidos.

    valor_total = total_comida + total_bebida
    print('\n' + '=' * 40)
    print('  RESUMO DOS SEUS PEDIDOS    ')
    print('\n' + '=' * 40)
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
