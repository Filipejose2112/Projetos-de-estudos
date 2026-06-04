
# Sistema de cadastro e de login, criado usando algumas das coisas que aprendi até esse momento
# basicamente, aqui você vai se cadastrar e entrar numa 'espécie' de rede social,
# com algumas opções de escolha, como abrir configuração, perfil e algumas escolhas dentro delas.

usuarios_cadastrados = {}

escolhas = [
    '1 - Acessar perfil',
    '2 - Acessar configurações',
    '3 - Sair do site'
]
escolhas_perfil = [
    '1 - Ver informações pessoais',
    '2 - Ver postagens',
    '3 - Ver atividades recentes',
    '4 - Voltar ao menu principal'
]
escolhas_configuracoes = [
    '1 - Alterar senha',
    '2 - Configurações de privacidade',
    '3 - Configurações de notificações',
    '4 - Voltar ao menu principal'
]

print('Olá, seja bem-vindo ao site')
print('Faça seu cadastro para acessar o site ou faça login se já tiver cadastro')


def cadastro_login():  # função de cadastro e de login

    global escolhas_perfil, escolhas_configuracoes, escolhas, usuarios_cadastrados, usuario_logado
    while True:
        opcao = input('\nDigite 1 para cadastro ou 2 para login: ')

        # Seção para fazer cadastro no site
        if opcao == '1':
            login_usuario = input(
                'Digite um nome de usuário para se cadastrar: ') .strip()
            if login_usuario == '':  # Caso o nome esteja vazio
                print('Login não pode ser vazio. Tente novamente.')
                continue

            elif login_usuario in usuarios_cadastrados:  # Caso o nome já existe no sistema
                print('Login já existe. Tente um login diferente.')
                continue

            while True:
                senha_usuario = input(
                    'Digite sua senha (mínimo 4 caracteres): ') .strip()
                if len(senha_usuario) < 4:
                    print('Senha muito curta. Tente novamente.')
                    # ficar insistindo até o usuário digitar uma senha válida
                    continue

                usuarios_cadastrados[login_usuario] = senha_usuario
                print('Cadastro realizado com sucesso! Agora faça o login.')
                break

        # Para fazer login no site
        elif opcao == '2':
            login_usuario = input('Digite seu login: ') .strip()

            if login_usuario == '':
                print('Login não pode ser vazio. Tente novamente.')
                continue  # Volta para o início do loop de login

            senha_usuario = input('Digite sua senha: ') .strip()

            if login_usuario in usuarios_cadastrados and usuarios_cadastrados[login_usuario] == senha_usuario:
                print("\n"+"="*50)
                print('Login realizado com sucesso!')
                print("olá senhor(a) " + login_usuario +
                      ", seja bem-vindo(a) ao site!")
                print("\n"+"="*50)
                usuario_logado = login_usuario
                break  # Agora o sistema entrará no menu principal
            else:
                print('Login ou senha incorretos. Tente novamente.')


# para acessar o menu principal, sendo configurações, perfil ou sair do site
def menu_principal():
    while True:
        print('\n--- MENU PRINCIPAL ---')
        print("\n"+"="*50)
        print('O que você gostaria de fazer?')
        for escolha in escolhas:
            print(escolha)

        opcao_usuario = input('Digite o número da opção desejada: ')

        # caso usuário queira acessar o perfil

        if opcao_usuario == '1':
            while True:  # Loop de perfil

                print("\n"+"="*50)
                print('\n--- PERFIL ---')
                print("\n"+"="*50)
                print(
                    'Aqui você pode ver suas informações pessoais, postagens e atividades.')
                for escolha in escolhas_perfil:
                    print(escolha)

                opcao_perfil = input('Digite a opção desejada: ')

                if opcao_perfil == '1':
                    print('\nExibindo informações pessoais...')
                    escolha_informacoes = ['1 - Nome',
                                           '2 - Email', '3 - Data de nascimento']
                    for escolha in escolha_informacoes:
                        print(escolha)
                    opcao_informacoes = input('Escolha o que deseja ver: ')
                    if opcao_informacoes == '1':
                        # Mostrar o nome do usuário logado caso ele queria ver o perfil
                        print(f'Exibindo nome...{usuario_logado}')
                    elif opcao_informacoes == '2':
                        print('Exibindo email...')
                    elif opcao_informacoes == '3':
                        print('Exibindo data de nascimento...')
                    else:
                        print('Opção inválida.')

                elif opcao_perfil == '2':
                    print('\nExibindo postagens...')
                    opcao_postagens = ['1 - Recentes',
                                       '2 - Mais curtidas', '3 - Mais comentadas']
                    for escolha in opcao_postagens:
                        print(escolha)
                    op_post = input('Escolha a opção: ')

                    print(f'Exibindo opção {op_post} de postagens...')

                elif opcao_perfil == '3':
                    print('\nExibindo atividades recentes...')
                    print(
                        'Você criou sua conta recentemente e não tem muitas atividades.')

                elif opcao_perfil == '4':
                    # Sai do loop do perfil e volta para o menu principal
                    break
                else:
                    print('Opção inválida.')

        # se quiser entrar nas configurações

        elif opcao_usuario == '2':
            while True:  # loop de configurações

                print("\n"+"="*50)
                print('\n--- CONFIGURAÇÕES ---')
                print("\n"+"="*50)
                for escolha in escolhas_configuracoes:
                    print(escolha)

                opcao_configuracoes = input('Digite a opção desejada: ')

                if opcao_configuracoes == '1':

                    while True:
                        # caso usuário resolva criar uma nova senha, aqui ficará salvo a nova senha
                        nova_senha = input('Digite sua nova senha: ')
                        if len(nova_senha) < 4:
                            print('Senha muito curta. Tente novamente.')
                            continue
                        else:
                            # para atualizar a senha do usuario no dicionário de usuários cadastrados
                            usuarios_cadastrados[usuario_logado] = nova_senha
                            print(
                                f'Senha alterada com sucesso!')
                            break

                elif opcao_configuracoes == '2':
                    print('Configurando preferências de privacidade...')
                elif opcao_configuracoes == '3':
                    print('Configurando notificações...')
                elif opcao_configuracoes == '4':
                    # Sai do loop de configurações e volta para o menu principal
                    break
                else:
                    print('Opção inválida.')

        # se quiser sair do site.
        elif opcao_usuario == '3':

            print("\n"+"="*50)
            print("Saindo do site. Até logo senhor(a) " + usuario_logado+"!")
            print("\n"+"="*50)
            break  # para finalizar o programa e sair do loop principal
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

# finalização


cadastro_login()
menu_principal()
