from os import system
import cv2
class camara2:
	def tomar(self):
		system("sudo fswebcam -r 1280x720 --no-banner --png 9  /home/buho/Documents/proyecto/programa/imagenes/imagen1280.png")
		#print("foto tomada")
	def resize(self):
		dire ="/home/buho/Documents/proyecto/programa/imagenes/imagen1280.png"
        	#print(dire)
		img = cv2.imread(dire)
        	#print("carge la imagen")
		h,w,x = img.shape
		#print("h",h)
		#print("w",w)
		clone  = img[40:650,280:1200]
		#cv2.imshow("imagen clonada",clone)
		res = cv2.resize(clone,(640,480))
		#cv2.waitKey(0)
		name = "/home/buho/Documents/proyecto/programa/imagenes/imagen.png"
		cv2.imwrite(name,res)

	def eliminar(self):
		system("sudo rm -r /home/buho/Documents/proyecto/pythonpru/imagenes/imagen.jpg")
		#print("elimine la foto")
