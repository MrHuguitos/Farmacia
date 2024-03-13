import mysql.connector

meubanco = mysql.connector.connect(host="localhost",
                                   database="farm",
                                   user="root",
                                   password="labhugo")

cursor = meubanco.cursor(dictionary=True)

func = input('Qual seu CPF? ')
cursor.execute("SELECT cpf, nome FROM funcionario WHERE cpf = %s;", (func,))
linha = cursor.fetchone()
print(linha)

if linha is not None: 
    nome = linha.get('nome')
    print(f'Bem vindo, {nome}!')   
    while True:
        print("----------- Caixa -----------")
        print('[1] Clientes')
        print('[2] Caixa')
        print('[3] Relatórios')
        print('[4] Encerrar')
        opcao = int(input('?'))

        if opcao == 1:
            print("----------- Clientes -----------")
            print('[1] Cadastrar')
            print('[2] Alterar')
            print('[3] Voltar')
            opcao1 = int(input('?'))
            if opcao1 == 1:
                cpf = input("CPF: ")
                nom = input("Nome: ")
                con = input("Contato: ")
                rua = input("Rua: ")
                est = input("Estado: ")
                cid = input("Cidade: ")
                bai = input("Bairro: ")
                num = input("Número: ")

                cursor.execute(f"INSERT INTO cliente VALUES ('{cpf}', '{nom}', '{rua}', '{est}', '{cid}', '{bai}', '{num}')")
                cursor.execute(f"INSERT INTO contato_cliente VALUES ('{con}', '{cpf}')")
                meubanco.commit()
                print('>>> Cliente cadastrado com sucesso!\n')
            elif opcao1 == 2:
                forn = input('CPF: ')
                alter = input('Alteração: ')
                val = input('Novo Valor: ')

                cursor.execute(f"UPDATE cliente SET {alter} = '{val}' WHERE cpf = '{forn}'")
                meubanco.commit()
                print('>>> Informação alterada com sucesso!\n')

            elif opcao1 == 3:
                print('Voltando...\n')
        if opcao == 2:
            print("----------- Caixa -----------")
            cpf = input("CPF do Cliente: ")
            cod = input("Código do Produto: ")
            dat = input("Data: ")
            qua = int(input("Quantidade: "))

            cursor.execute(f"INSERT INTO compra VALUES ('{dat}', '{qua}', '{cod}', '{cpf}')")
            cursor.execute(f"INSERT INTO vende VALUES ('{cod}', '{func}')")
            cursor.execute(f"UPDATE produtos SET quantidade = (produtos.quantidade) - {qua} WHERE cod = {cod}")
            cursor.execute(f"UPDATE compra, produtos SET compra.valor = (produtos.valor) * {qua} WHERE compra.cod_produtos = produtos.cod AND compra.cod_produtos= {cod}")
            meubanco.commit()
            print('>>> Compra realizada com sucesso!\n') #A compra será realizada apenas se o cpf do funcionário adicionado no inicio do programa for realmente igual aos cpfs presentes na tabela 'Funcionario'.
        if opcao == 3:
            print("----------- Relatórios -----------")
            print('[1] Fechamento do Dia')
            print('[2] Fechamento do Mês')
            print('[3] Vendas do Funcionário')
            print('[4] Voltar')
            opcao1 = int(input('?'))
            if opcao1 == 1:
                data = input("Data(Ano, Mês e Dia): ")
                cursor.execute(f"SELECT compra.data, compra.valor as Valor_Total, produtos.valor as Valor_Produto, produtos.nome as Produto, cliente.nome as Cliente, funcionario.nome as Funcionario FROM compra, produtos, cliente, funcionario, vende WHERE compra.cod_produtos = produtos.cod AND compra.cpf_cliente = cliente.cpf AND vende.cpf_funcionario = funcionario.cpf AND vende.cod_produtos = produtos.cod AND compra.data = '{data}' ORDER BY Produto ASC")
                for linha in cursor:
                    data = linha["data"]
                    valort = linha["Valor_Total"]
                    produto = linha["Produto"]
                    valorp = linha["Valor_Produto"]
                    cliente = linha["Cliente"]
                    funcionario = linha["Funcionario"]
                    print(f"| {data} | {valort} | {produto} | {valorp} | {cliente} | {funcionario} |\n")
            elif opcao1 == 2:
                data = input('Data(Ano e Mês): ')
                cursor.execute(f"SELECT compra.data, compra.valor as Valor_Total, produtos.valor as Valor_Produto, produtos.nome as Produto, cliente.nome as Cliente, funcionario.nome as Funcionario FROM compra, produtos, cliente, funcionario, vende WHERE compra.cod_produtos = produtos.cod AND compra.cpf_cliente = cliente.cpf AND vende.cpf_funcionario = funcionario.cpf AND vende.cod_produtos = produtos.cod AND compra.data BETWEEN '{data}-01' AND '{data}-28'")
                for linha in cursor:
                    data = linha["data"]
                    valort = linha["Valor_Total"]
                    produto = linha["Produto"]
                    valorp = linha["Valor_Produto"]
                    cliente = linha["Cliente"]
                    funcionario = linha["Funcionario"]
                    print(f"| {data} | {valort} | {produto} | {valorp} | {cliente} | {funcionario} |\n")
            elif opcao1 == 3:
                cp = input('CPF do Funcionario: ')
                cursor.execute(f"SELECT funcionario.nome as Funcionario, produtos.nome as Produto FROM funcionario, vende, produtos WHERE vende.cod_produtos = produtos.cod AND vende.cpf_funcionario = funcionario.cpf AND funcionario.cpf = '{cp}' ORDER BY produtos.nome ASC")
                for linha in cursor:
                    funcio = linha["Funcionario"]
                    prod = linha["Produto"]
                    print(f"| {funcio} | {prod} |\n")
            elif opcao1 == 4:
                print('Voltando...\n')
        elif opcao == 4:
            print('Encerrando...\n')
            break
else:
    print('Funcionário não cadastrado. Tente novamente')