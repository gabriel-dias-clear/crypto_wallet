from flask import Flask

app = Flask(__name__)

class MinhaClasseDeRotas:
    def __init__(self, app):
        self.app = app

        self.registrar_rotas()

    def registrar_rotas(self):
        self.app.add_url_rule('/', 'index', self.index)
        self.app.add_url_rule('/pagina1', 'pagina1', self.pagina1)
        self.app.add_url_rule('/pagina2', 'pagina2', self.pagina2)

    def index(self):
        return "Página Inicial"

    def pagina1(self):
        return "Página 1"

    def pagina2(self):
        return "Página 2"

minhas_rotas = MinhaClasseDeRotas(app)

if __name__ == '__main__':
    app.run(debug=True)
