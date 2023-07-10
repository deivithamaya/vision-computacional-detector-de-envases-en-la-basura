import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

class sensor:
	def __init__(self,pin):
		self.pin = pin
		GPIO.setup(pin,GPIO.IN,pull_up_down = GPIO.PUD_UP) 
	
	def detectar(self) : 
		while True:
			input = GPIO.input(self.pin)
			if input == False:
				break
			return True
			sleep(0.2)
		return False
