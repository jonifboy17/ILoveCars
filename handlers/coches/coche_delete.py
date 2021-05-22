# coding: utf-8
# Elimina coche registrado

import webapp2
import time
from model.coche import Coche

class CocheDeleteHandler(webapp2.RequestHandler):

    def get(self):
        coche = Coche.recupera(self.request)
        coche.key.delete()
        time.sleep(1)
        return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/coches/coche_delete', CocheDeleteHandler)
], debug=True)