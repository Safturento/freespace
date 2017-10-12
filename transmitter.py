import RPi.GPIO as io
import time

oLED = 21

dt = .02
io.setmode(io.BCM)
io.setwarnings(False)

message = "Hello World"
messageBytes = [format(ord(x), 'b').zfill(8) for x in message]
byteList = [tuple(int(bit) for bit in byte) for byte in messageBytes]

total = len(byteList)

io.setup(oLED, io.OUT)

for byte in byteList:
	# Send start bit
	io.output(oLED, 1)
	time.sleep(dt)

	# Send 8 bits for character
	for bit in byte:
		io.output(oLED, bit)
		time.sleep(dt)

	# Send stop bit
	io.output(oLED, 0)
	time.sleep(dt)

#make sure to turn it off after
io.output(oLED, 0)
