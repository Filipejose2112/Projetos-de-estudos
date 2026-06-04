# programa para simular uma entrada em conta de banco, saque de dinheiro e conferencia de valor na conta

cadastro_completo = {}
saldo_do_usuario = 0.0

print('\n' + '=' * 50)
print('OLÁ, SEJA BEM VINDO(A) AO BANCO XYZ!')
print("Para entrar no aplicativo, basta entrar com seu login!")
print('\n' + '=' * 50)


def entrando_na_conta():  # entrar na conta, local de cadastro e de login.

    global cadastro_completo

    while True:
        print('\nCaso não tenha uma conta em nosso banco, basta escrever "cadastro" para se cadastrar')
        print('se já tem uma conta, basta escrever "login".')
        escolha = input('Qual opção deseja seguir? ') . strip().lower()
        print('\n' + '=' * 50)

        if escolha == 'cadastro':
            while True:

                novo_usuario = input(
                    "Informe um nome de usuário para o cadastro: ") .strip()
                if novo_usuario == '':
                    print(
                        "O login do usuário não pode está vazio. Por favor, informe um login válido.")
                    # para insistir até colocar um nome válido no cadastro.
                    continue

                elif novo_usuario in cadastro_completo:
                    print(
                        'já existe um usuário com esse nome, por insira um nome diferente.')
                # para ele colocar um nome de usuário que não esteja no cadastro do aplicativo.
                    continue
                break

            while True:
                nova_senha = input(
                    'Digite uma senha para ter acesso ao aplicativo. Essa senha deve conter no mínimo 6 caracteres.').strip()
                if len(nova_senha) < 6:
                    print(
                        "Número de caracteres inválido. Por favor, insira pelo menos 6 caracteres")

                    # para continuar insistindo até colocar uma senha válida pro cadastro.
                    continue
                print('Senha válida. Cadastro concluído!')
                cadastro_completo[novo_usuario] = nova_senha
                break  # finaliza o processo de cadastro.

        elif escolha == 'login':
            login_usuario = input(
                'Informe o seu nome de usuário: ') . strip()

            if login_usuario not in cadastro_completo:
                print(
                    'Nome de usuário não cadastrado no nosso banco de dados. Digite um nome de usuário válido.')
                continue  # continuar até colocar um nome que esteja dentro do banco de nomes de usuários cadastrados

            senha_usuario = input('Digite sua senha: ') .strip()

            # verificar senha e ver se tem no banco de dados

            if cadastro_completo[login_usuario] == senha_usuario:
                print('\n' + '=' * 50)
                print(f'LOGIN REALIZADO COM SUCESSO! BEM VINDO(A) ' + login_usuario)
                print('\n' + '=' * 50)
                return login_usuario
            else:
                print('Senha informada está incorreta. Tente novamente.')

        else:
            print('Volte ao menu de cadastro ou tente novamente logar na sua conta.')


def setor_financeiro(usuario):  # aqui onde ficará a parte de finanças

    global saldo_do_usuario

    while True:
        print('\n' + '=' * 50)
        print('SETOR DE FINANÇAS')
        print('\n' + '=' * 50)
        print(
            'Opções disponíveis no setor financeiro: [sacar] | [depositar] | [conferir] | [sair]')

        escolha = input('O que deseja fazer hoje ' + usuario + '??')

        if escolha == 'depositar':
            while True:
                try:
                    valor = float(
                        input('Para realizar o depósito, o valor.'))
                    if valor <= 0:
                        print(
                            "Por favor, insira um valor maior que zero para fazer o deposito.")
                        continue

                    saldo_do_usuario += valor  # para somar o valor do saldo
                    print(
                        f'valor depositado de R$ {valor:.2f} realizado com sucesso!')
                except ValueError:
                    print('POr favor, digite um número válido')
                    continue

                continuar = input(
                    "Deseja fazer um novo deposito? sim ou nao: ").lower().strip()
                if continuar != 'sim':
                    break

                # para sacar dinheiro

        elif escolha == 'sacar':
            while True:
                try:
                    valor = float(
                        input('Qual o valor do saque que o senhor(a) pretende fazer?'))
                    if valor <= 0:
                        print("Insira um valor maior do que zero para sacar.")
                        continue
                    if valor > saldo_do_usuario:
                        print(
                            f"saldo atual insufiente para essa ação! seu saldo atual é de R$ {saldo_do_usuario:.2f}")
                        break

                    saldo_do_usuario -= valor
                    print(f'Você sacou R$ {valor:.2f} com sucesso!')
                except ValueError:
                    print('Por favor, digite um número válido.')
                    continue
                continuar = input(
                    "O senhor(a) deseja fazer outro saco? sim ou nao: ").lower().strip()
                if continuar != 'sim':
                    break

        elif escolha == 'conferir':
            print(f'Certo, você atualmente possui: R$ {saldo_do_usuario:.2f}')

        elif escolha == 'sair':
            print("Obrigado por usar o Banco XYZ. Até logo!")
            break
        else:
            print('Escolha inválida. Escolha entre sacar, depositar, conferir ou sair.')


# Resumo e Execução do programa

usuario_logado = entrando_na_conta()
setor_financeiro(usuario_logado)
