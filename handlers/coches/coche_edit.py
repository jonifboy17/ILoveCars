# coding: utf-8
# Nuevo coche

import webapp2
import time
from webapp2_extras import jinja2
from model.coche import Coche

class CocheEditHandler(webapp2.RequestHandler):
    def get(self):

        coche = Coche.recupera(self.request)

        valores_plantilla = {
            "coche" : coche
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("coche_edit.html", **valores_plantilla))

    def post(self):

        id_coche = self.request.get("edIdCoche", "")

        coche = Coche.query(Coche.id_coche == id_coche).get()

        # Modificacion de algunos atributos
        coche.marca = self.request.get("edMarca", "").strip()
        coche.modelo = self.request.get("edModelo", "").strip()
        coche.carroceria = self.request.get("edCarroceria", "").strip()
        coche.anho = int(self.request.get("edAnho", ""))

        # Tratamientos foto
        if self.request.get("edFoto") != "":
            imagen = self.request.get("edFoto", None)
            coche.foto = imagen

        # Modifica el atributo id_coche
        id_coche = Coche.obtener_id_coche(coche.marca, coche.modelo, coche.carroceria, coche.anho)
        coche.id_coche = id_coche

        try:
            anho = int(coche.anho)
        except ValueError:
            anho = -1

        if (anho < 0 or not(coche.marca) or not(coche.modelo) or not(coche.carroceria)):
            return self.redirect("/coche_edit")
        else:

            # Almacena el objeto
            coche.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/coches/coche_edit', CocheEditHandler)
], debug=True)