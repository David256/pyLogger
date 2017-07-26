#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Este módulo define una clase Logger, encargada de recibir mensajes
para guardar en un archivo de logs.

>>> l = Logger("salida.log")

Para usar, se cuenta con el método `escribir(...)`, que tiene los
siguientes argumentos:

mensaje : significa el mensaje a guardar.
funcion : nombre de la función que ejecuta este método. Sirve como guía.
exito : especifica si la acción resultó exitosa o no.

"""

import time

class Logger(object):
	"""Crea un log."""
	def __init__(self, ruta):
		super(Logger, self).__init__()
		self.ruta = ruta
		self.archivo = open(self.ruta, "a")
		self._cabecera()

	def _momento(self):
		return time.strftime("[%Y-%m-%d %H:%M:%S]")

	def _cabecera(self):
		self.archivo.write("\n")
		self.archivo.write("%s :: Inicio de sección\n" % self._momento())
	
	def escribir(self, mensaje="", funcion=None, exito=None):
		self.archivo.write(self._momento() + " ")
		
		if funcion != None:
			self.archivo.write("(%s) " % funcion)
		if exito != None:
			if exito:
				self.archivo.write("― OK ― ")
			else:
				self.archivo.write("― Error ― ")
		self.archivo.write("%s." % mensaje)
		self.archivo.write("\n")

	def __del__(self):
		self.archivo.close()