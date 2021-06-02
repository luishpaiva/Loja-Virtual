#IMPORTAÇÕES DE OUTROS MÓDULOS
from datetime import datetime

#FUNÇÕES
#As variáveis incluídas no retorno das funções possuem um "_fun" ao final de seu nome para poder distingui-las das variáveis globais com mesmo nome.
#Etapa 4: 1 (1 de 2)
def obter_limite():
    #Etapa 1: 1
    nome_loja = 'Lojão do Luisão'
    meu_nome_completo_fun = 'Luís Henrique Paiva'
    print('====================================================================================================================================================')
    print('Olá, seja bem-vindo ao {0}. Meu nome é {1} e sou atendente da loja.'.format(nome_loja,meu_nome_completo_fun))

    #Etapa 1: 2
    print('Prezado cliente, para melhor atendê-lo, faremos agora uma análise de crédito para você, mas, para isso, precisaremos de alguns dados. Por gentileza:\n')
    while True:
        cargo = str(input("Informe o seu cargo: "))
        if all(x.isalpha() or x.isspace() for x in cargo) or '\'' in cargo:
            break
        else:
            print('O cargo informado contém caracteres especiais ou números. Por gentileza, utilize apenas letras, espaços e apóstrofo.\n')
            continue
    
    while True:
        try:
            salario = float(input('Informe o seu salário: R$ '))
        except ValueError:
            print ('O salário informado não está em formato numérico! Por gentileza, informe apenas números. Se precisar, utilize um ponto para separar as casas decimais.\n')
            continue
        else:
            break
        
    while True:
        try:
            ano_nascimento = int(input('Informe o ano de seu nascimento: '))
        except ValueError:
            print('O ano informado não está em formato numérico! Por gentileza, informe apenas números.\n')
            continue
        else:
            if ano_nascimento < 1900 or ano_nascimento >= (datetime.now().year):
                print('Ano inválido! Por gentileza, informe um ano igual ou posterior a 1900 e anterior ao ano corrente.\n')
                continue
            else:
                break

    #Etapa 1: 3
    print('\nO seu cargo é', cargo)
    print('O seu salário é R$ {:.2f}'.format(salario))
    print('O seu ano de nascimento é', ano_nascimento)

    #Etapa 2: 1
    idade_fun = int((datetime.now().year)-ano_nascimento)
    print('A sua idade aproximada é', idade_fun,'anos')

    #Etapa 2: 2
    limite_fun = (salario * (idade_fun/1000)) + 100
    print('----------------------------------------------------------------------------------------------------------------------------------------------------')
    print('Prezado cliente, o seu limite de gasto é R$ {:.2f}.'.format(limite_fun))

    #Etapa 4: 1 (2 de 2)
    return limite_fun, idade_fun, meu_nome_completo_fun

#Etapa 4: 2
def verificar_produto(limite):
    #Etapa 3: 1
    while True:
        try:
            #Etapa 4: 6 (2 de 2)
            while True:
                nome_produto_fun = input('Informe o nome de um produto: ')
                if all(y.isalpha() or y.isspace() or y.isnumeric for y in nome_produto_fun) or '\'' in nome_produto_fun:
                    try:
                        valor_produto_fun = float(input('Informe o valor desse produto: R$ '))
                    except ValueError:
                        print('O valor do produto informado não está em formato numérico! Por gentileza, informe apenas números. Se precisar, utilize um ponto para separar as casas decimais.\n')
                    else:
                        if valor_produto_fun > limite:
                            print('----------------------------------------------------------------------------------------------------------------------------------------------------')
                            print('\nO valor do produto informado excede o valor do limite disponível. Por gentileza, informe outro produto.')
                            print('Seu limite parcial é R$ {:.2f}.'.format(limite))
                            print('----------------------------------------------------------------------------------------------------------------------------------------------------')
                        else:
                            break
                else:
                    print('O produto informado contém caracteres especiais. Por gentileza, utilize apenas letras, espaços, apóstrofo e números.\n')
                    continue
            else:
                break
        except ValueError:
            print('O valor do produto informado não está em formato numérico! Por gentileza, informe apenas números. Se precisar, utilize um ponto para separar as casas decimais.')
            continue
        else:
            break

    #Etapa 3: 2
    if valor_produto_fun < (0.6*limite):
        print('\nLiberado!')
        qtde_vezes_fun = 1
    elif valor_produto_fun < (0.9*limite):
        print('\nLiberado para parcelar em até 2 vezes.')
        qtde_vezes_fun = 2
    elif valor_produto_fun < limite:
        print('\nLiberado para parcelar em 3 vezes ou mais.')
        while True:
            try:
                qtde_vezes_fun = int(input('\nEm quantas vezes pretende fazer o parcelamento do produto? '))
            except ValueError:
                print ('O salário informado não está em formato numérico! Por gentileza, informe apenas números.')
                continue
            else:
                if qtde_vezes_fun <= 3:
                    print('Para esse valor, a compra pode ser parcelada em 3 vezes ou mais! Por gentileza, informe um número igual ou maior a 3.\n')
                    continue
                else:
                    break
    else:
        print('\nBloqueado.')

    #Etapa 3: 3
    primeiro_nome_conta = float(len(meu_nome_completo.split(' ')[0]))
    if len(meu_nome_completo) < valor_produto_fun < idade:
        print('Seu desconto será de R$ {:.2f}.'.format(primeiro_nome_conta))
        #Etapa 3: 4
        print('O valor final do seu produto, já com o desconto, é R$ {:.2f}.'.format(valor_produto_fun-primeiro_nome_conta))
        valor_produto_fun = valor_produto_fun-primeiro_nome_conta
    else:
        print('Você não tem direito a desconto. O valor final do seu produto é R$ {:.2f}.'.format(valor_produto_fun))

    return valor_produto_fun, nome_produto_fun, qtde_vezes_fun

#RESTANTE DO PROGRAMA
#Etapa 4: 3
limite, idade, meu_nome_completo = obter_limite()

#Etapa 4: 4
while True:
    try:
        print('====================================================================================================================================================')
        contador = int(input('Por gentileza, informe quantos produtos deseja cadastrar: '))
        print('')
    except ValueError:
        print('O valor informado para a quantidade de itens não está em formato numérico! Por gentileza, informe apenas números.')
        continue
    else:
        if contador < 1:
            print('A quantidade inserida para a quantidade de itens foi menor que 1! Insira um número inteiro igual ou maior do que 1.')
            continue
        else:
            break

#Etapa 4: 5
valor_total = 0.00
nomes_total = []
valores_individuais = []
qtde_vezes_individuais = []
for i in range(contador, 0, -1):
    if valor_total >= limite:
        print('O limite de crédito foi alcançado. Não será possível adicionar mais produtos.\n')
        break
    else:
        #Etapa 4: 6 (1 de 2)
        valor_parcial, nome_produto, qtde_vezes = verificar_produto(limite-valor_total)
        valor_total += valor_parcial
        nomes_total.append(nome_produto)
        valores_individuais.append(valor_parcial)
        qtde_vezes_individuais.append(qtde_vezes)
    if i > 1:
        if limite-valor_total > 0:
            print('----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('Seu limite parcial é R$ {:.2f}.'.format(limite-valor_total))
            print('----------------------------------------------------------------------------------------------------------------------------------------------------')
    else:
        if limite-valor_total < 2.00:
            print('----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('Sobrou R$ {:.2f} do seu limite.'.format(limite-valor_total))
        else:
            print('----------------------------------------------------------------------------------------------------------------------------------------------------')
            print('Sobraram R$ {:.2f} do seu limite.'.format(limite-valor_total))

print('====================================================================================================================================================')
print('Sua sacola de produtos:')
print('+-------------------+--------------+----------+')
print('|      Produto      |     Valor    | Parcelas |')
print('+-------------------+--------------+----------+')
for i in range(len(nomes_total)):
    espacos1 = 16-len(nomes_total[i])
    espacos2 = 8-len('{:.2f}'.format(valores_individuais[i]))
    print('|',nomes_total[i], (' ' * espacos1),'| R$ {:.2f}'.format(valores_individuais[i]),(' ' * espacos2), '|    {}     |'.format(qtde_vezes_individuais[i]))
print('+-------------------+--------------+----------+')
print('\nValor final da compra e parcelamento máximo:')
print('+-------------------+--------------+----------+')
print('| TOTAL             | R$ {:.2f}    | {} vezes  |'.format(valor_total, max(qtde_vezes_individuais)))
print('+-------------------+--------------+----------+')
print('----------------------------------------------------------------------------------------------------------------------------------------------------')
print('Agradecemos a preferência e volte sempre!!!')
print('====================================================================================================================================================')