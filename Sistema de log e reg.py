import sqlite3

banco = sqlite3.connect('banco_de_dados.db') #cria banco de dados#
cursor = banco.cursor() #conecta o cursor

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(nome text, cpf text, senha text)") ##Cria tabela "usuarios" se não existir##

#
class Usuario:
    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha

def lin():
    print('-=' * 10)

def menu():

    ##Função de Registro##
    def registro():
        lin()
        print('Registro')
        lin()
        nome = str(input('Seu nome:')).title()
        cpf = str(input('CPF:'))

        ##Tratamento de erro de cpf##
        while len(cpf) != 11:
            print('Digite um cpf válido!')
            cpf = str(input('CPF:'))
        cursor.execute("SELECT * FROM usuarios")
        usuarios = [usuario for usuario in cursor.fetchall()]
        cpfs = []
        for usuario in usuarios:
            cpfs.append(usuario[1])
        while cpf in cpfs:
            print('CPF Já utilizado!')
            cpf = str(input('CPF:'))
            while len(cpf) != 11:
                print('Digite um cpf válido!')
                cpf = str(input('CPF:'))

        senha = str(input('Senha:'))

        ##Tratamento de erro de senha##
        while len(senha) < 6 or senha.isnumeric() == False:
            lin()
            print('Erro!')
            lin()
            print('Sua deve deve conter pelo menos 6 caracteres!')
            print('Todos os caracteres devem ser números!')
            lin()
            senha = str(input('Senha:'))

        confirm = str(input('Confirmar senha:'))

        ##Tratamento de erro de confirmação de senha##
        while senha != confirm:
            print('Senhas não batem')
            senha = str(input('Senha:'))
            while len(senha) < 6 or senha.isnumeric() == False:
                lin()
                print('Erro!')
                lin()
                print('Sua deve deve conter pelo menos 6 caracteres!')
                print('Todos os caracteres devem ser números!')
                lin()
                senha = str(input('Senha:'))

            confirm = str(input('Confirmar senha:'))

        novo_usuario = Usuario(nome, cpf, senha)

        ##Cadastra o usuário no banco de dados##
        cursor.execute("INSERT INTO usuarios VALUES('"+novo_usuario.nome+"', '"+novo_usuario.cpf+"', '"+novo_usuario.senha+"')")
        banco.commit()
        print('Cadastrado com sucesso!')

    ##Função de login##
    def login():

        acesso = None

        ##Função quando usuário loga na conta##
        def logou():
            print(f'Olá {conta_logada[0]}')

        lin()
        print('Login')
        lin()
        cpf = str(input('CPF:'))
        senha = str(input('Senha:'))

        ##Verificação de integridade CPF/senha##
        cursor.execute("SELECT * FROM usuarios")
        for usuario in cursor.fetchall():
            if usuario[1] == cpf and usuario[2] == senha:
                acesso = True
                conta_logada = usuario
                break
            else:
                acesso = False

        if acesso == True:
            print('Logado com sucesso!')
            logou()
        else:
            print('CPF ou senha inválidos!')


    lin()
    print('[1] Logar')
    print('[2] Registrar')
    lin()

    while True:
        try:
            escolha = int(input('>>>>>>>>>>>>>>'))

        ##Tratamento de erro##
            while escolha not in (1, 2):
                print('Opção inválida!')
            break
        except ValueError:
            print('Opção inválida!')

    if escolha == 1:
        login()

    if escolha == 2:
        registro()

while True:
    menu()