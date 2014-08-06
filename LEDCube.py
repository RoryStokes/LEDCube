import time
import RPi.GPIO as GPIO
import threading
import numpy as np
import Queue



class LEDCube:
	class CubeThread(threading.Thread):
		def __init__(self,n,dt):
			threading.Thread.__init__(self)
			GPIO.setmode(GPIO.BCM)
			for i in range(1,27):
				GPIO.setup(i, GPIO.OUT)
			
			GPIO.output(26,0)

			self.lattice = np.zeros(n,n,n)
			self.h = n

			self.dt = dt
			self.q = Queue.Queue()
			self.layer = 0

		def run(self):
			while(True):
				while !q.empty():
					e = q.get()
					if e = 'Q':
						break

				for x in range(0,n):
					for y in range(0,n):
						bcm = 1 + y*n + x
						GPIO.output(bcm, lattice[self.layer,x,y])

				GPIO.output(26,1)
				self.layer = (self.layer+1)%self.h
				GPIO.output(26,0)
				time.sleep(self.dt)

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