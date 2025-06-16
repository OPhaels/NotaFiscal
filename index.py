# Projeto principal - Nota Fiscal de Loja

from datetime import datetime

print('-------------- LOJA ---------------')
print('Preencha os dados e terá a Nota Fiscal\n')

compra = []            # Lista de dicionários com produtos
qnt_total = []         # Lista com quantidades de itens
valor_final = []       # Lista com os valores totais por item

funcionar = True
while funcionar:
    pessoa = dict()

    # --- Cadastro de Nome ---
    while True:
        print('-' * 35)
        nome = input('Nome: ').strip()

        if nome.replace(" ", "").isalpha():
            pessoa["nome"] = nome
            break
        else:
            print('Valor inválido!')

    while True:
        id = input('CPF (somente números): ')
        id_limpo = id.replace(".", "").replace("-", "").replace("/", "").replace(" ", "")

        if id_limpo.isdigit() and len(id_limpo) == 11:
            pessoa["cpf"] = id_limpo
            break
        else:
            print('-' * 35)
            print(' *** CPF inválido. Verifique os campos! ***')
            print('-' * 35)

    print('-' * 35)

    # --- Cadastro de Produto(s) ---
    while True:
        carrinho = dict()

        # Produto
        item = input('\nProduto: ').strip()
        if item.replace(" ", "").isalpha():
            carrinho["produto"] = item
        else:
            print('Entrada inválida! Verifique os campos.')
            continue

        # Quantidade
        while True:
            try:
                qnt = int(input('Quantidade: '))
                carrinho["quantidade"] = qnt
                qnt_total.append(qnt)
                break
            except ValueError:
                print('Valor inválido, verifique os campos!')

        # Valor unitário
        entrada = input('Valor: R$ ').strip()
        entrada_limpa = entrada.replace(",", ".").replace("-", "").replace(" ", "")

        try:
            valor = float(entrada_limpa)
            carrinho["valor"] = valor
            compra.append(carrinho)
        except ValueError:
            print('Erro! Tente novamente.')
            continue

        # Valor total por item (unitário * quantidade)
        valorSomado = valor * qnt
        valor_final.append(valorSomado)

        # Continuar adicionando produtos?
        decisao = input('\nDeseja inserir mais produtos? [S/N] ').strip().upper()
        if decisao and decisao[0] in ('S', 'N'):
            if decisao[0] == 'S':
                print('-' * 35)
                continue
            elif decisao[0] == 'N':
                print('\n------- Programa Finalizado -------\n')

                # Horário atual
                agora = datetime.now()
                data_hora = agora.strftime('%d/%m/%Y %H:%M:%S')
                print(f'Horário: {data_hora}\n')

                # Dados da Pessoa
                print(f'Nome: {pessoa["nome"]}')
                print(f'CPF: {pessoa["cpf"]}\n')

                # Dados da Compra
                print('         Dados da compra')
                print('-' * 35)
                print(f'{"Qnt":>5}  {"Produto":<14} {"Valor":>10}')
                print('-' * 35)

                for itens in compra:
                    nomeLimite = itens["produto"][:14]  # Limita nome do produto
                    print(f'{itens["quantidade"]:>5}  {nomeLimite:<14}  R${itens["valor"]:>7.2f}')

                print('\n' + '-' * 35)
                print(f'        Valor final: R$ {sum(valor_final):.2f}')
                print('-' * 35)

                funcionar = False
                break
        else:
            print('Erro! Entrada inválida.')
