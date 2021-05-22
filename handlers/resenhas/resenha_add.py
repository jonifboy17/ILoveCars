# coding: utf-8

# Nueva reseña

import webapp2
import time

from webapp2_extras import jinja2

from webapp2_extras.users import users

from google.appengine.ext import ndb

from model.resenha import Resenha

class ResenhaAddHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
            "clave_coche": self.request.GET["car"]
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(jinja.render_template("resenha_add.html", **valores_plantilla))

    def post(self):
        usr = users.get_current_user()

        email = self.request.get("edEmail ", "")
        opinion = self.request.get("edOpinion", "")
        clave_coche = self.request.GET["car"]

        if (not(opinion)):
            return self.redirect("/resenha_add")
        else:
            resenha = Resenha(email=usr.email(), opinion=opinion, clave_coche=ndb.Key(urlsafe=clave_coche))
            resenha.put()
            time.sleep(1)
            return self.redirect("/resenhas/resenha_showall?car=" + clave_coche)


app = webapp2.WSGIApplication([
    ('/resenhas/resenha_add', ResenhaAddHandler)
], debug=True)