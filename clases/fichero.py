from os import system
import os
class carpetas:
	def __init__(self):
		self.direccion = '/home/buho/Documents/proyecto/programa/imagenes/resultados/'
		self.actual = ''
		self.direccion2 = '/home/buho/Documents/proyecto/programa/imagenes/muestras'
		contenido = os.listdir(self.direccion)
		contenido2 = os.listdir(self.direccion2)
		self.contador = len(contenido)
		self.contador2 = 0
		self.contador3 = len(contenido2)
	def dirCarpeta(self,estado):

		if estado == 1:
			self.contador += 1
			self.contador2 = 1
			self.actual = self.direccion + "parada{}".format(self.contador)
			system("sudo mkdir {}".format(self.actual))
			system("sudo chmod a+w {}".format(self.actual))
		
		elif estado ==2:
			self.contador2 += 1
		return self.actual
			
	def moverImagenYEliminarCarpeta(self):
		system("sudo mv {}/resultado/imagen.jpg {}/imagen{}.jpg".format(self.actual,self.actual,self.contador2))
		system("sudo rm -r {}/resultado".format(self.actual))
	
	def moverImagenMuestra(self):
		self.contador3 += 1
		system("sudo mv /home/buho/Documents/proyecto/programa/imagenes/imagen.png {}/imagen{}.png".format(self.direccion2,self.contador3))
