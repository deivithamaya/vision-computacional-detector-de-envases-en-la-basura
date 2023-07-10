#export BROWSER=/usr/bin/firefox
#export DISPLAY=:0

from clases.sensor import sensor
from clases.motor import motor
from clases.camara2 import camara2
from clases.modelo import modelo 
from clases.pantalla import pantalla
from clases.fichero import carpetas
from time import sleep
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('-i','--indicador',type=int,default=0,required=False,help='indicador de detenimiento')
args = parser.parse_args()

pin = 19
pin2 = 21
pwm = 12
dire = 18
model = '/home/buho/Documents/proyecto/programa/modelos/modelo1/best.pt'
model2 = '/home/buho/Documents/proyecto/programa/modelos/modelo2/best.pt'
model3 = '/home/buho/Documents/proyecto/programa/modelos/modelo3/best.pt'
imagen = '/home/buho/Documents/proyecto/programa/imagenes/imagen.png'

sensor_entrada = sensor(pin)
sensor_salida = sensor(pin2)
monitor = pantalla()
motorBanda = motor(pwm,dire,sensor_salida)
camara = camara2()
fichero = carpetas()
yolo = modelo(model3,camara,fichero,monitor)



def bucleDeInferencia():
	#monitor.imprimir("ingrese al bucle de inferencia")
	instantei = datetime.now()
	inferencia,valor = yolo.inferir(imagen,1)
	instantef = datetime.now()
	tiempo = instantef - instantei
	segundos = tiempo.seconds
	monitor.imprimir("se tardo {}segundos".format(segundos))
	#if args.indicador:
	#	input("oprima enter")
	while(valor!=False):
		#print("inferencia",len(inferencia))
		print("inferencia0",inferencia["confidence"][0])
		monitor.imprimir("TOMANDO BOTELLA")
		sleep(10)
		if args.indicador:
			input("oprima enter")
		monitor.cerrar_ventana()
		fichero.moverImagenMuestra()
		camara.tomar()
		camara.resize()
		inferencia,valor = yolo.inferir(imagen,2)
	fichero.moverImagenMuestra()
while True:
	monitor.imprimir("ESPERANDO MUESTRA")
	while sensor_entrada.detectar():
		sleep(0.2)
	#monitor.imprimir("sali del while")
	motorBanda.avanzar()
	#print("hay objeto en la banda")
	camara.tomar()
	camara.resize()
	bucleDeInferencia()
	motorBanda.avanzar_10()
	while not sensor_salida.detectar():
		#print("entre al bucle de 10 segundos")
		camara.tomar()
		camara.resize()
		bucleDeInferencia()
		motorBanda.avanzar_10()

