import RPi.GPIO as io
import time
import re

iLED = 17
dt = .03
io.setmode(io.BCM)
io.setwarnings(False)

ledInput = []

io.setup(iLED, io.IN)

start = 0

def toChar(bits):
	return chr(int(''.join(str(bit) for bit in bits),2))


while True:
	# Possible start bit
	if io.input(iLED):
		time.sleep(dt*.5)
		# Check if valid start bit
		if io.input(iLED):
			bits = []
			for i in range(8):
				time.sleep(dt)
				bits.append(io.input(iLED))
			print(toChar(bits))



# while time.time()-start < 10:
# 	time.sleep(dt)
# 	ledInput.append(io.input(iLED))

# p = re.compile("([1]+[0]+)")

# #splits input into chunks of 1's followed by 0's
# splitInput = list(filter(None, p.split(''.join([str(x) for x in ledInput]))[1:]))

# #print(len(splitBits))

# parsedBits = []
# for x in splitInput:
# 	print(1 if x.count('1')/len(x) > .5 else 0)
# 	parsedBits.append(1 if x.count('1')/len(x) > .5 else 0)

# recievedStr = ''.join([chr(int(''.join(x),2)) for x in zip(*[iter(''.join(map(str,parsedBits)))]*8)])

# print(recievedStr)
