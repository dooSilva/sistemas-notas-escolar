import msvcrt
####################################################
#FUNÇÃO PARA  ESCONDER OS CARACTERES  DA SENHA  
def input_senha(prompt=''):
    print(prompt, end='', flush=True)
    senha = ''
    while True:
        tecla = msvcrt.getwch()
        if tecla == '\r':
            print()
            break
        elif tecla == '\b':
            if senha:
                senha = senha[:-1]
                print('\b \b', end='', flush=True)
        else:
            senha += tecla
            print('*', end='', flush=True)
    return senha
#FUNÇÃO PARA  ESCONDER OS CARACTERES  DA SENHA
####################################################


####################################################
#FUNÇÃO PARA OS CARACTERES DO LOGIN E DO NOME DO ALUNO SEREM MAÍUSCULOS
def input_maiusculo(prompt=''):
    print(prompt, end='', flush=True)
    texto = ''
    while True:
        tecla = msvcrt.getwch()
        if tecla == '\r':  # Enter
            print()
            break
        elif tecla == '\b':  # Backspace
            if texto:
                texto = texto[:-1]
                print('\b \b', end='', flush=True)
        else:
            letra = tecla.upper()
            texto += letra
            print(letra, end='', flush=True)
    return texto
#FUNÇÃO CARACTERES MAIUSCULOS
#########################################################


#########################################################
#FUNÇÃO DE APROVAR O ALUNO
def sistemaNota():
    # Código principal
    nome = input_maiusculo("Digite o nome do aluno: ")

    matematica = float(input("Digite a nota de Matemática: "))
    portugues = float(input("Digite a nota de Português: "))
    ciencias = float(input("Digite a nota de Ciências: "))
    historia = float(input("Digite a nota de História: "))
    ingles = float(input("Digite a nota de Inglês: "))
    input("Pressione ENTER para finalizar.....")

    calculo = matematica + portugues + ingles + historia + ciencias


    if calculo >= 350:
        print(f"{nome} APROVADO")
    elif 250 <= calculo < 350:
        print(f"{nome} EM RECUPERAÇÃO")
    else:
        print(f"{nome} REPROVADO")
#FUNÇÃO DE APROVAR O ALUNO
##############################################################

#FUNÇÃO E AUTENTICAÇÃO
#################################################################
def autenticacao(login, senha):
    log = "ADMIN"
    passd = "1234"

    if login == log and senha == passd:
        print("Bem vindo")
        sistemaNota()
    else:
        print("Falha de autenticação")
        return False

def tentar_login(max_tentativas=3):
    for tentativa in range(max_tentativas):
        login = input_maiusculo("Digite seu nome de usuário: ")
        senha = input_senha("Digite sua senha: ")
        if autenticacao(login, senha):
            return True
        else:
            print(f"Tentativa {tentativa + 1} de {max_tentativas}\n")
    print("Limite excedido de tentativas.")
    return False
        

tentar_login()
###################################################################