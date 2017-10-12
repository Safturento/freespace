import RPi.GPIO as io
import time

oLED = 21
iLED = 17

dt = .003
io.setmode(io.BCM)
io.setwarnings(False)

message = "Hello World"
# lorem ipsum oaiwjfoi qwiejf oiqwejf qwiopjfiopqwejfiop qjwefopij qweiopfj qwiopef qiopwef oqpiwejfqiopwefj iop"
binMsg = "".join(format(ord(x), 'b').zfill(8) for x in message)
#binMsg = [bin(ord(x))[2:] for x in message]
bitList = [int(x) for x in binMsg]

#print(bitList)

recieved = []

total = len(bitList)
errors = 0

io.setup(oLED, io.OUT)
io.setup(iLED, io.IN)

for bit in bitList:
	time.sleep(dt)
	io.output(oLED, bit)
	time.sleep(dt)
	recieved.append(io.input(iLED))

#make sure to turn it off after
io.output(oLED, 0)

for i in range(total):
	if bitList[i] != recieved[i]:
		errors+=1

recievedStr = ''.join(map(str,recieved))
#print([''.join(x) for x in zip(*[iter(''.join(recievedStr))]*8])


print(''.join([chr(int(''.join(x),2)) for x in zip(*[iter(''.join(recievedStr))]*8 )]))

print(errors, errors/total*100)
