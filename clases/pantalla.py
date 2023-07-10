from os import system

class pantalla:
	def __init__(self):
		system("export DISPLAY=:0")

	def cerrar_ventana(self):
		system("pkill gpicview")
		#print("cerre ventana")
	
	def imprimir(self,mensaje):
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
		print("               {}                  ".format(mensaje))
		print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
