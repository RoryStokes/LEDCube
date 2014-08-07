import LEDCube
import time

wave = [1,2,3,3,2,1]
cube = LEDCube.LEDCube(5,1000)

while True:
	for t in range(0,6):
		for x in range(0,5):
			for y in range(0,5):
				cube.fillCol((x,y),wave[(x+t+y)%len(wave)])
		
		time.sleep(0.1)
