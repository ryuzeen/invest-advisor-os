from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/recomendar", methods=["POST"])
def recomendar():
    dados = request.json

    perfil = dados.get("perfil", "conservador")
    objetivo = dados.get("objetivo", "curto prazo")

    if perfil == "conservador":
        carteira = ["Tesouro Selic", "CDBs de liquidez diária"]
    elif perfil == "moderado":
        carteira = ["Tesouro IPCA+", "Fundos Multimercado"]
    else:
        carteira = ["Ações de crescimento", "Criptoativos"]

    return jsonify({
        "perfil": perfil,
        "objetivo": objetivo,
        "carteira_recomendada": carteira,
        "explicacao": f"Carteira alinhada ao perfil {perfil} com foco em {objetivo}."
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
