# coding: utf-8
# Registra un nuevo coche

import webapp2
import time

from webapp2_extras import jinja2
from model.coche import Coche
from webapp2_extras.users import users

class CocheAddHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        valores_plantilla = {
            "usr" : usr
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(jinja.render_template("coche_add.html", **valores_plantilla))

    def post(self):

        marca = self.request.get("edMarca", "")
        modelo = self.request.get("edModelo", "")
        carroceria = self.request.get("edCarroceria", "")
        anho = int(self.request.get("edAnho", ""))
        id_coche = self.request.get("edIdCoche", "")

        # Tratamientos foto
        imagen = None
        if self.request.get("edFoto") != "":
            imagen = self.request.get("edFoto", None)

        # Forma la nueva id_coche con los otros campos introducidos
        id_Coche = Coche.obtener_id_coche(marca, modelo, carroceria, anho)

        try:
            anho = int(anho)
        except ValueError:
            anho = -1

        if anho < 0 or not(marca) or not(modelo) or not(carroceria) or not(id_Coche):
            return self.redirect("/coche_add")
        else:
            coche = Coche(marca=marca, modelo=modelo, carroceria=carroceria, anho=anho, foto=imagen, id_coche=id_Coche)
            coche.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/coches/coche_add', CocheAddHandler)
], debug=True)