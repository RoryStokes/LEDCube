import time
try:
	import RPi.GPIO as GPIO
except ImportError:
	import GPIO
	import matplotlib.pyplot as plt
	from mpl_toolkits.mplot3d import Axes3D
	global emulated
	emulated = True
import threading
import numpy as np
import Queue
import atexit

class LEDCube:
	class CubeThread(threading.Thread):
		def __init__(self,n,dt):
			self.pins = [3,5,7,11,13,15,19,21,23,29,31,33,35,37,8,10,12,16,18,22,24,26,32,36,38,40]
			threading.Thread.__init__(self)
			GPIO.setmode(GPIO.BOARD)
			for pin in self.pins:
				if pin<27:
					GPIO.setup(pin, GPIO.OUT)

			self.lattice = np.zeros((n,n,n),dtype=bool)
			self.n = n

			self.dt = dt
			self.q = Queue.Queue()
			self.layer = 0
			self.running = True

		def run(self):
			global emulated
			while self.running:
				while not self.q.empty():
					e = self.q.get()
					if e == 'Q':
						break

				for x in range(0,self.n):
					for y in range(0,self.n):
						i = 1 + y*self.n + x
						if self.pins[i]<27:
							GPIO.output(self.pins[i], int(self.lattice[self.layer,x,y]))

				GPIO.output(26,1)
				self.layer = (self.layer+1)%self.n
				GPIO.output(26,0)

				if emulated:
					GPIO.display(self)

				time.sleep(self.dt/1000)

		def stop(self):
			self.running = False

	def __init__(self,n,dt):
		self.n = n
		self.thread = LEDCube.CubeThread(n,dt)
		self.thread.start()
		atexit.register(self.cleanup)
	
	def cleanup(self):
		self.thread.stop()

	def set(self,coord,val):
		self.thread.lattice[coord] = val

	def toggle(self,coord):
		self.thread.lattice[coord] = not self.thread.lattice[coord]

	def fillCol(self,col,h,val=1):
		for i in range(0,h):
			self.thread.lattice[i][col] = val
		for i in range(h,self.n):
			self.thread.lattice[i][col] = not val

	def fill(self, h, val=1):
		for x in range(0,self.n):
			for y in range(0,self.n):
				fillCol((x,y),h,val)
