import time
import RPi.GPIO as GPIO
import threading
import numpy as np
import Queue

class LEDCube:
	class CubeThread(threading.Thread):
		def __init__(self,n,dt):
			self.pins = [3,5,7,11,13,15,19,21,23,29,31,33,35,37,8,10,12,16,18,22,24,26,32,36,38,40]
			threading.Thread.__init__(self)
			GPIO.setmode(GPIO.BOARD)
			for pin in self.pins:
				GPIO.setup(pin, GPIO.OUT)

			self.lattice = np.zeros(n,n,n)
			self.n = n

			self.dt = dt
			self.q = Queue.Queue()
			self.layer = 0

		def run(self):
			while(True):
				while not self.q.empty():
					e = self.q.get()
					if e = 'Q':
						break

				for x in range(0,self.n):
					for y in range(0,self.n):
						i = 1 + y*self.n + x
						GPIO.output(self.pins[i], self.lattice[self.layer,x,y])

				GPIO.output(26,1)
				self.layer = (self.layer+1)%self.n
				GPIO.output(26,0)
				time.sleep(self.dt/1000)

	def __init__(self,n,dt):
		self.thread = LEDCube.CubeThread(n,dt)
		self.thread.start()

	def set(self,coord,val):
		self.thread.lattice[coord] = val

	def toggle(self,coord):
		self.thread.lattice[coord] = 1-self.thread.lattice[coord]

	def fillCol(self,col,h=n,val=1):
		for i in range(0,h):
			self.thread.lattice[i][col] = val
		for i in range(h,n):
			self.thread.lattice[i][col] = 1-val

	def fill(self, h=n, val=1):
		for x in range(0,n):
			for y in range(0,n):
				fillCol((x,y),h,val)