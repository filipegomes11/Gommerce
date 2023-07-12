from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def page_home():
    return render_template('home.html')



@app.route('/produtos')
def page_produtos():
    itens = [
        {'id': 1, 'nome': 'Camiseta', 'cod_barra': '23515630', 'preco': 50},
        {'id': 2, 'nome': 'Xbox', 'cod_barra': '231415531', 'preco': 12200},
        {'id': 3, 'nome': 'TV usada', 'cod_barra': '635434', 'preco': 523},
        ]
    return render_template('produtos.html', itens=itens)


    






 

