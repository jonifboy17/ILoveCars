# coding: utf-8
# Un coche registrado

from google.appengine.ext import ndb


class Coche(ndb.Model):

    marca = ndb.StringProperty(indexed=True)
    modelo = ndb.StringProperty(required=True)
    carroceria = ndb.StringProperty(required=True)
    anho = ndb.IntegerProperty(required=True)
    foto = ndb.BlobProperty(default=None)

    id_coche = ndb.StringProperty(required=True)


    @staticmethod
    def obtener_id_coche(marca, modelo, carroceria, anho):
        m = marca[0:3]
        mo = modelo
        ca = carroceria
        an = str(anho)

        return m + mo + ca + an

    @staticmethod
    def recupera(req):
        try:
            id_coche = req.GET["id"]
        except KeyError:
            id_coche = ""

        return ndb.Key(urlsafe=id_coche).get()
