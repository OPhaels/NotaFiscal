# import copy, time
# jogadores = list()
# Keep = True
# print('-' * 35)
# while Keep:
#     jogador = dict()
#     gols = list()
#     jogador["nome"] = str(input('Nome: '))
#     while True:
#         try:
#             qnt_gols = int(input(f'Quantos gols {jogador["nome"]} conseguiu fazer: '))
#             break
#         except ValueError:
#             print('Valor inválido! Verifique os campos.')
# 
#     for u in range(1, qnt_gols + 1):
#         while True:
#             try:
#                 gol = int(input(f'\tQuantos gols na partida {u}? -> '))
#                 gols.append(gol)
#                 break
#             except ValueError:
#                 print('Valor inválido! Digite um número inteiro.')
# 
#     print('')
#     jogador["gols"] = gols
#     jogadores.append(copy.deepcopy(jogador))
# 
#     while True:
#         decisao = str(input('Deseja inserir mais usuários? [S/N] -> ')).upper()[0]
#         if decisao in ['S', 'N']:
#             if decisao == 'S':
#                 print('-' * 35)
#                 break
#             else:
#                 print('\n' + '-' * 40)
#                 print('      RELATÓRIO FINAL DOS JOGADORES')
#                 print('-' * 40 + '\n')
#                 for jogador in jogadores:
#                     time.sleep(1)
#                     print(f'Nome: {jogador["nome"]}')
#                     for i, gol in enumerate(jogador["gols"]):
#                         time.sleep(1)
#                         print(f'\tPartida {i+1}: {gol} gols.')
#                     print('-' * 35)
#                 Keep = False
#                 break
#         else:
#             print('Valor inválido! Digite apenas S ou N.')



## Projeto principal

nf = list()
funcionar = True
while funcionar:
    pessoa = dict()
    while True:
        nome = input('Nome: ').strip()

        if nome.replace(" ", "").isalpha():
            pessoa["nome"] = nome
            break
        else:
            print('Valor inválido!')
    while True:
        id = input('CPF ou CNPJ: ')
        
        id_limpo = id.replace(".", "").replace('-', "").replace("/", "").replace(" ", "")
        
        if id_limpo.replace(".", "").isalnum:
            if len(id) == 11:
                pessoa["cpf"] = id_limpo
                break
            elif len(id) == 14:
                pessoa["cnpj"] = id_limpo
                break
            else:
                print('CPF ou CNPJ inválido. Verifique os campos!')
    while True:
        carrinho = dict()
        
        item = input('Produto: ')
        if item.replace(" ", "").isalpha():
            carrinho["produto"] = item
        else:
            print('Entrada inválida! Verifique os campos')
            continue
        
        try:
            qnt = int(input('Quantidade: '))
            carrinho["quantidade"] = qnt
        except ValueError:
            print('Valor inválido, verifique os campos!')
            continue
        
        
        entrada = input('Valor R$ ').strip()
            
        # remove vírgulas, pontos e traços
        entrada_limpa = entrada.replace(",",".").replace("-", "").replace(" ", "")
            
        try:
            valor = float(entrada_limpa)
            carrinho["valor"] = valor
        except ValueError:
            print('Erro! Tente novamente')
            continue
        
        valor_final = valor * qnt #  valor * quantidade 
        
        
        decisao = str(input('Deseja inserir mais produtos? ')).upper()[0]
        if decisao in ('S', 'N'):
            if decisao == 'S':
                print('Ok!')
            elif decisao == 'N':
                print('------- Programa Finalizado -------')
                print(valor_final)
                print(f'Dados do comprador: {pessoa}')
                print(f'Quantidade de itens: {qnt}')
                print(f'Itens: {carrinho}')
                funcionar = False
                break
            else:
                print('Erro!', 'Entrada inválida')
        
    