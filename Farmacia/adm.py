import mysql.connector

meubanco = mysql.connector.connect(host="localhost",
                                   database="farm",
                                   user="root",
                                   password="labhugo")

cursor = meubanco.cursor(dictionary=True)

while True:
    print("----------- Area Administrativa -----------")
    print('[1] Fornecedores')
    print('[2] Produtos')
    print('[3] Funcionários')
    print('[4] Relatórios')
    print('[5] Encerrar')
    opcao = int(input('?'))

    if opcao == 1:
        print("----------- Fornecedores -----------")
        print('[1] Cadastrar')
        print('[2] Alterar')
        print('[3] Voltar')
        opcao1 = int(input('?'))
        if opcao1 == 1:
            cnp = input("Cnpj: ")
            nom = input("Nome: ")
            con = input("Contato: ")
            cep = input("CEP: ")
            est = input("Estado: ")
            rua = input("Rua: ")
            cid = input("Cidade: ")
            bai = input("Bairro: ")
            num = input("Número: ")

            cursor.execute(f"INSERT INTO fornecedor VALUES ('{cnp}', '{nom}', '{cep}', '{est}', '{rua}', '{cid}', '{bai}', '{num}')")
            cursor.execute(f"INSERT INTO contato_fornecedor VALUES ('{con}', '{cnp}')")
            meubanco.commit()
            print('>>> Empresa cadastrada com sucesso!\n')

        elif opcao1 == 2:
            forn = input('Cnpj: ')
            alter = input('Alteração: ')
            val = input('Novo Valor: ')

            cursor.execute(f"UPDATE fornecedor SET {alter} = '{val}' WHERE cnpj = '{forn}'")
            meubanco.commit()
            print('>>> Informação alterada com sucesso!\n')

        elif opcao1 == 3:
            print('Voltando...\n')
    if opcao == 2:
        print("----------- Produtos -----------")
        print('[1] Cadastrar')
        print('[2] Alterar')
        print('[3] Voltar.')
        opcao1 = int(input('?'))
        if opcao1 == 1:
            cod = input("Código: ")
            nom = input("Nome: ")
            qua = input("Quantidade: ")
            valo = input("Valor: ")
            vali = input("Validade: ")
            rec = input("Receita: ")
            cat = input("Categoria: ")

            cursor.execute(f"INSERT INTO produtos(cod, nome, quantidade, valor, validade, receita, categoria) VALUES ('{cod}', '{nom}', '{qua}', '{valo}', '{vali}', '{rec}', '{cat}')")
            meubanco.commit()
            print('>>> Produto cadastrado com sucesso!\n')

        elif opcao1 == 2:
            forn = input('Código: ')
            alter = input('Alteração: ')
            val = input('Novo Valor: ')

            cursor.execute(f"UPDATE produtos SET {alter} = '{val}' WHERE cod = '{forn}'")
            meubanco.commit()
            print('>>> Informação alterada com sucesso!\n')

        elif opcao1 == 3:
            print('Voltando...\n')
    if opcao == 3:
        print("----------- Funcionários -----------")
        print('[1] Cadastrar')
        print('[2] Alterar')
        print('[3] Voltar.')
        opcao1 = int(input('?'))
        if opcao1 == 1:
            cpf = input("CPF: ")
            nom = input("Nome: ")
            con = input("Contato: ")
            fun = input("Função: ")
            sal = input("Salário: ")
            rua = input("Rua: ")
            cid = input("Cidade: ")
            est = input("Estado: ")
            bai = input("Bairro: ")
            num = input("Número: ")

            cursor.execute(f"INSERT INTO funcionario VALUES ('{cpf}', '{nom}', '{fun}', '{sal}', '{rua}', '{cid}', '{est}', '{bai}', '{num}')")
            cursor.execute(f"INSERT INTO contato_funcionario VALUES ('{con}', '{cpf}')")
            meubanco.commit()
            print('>>> Funcionário cadastrado com sucesso!\n')

        elif opcao1 == 2:
            forn = input('CPF: ')
            alter = input('Alterar: ')
            val = input('Novo Valor: ')

            cursor.execute(f"UPDATE funcionario SET {alter} = '{val}' WHERE cpf = '{forn}'")
            meubanco.commit()
            print('>>> Informação alterada com sucesso!\n')

        elif opcao1 == 3:
            print('Voltando...\n')
    if opcao == 4:
        print("----------- Relatórios -----------")
        print('[1] Estoque de Produtos.')
        print('[2] Lista de Funcionários.')
        print('[3] Lista de Clientes.')
        print('[4] Voltar.')
        opcao1 = int(input('?'))
        if opcao1 == 1:
            cursor.execute("SELECT nome, quantidade FROM produtos ORDER BY quantidade ASC;")
            for linha in cursor:
                nome = linha["nome"]
                quant = linha["quantidade"]
                print(f"| {nome} | {quant} |\n")

        elif opcao1 == 2:
            cursor.execute("SELECT nome, cpf FROM funcionario ORDER BY nome ASC")
            for linha in cursor:
                nome = linha["nome"]
                cpf = linha["cpf"]
                print(f"| {nome} | {cpf} |\n")

        elif opcao1 == 3:
            cursor.execute("SELECT cliente.nome, cliente.cpf, compra.valor FROM cliente, compra WHERE compra.cpf_cliente = cliente.cpf ORDER BY cliente.nome ASC")
            for linha in cursor:
                nome = linha["nome"]
                cpf = linha["cpf"]
                valor = linha["valor"]
                print(f"| {nome} | {cpf} | {valor} |\n")
        elif opcao1 == 4:
            print('Voltando...\n')
    elif opcao == 5:
        print('Encerrando...\n')
        break