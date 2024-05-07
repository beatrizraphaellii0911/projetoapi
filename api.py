from flask import Blueprint

bp = Blueprint("api", __name__)

#Daqui pra baixo as rotas

@app.route("/", methods=("GET",))
def index():
    return jsonify({"status": 200, "message": "API da Beatriz Raphaelli de Oliveira Silva"})

@app.route("/aleatorios", methods=("GET",)) # decorator de rota
def aleatorios(): # função python
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a}) # retorno
