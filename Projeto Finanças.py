import mysql.connector
from random import randint

def apresentacao():
    print('-=' * 15)
    print(f'{"     DEPÓSITO INVESTIMENTO"     }')
    print('-=' * 15)
    print('''    [1] - CRIPTOMOEDA 
    [2] - FIIS
    [3] - AÇÕES
    [4] - RENDA FIXA / CAIXA''')
    print('-=' * 15)


def escolha():

    #ESCOLHA DO INVESTIMENTO

    global sua_escolha
    opcoes = [1, 2, 3, 4, 5]
    while sua_escolha not in opcoes:
        print('\033[31mValor Inválido\033[m')
        sua_escolha = int(input('Qual o número de sua escolha? '))
    print('-=' * 15)


def criptomoeda():

    #PEDE AS INFORMAÇÕES DO USUÁRIO

    id_crip = randint(0, 9999)
    cripto = ['BITCOIN', 'ETHEREUM', 'DOGCOIN']
    print('Você escolheu Criptomoedas')
    print('Qual criptomoeda?')

    tipo_crip = str(input('Bitcoin | Ethereum | Dogcoin: ')).upper()
    if tipo_crip not in cripto:
        print('\033[31mEssa criptomoeda não está nos seus investimentos!\033[m')
        tipo_crip = str(input('Bitcoin | Ethereum | Dogcoin: ')).upper()

    valor_dep_crip = float(input('Qual o valor a depositar? R$'))
    print(f'O valor investido em {tipo_crip} foi R${valor_dep_crip}')
    print('-=' * 15)

    #INSERÇÃO NO BANCO DE DADOS

    sql_crip = "INSERT INTO criptomoeda (CHAVE, TIPO, VALOR_DEPOSITADO) VALUES (%s, %s, %s)"
    valores_crip = (id_crip, tipo_crip, valor_dep_crip)
    cursor.execute(sql_crip, valores_crip)
    conexao.commit()


def fiis():

    #PEDE AS INFORMAÇÕES DO USUÁRIO

    id_fii = randint(0, 9999)
    print('Você escolheu Fundos Imobiliários')
    cod_fii = str(input('Qual o código do FII? ')).upper()
    while len(cod_fii) < 6 or len(cod_fii) > 6:
        print('\033[31mCódigo inválido\033[m')
        cod_fii = str(input('Qual o código do FII? ')).upper()

    quantidade_fii = int(input('Qual a quantidade? ')) 
    valor_unidade_fii = float(input('Qual o valor por unidade? R$'))
    valor_tot_inv_fii = quantidade_fii * valor_unidade_fii

    print(f'O valor total investido em {cod_fii} foi R${valor_tot_inv_fii}')
    print('-=' * 15)

    #INSERÇÃO NO BANCO DE DADOS

    sql_fii = "INSERT INTO fiis (CHAVE, CODIGO, QUANTIDADE, PRECO_UNIDADE, VALOR_TOT_INV) VALUES (%s, %s, %s, %s, %s)"
    valores_fii = (id_fii, cod_fii, quantidade_fii, valor_unidade_fii, valor_tot_inv_fii)
    cursor.execute(sql_fii, valores_fii)
    conexao.commit()


def acoes():
    
    #PEDE AS INFORMAÇÕES DO USUÁRIO

    id_acao = randint(0, 9999)
    print('Você escolheu Ações')
    cod_acao = str(input('Qual o código da ação? ')).upper()
    while len(cod_acao) < 6 or len(cod_acao) > 6:
        print('\033[31mCódigo inválido\033[m')
        cod_acao = str(input('Qual o código da ação? ')).upper()
        
    quantidade_acao = int(input('Qual a quantidade? ')) 
    valor_unidade_acao = float(input('Qual o valor por unidade? R$'))
    valor_tot_inv_acao = quantidade_acao * valor_unidade_acao

    print(f'O valor total investido em {cod_acao} foi R${valor_tot_inv_acao}')
    print('-=' * 15)

    #INSERÇÃO NO BANCO DE DADOS

    sql_acao = "INSERT INTO acao (CHAVE, CODIGO, QUANTIDADE, PRECO_UNIDADE, VALOR_TOT_INV) VALUES (%s, %s, %s, %s, %s)"
    valores_acao = (id_acao, cod_acao, quantidade_acao, valor_unidade_acao, valor_tot_inv_acao)
    cursor.execute(sql_acao, valores_acao)
    conexao.commit()
    

def renda_fixa():

    #PEDE AS INFORMAÇÕES DO USUÁRIO

    id_rf = randint(0, 9999)
    print('Você escolheu Renda Fixa')
    tipo_rf = str(input('Qual o tipo? ')).upper()
    valor_rf = float(input('Qual o valor deseja depositar? R$'))
    valor_caixa = float(input('Qual valor deseja add para investimentos futuros? R$'))
    print(f'Valor investido em {tipo_rf} foi de {valor_rf}, e valor depositado em caixa foi RS{valor_caixa}')
    print('-=' * 15)

    #INSERÇÃO NO BANCO DE DADOS

    sql_rf = "INSERT INTO renda_fixa (CHAVE, TIPO, VALOR, VALOR_EM_CAIXA) VALUES (%s, %s, %s, %s)"
    valores_rf = (id_rf, tipo_rf, valor_rf, valor_caixa)
    cursor.execute(sql_rf, valores_rf)
    conexao.commit()


conexao = mysql.connector.connect(user='root', password='',
                                host='localhost',
                                database='investimentos')
cursor = conexao.cursor()

while True:
    apresentacao()
    sua_escolha = int(input('Qual o número de sua escolha? '))
    escolha()
    if sua_escolha == 1:
        criptomoeda()
    elif sua_escolha == 2:
        fiis()
    elif sua_escolha == 3:
        acoes()
    elif sua_escolha == 4:
        renda_fixa()

    continuar = str(input('Deseja escolher mais uma opção? [S/N] ')).upper()
    if continuar == 'N':
        print('\033[32mInvestimento concluido com sucesso!\033[m')
        print('-=' * 15)
        break
    else:
        continue