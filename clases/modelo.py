import torch
import cv2
from matplotlib import pyplot as plt
import numpy as np
from time import sleep

class modelo:
	def __init__(self,modelo,camara,carpeta,monitor):
		self.modelo = torch.hub.load('ultralytics/yolov5', 'custom', path=modelo)
		self.modelo.conf = 0.48
		#self.modelo.iou = 0.4
		self.camara = camara
		self.carpeta = carpeta
		self.monitor = monitor
		self.monitor.imprimir("MODELO CARGADO")
		
	
	def inferir(self,imagen,estado):
		print("realizando inferencia")
		self.resul = self.modelo(imagen)
		print("inferencia realizada")
		if (len(self.resul.pandas().xyxy[0])):
			self.monitor.imprimir("HAY BOTELLAS")
			dire = self.carpeta.dirCarpeta(estado)
			resulDire = dire+"/resultado"
			self.resul.save(save_dir=resulDire)
			#input("estoy re")
			self.carpeta.moverImagenYEliminarCarpeta()
			self.resul.show()
			return self.resul.pandas().xyxy[0],True
		else:
	            self.monitor.imprimir("NO HAY BOTELLAS")
        	    return self.resul.pandas().xyxy[0],False
