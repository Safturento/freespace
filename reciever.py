import RPi.GPIO as io
import time
import re

iLED = 17
dt = .01
io.setmode(io.BCM)
io.setwarnings(False)

ledInput = []

io.setup(iLED, io.IN)

start = time.time()

while time.time()-start < 10:
	time.sleep(dt)
	ledInput.append(io.input(iLED))

p = re.compile("([1]+[0]+)")

#splits input into chunks of 1's followed by 0's
splitInput = list(filter(None, p.split(''.join([str(x) for x in ledInput]))[1:]))

#print(len(splitBits))

parsedBits = []
for x in splitInput:
	print(1 if x.count('1')/len(x) > .5 else 0)
	parsedBits.append(1 if x.count('1')/len(x) > .5 else 0)

recievedStr = ''.join([chr(int(''.join(x),2)) for x in zip(*[iter(''.join(map(str,parsedBits)))]*8)])

print(recievedStr)
