# coding: utf-8
# Resenha de un usuario para un coche determinado

from google.appengine.ext import ndb

from coche import Coche

class Resenha(ndb.Model):

    email = ndb.StringProperty(required=True)
    opinion = ndb.StringProperty(required=True)
    clave_coche = ndb.KeyProperty(kind=Coche)

    @staticmethod
    def recupera_res(req):
        try:
            id_resenha = req.GET["id"]
        except KeyError:
            id_resenha = ""

        return ndb.Key(urlsafe=id_resenha).get()

    @staticmethod
    def recupera_para(req):
        try:
            id_car = req.GET["car"]
        except KeyError:
            id_car = ""

        if id_car:
            clave_coche = ndb.Key(urlsafe=id_car)
            resenhas = Resenha.query(Resenha.clave_coche == clave_coche)
            return (clave_coche.get(), resenhas)
        else:
            print ("ERROR: Coche no encontrado")