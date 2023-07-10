import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BOARD)


class motor:
	def __init__(self,PPwm,PDir,Sensor):
		self.pwm = PPwm
		self.dir = PDir
		self.sensor = Sensor
		GPIO.setup(self.pwm,GPIO.OUT)
		GPIO.setup(self.dir,GPIO.OUT)
		self.pulse = GPIO.PWM(self.pwm,100)
		self.pulse.start(0)

	def avanzar(self):
		self.pulse.ChangeDutyCycle(50)
		while self.sensor.detectar():
			sleep(0.1)
		self.pulse.ChangeDutyCycle(0)
		#print("sali")
				
	def avanzar_10(self):
		contador = 0
		contador2 = 0
		self.pulse.ChangeDutyCycle(50)
		#while self.sensor.detectar() ==False:
		#	sleep(0.1)
		while contador2<4:
			sleep(1)
			contador2 += 1
			print("contador2",contador2)
		while self.sensor.detectar() and contador <20 :
			sleep(0.5)
			contador += 1
		self.pulse.ChangeDutyCycle(0)
		#print("sali")	
		
