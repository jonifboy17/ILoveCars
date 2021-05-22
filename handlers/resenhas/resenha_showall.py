import webapp2
from webapp2_extras import jinja2

from model.resenha import Resenha


class ResenhaShowallHandler(webapp2.RequestHandler):
    def get(self):
        coche, resenhas = Resenha.recupera_para(self.request)

        valores_plantilla = {
            "resenhas": resenhas,
            "coche": coche
        }

        jinja = jinja2.get_jinja2(app=self.app)

        self.response.write(
            jinja.render_template("resenhas_showall.html", **valores_plantilla))


app = webapp2.WSGIApplication([
    ('/resenhas/resenha_showall', ResenhaShowallHandler)
], debug=True)