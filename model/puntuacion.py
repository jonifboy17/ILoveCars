# Puntuación por estrellas para indicar como de bueno es un coche

from google.appengine.ext import ndb

from coche import Coche

class Puntuacion(ndb.Model):

    puntos = ndb.IntegerProperty(required=True)
    clave_coche = ndb.KeyProperty(kind=Coche)

    @staticmethod
    def recupera_para(req):
        try:
            id_car = req.GET["car"]
        except KeyError:
            id_car = ""

        if id_car:
            clave_coche = ndb.Key(urlsafe=id_car)
            puntuaciones = Puntuacion.query(Puntuacion.clave_coche == clave_coche)
            return puntuaciones
        else:
            print ("ERROR: Coche no encontrado")