from flask import render_template, jsonify
from random import choice
from app1.pokeneas import pokeneas
from app1.utils import generar_url_firmada, get_contenedor_id

def configure_routes(app):

    @app.route("/pokenea/json")
    def pokenea_json():
        p = choice(pokeneas)
        return jsonify({
            "id": p["id"],
            "nombre": p["nombre"],
            "altura": p["altura"],
            "habilidad": p["habilidad"],
            "contenedor_id": get_contenedor_id()
        })

    @app.route("/pokenea/frase")
    def mostrar_pokenea():
        p = choice(pokeneas)
        url_firmada = generar_url_firmada(p["imagen"])
        contenedor_id = get_contenedor_id()
        return render_template("frase.html", nombre=p["nombre"], imagen=url_firmada,
                               frase=p["frase"], contenedor_id=contenedor_id)

