import LEDCube
import time

wave = [1,2,3,3,2]
cube = LEDCube.LEDCube(5,1)

while True:
	for i in range(0,5):
		for x in range(0,5):
			for y in range(0,5):
				cube.fillCol((x,y),wave[(x+i)%5])
		
		time.sleep(0.1)
