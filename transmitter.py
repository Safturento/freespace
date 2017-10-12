import RPi.GPIO as io
import time

oLED = 21

dt = .1
io.setmode(io.BCM)
io.setwarnings(False)

message = "Hello World"
binMsg = "".join(format(ord(x), 'b').zfill(8) for x in message)
bitList = [int(x) for x in binMsg]

total = len(bitList)

io.setup(oLED, io.OUT)

for bit in bitList:
	io.output(oLED, 1)
	if bit==1:
		time.sleep(dt*.75)
		io.output(oLED, 0)
		time.sleep(dt*.25)
	else:
		time.sleep(dt*.25)
		io.output(oLED,0)
		time.sleep(dt*.75)

#make sure to turn it off after
io.output(oLED, 0)
