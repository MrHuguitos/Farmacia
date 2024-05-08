from flask import Flask, render_template, request
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "labhugo",
    database = "farmdigital"
)
cursor = banco.cursor()

app = Flask(__name__)

@app.route('/principal') #Página de opções do usuário
def principal():
    return render_template("Administração.html")

@app.route('/inserir', methods=['GET', 'POST']) #Página onde o usuário pode inserir um produto
def inserir():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']
        quantidade = request.form['quant']
        valor = request.form['valor']
        categoria = request.form['categoria']
        foto = request.files['imagem']

        imagem = foto.read() #Converter a imagem em binário

        cursor.execute(f"SELECT * FROM produtos WHERE cod = {codigo};")
        linha = cursor.fetchone()

        if linha is not None: #Caso o produto já exista
            return render_template("Administração.html", mensagem = "O produto não pode ser cadastrado, pois já existe!")
        else: 
            cursor.execute(f"INSERT INTO produtos VALUES (%s, %s, %s, %s, %s, %s);", (codigo, nome, quantidade, valor, categoria, imagem))
            banco.commit()
            return render_template("Administração.html", mensagem = "Produto Cadastrado com Sucesso!")
    else:
        return render_template("Add_produtos.html")
    
@app.route('/deletar', methods=['GET', 'POST']) #Página onde o usuário pode inserir um produto
def deletar():
    if request.method == 'POST':
        codigo = request.form['codigo']

        cursor.execute(f"SELECT * FROM produtos WHERE cod = {codigo};")
        linha = cursor.fetchone()

        if linha is not None: #Caso o produto exista
            cursor.execute(f"DELETE FROM produtos WHERE cod = {codigo};")
            banco.commit()
            return render_template("Administração.html", mensagem = "Produto Deletado com Sucesso!")
        else: 
            return render_template("Administração.html", mensagem = "O produto não pode ser deletado, pois não existe!")
    else:
        return render_template("Del_produtos.html")

@app.route('/editor') #Página de edição do produto
def editor():
    return render_template("Edit_produtos.html")

#--------------------------- Quantidade de produtos ---------------------------------
 
@app.route('/editor/quantidade') #Página de edição do produto
def editor_quant():
    return render_template("Edit_quant.html")

@app.route('/editor/quantidade/adicionar', methods=['GET', 'POST']) #Página de edição do produto
def editor_quant_add():
    if request.method == 'POST':
        codigo = request.form['codigo']
        quantidade = request.form['quant']

        cursor.execute(f"SELECT quantidade FROM produtos WHERE cod = {codigo};")
        linha = cursor.fetchone()

        if linha is not None: #Caso o produto exista
            total = linha[0] + int(quantidade)
            cursor.execute(f"UPDATE produtos SET quantidade = {total} WHERE cod = {codigo};")
            banco.commit()
            return render_template("Administração.html", mensagem = "Produto Alterado com Sucesso!")
        else: 
            return render_template("Administração.html", mensagem = "O produto não pode ser alterado, pois não existe!")
    else:
        return render_template("Edit_quant_add.html")

@app.route('/editor/quantidade/remover', methods=['GET', 'POST']) #Página de edição do produto
def editor_quant_del():
    if request.method == 'POST':
        codigo = request.form['codigo']
        quantidade = request.form['quant']

        cursor.execute(f"SELECT quantidade FROM produtos WHERE cod = {codigo};")
        linha = cursor.fetchone()

        if linha is not None: #Caso o produto exista
            total = linha[0] - int(quantidade)
            if total < 0:
                return render_template("Administração.html", mensagem = "Operação Inválida!")
            else:
                cursor.execute(f"UPDATE produtos SET quantidade = {total} WHERE cod = {codigo};")
                banco.commit()
                return render_template("Administração.html", mensagem = "Produto Alterado com Sucesso!")
        else: 
            return render_template("Administração.html", mensagem = "O produto não pode ser alterado, pois não existe!")
    else:
        return render_template("Edit_quant_del.html")
    
#--------------------------- Valor do produtos ---------------------------------    
    
@app.route('/editor/valor', methods=['GET', 'POST']) #Página de edição do produto
def editor_valor():
    if request.method == 'POST':
        codigo = request.form['codigo']
        valor = request.form['valor']

        cursor.execute(f"SELECT quantidade FROM produtos WHERE cod = {codigo};")
        linha = cursor.fetchone()

        if linha is not None: #Caso o produto exista
            cursor.execute(f"UPDATE produtos SET valor = {valor} WHERE cod = {codigo};")
            banco.commit()
            return render_template("Administração.html", mensagem = "Produto Alterado com Sucesso!")
        else: 
            return render_template("Administração.html", mensagem = "O produto não pode ser alterado, pois não existe!")
    else:
        return render_template("Edit_valor.html")
    
#--------------------------- Nome do produtos ---------------------------------  
    
@app.route('/editor/nome', methods=['GET', 'POST']) #Página de edição do produto
def editor_nome():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nome = request.form['nome']

        cursor.execute(f"SELECT quantidade FROM produtos WHERE cod = {codigo};")
        linha = cursor.fetchone()

        if linha is not None: #Caso o produto exista
            cursor.execute(f"UPDATE produtos SET nome = '{nome}' WHERE cod = {codigo};")
            banco.commit()
            return render_template("Administração.html", mensagem = "Produto Alterado com Sucesso!")
        else: 
            return render_template("Administração.html", mensagem = "O produto não pode ser alterado, pois não existe!")
    else:
        return render_template("Edit_nome.html")

@app.route('/promocoes') #Página de criação, edição e fechamento de promoções
def promocoes():
    return render_template("Promocoes.html")

if __name__ == "__main__":
    app.run(debug=True)