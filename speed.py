import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
trig=11
echo=13
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
samp = 20
offset = 0.0
SOS = 34300

tot dist = 0
avg dist = 0
dist0 = 0
dist1 = 1

speed = 0
totspeed = 0

velocity = 0
totvelocity = 0

pulse_width = 0
pulse_begin = 0
pulse_end0 = 0
pulse_end1 = 0
dist_error=False

for x in range(0,samp):
  GPIO.output(trig, False)
  time.sleep(0.310)
GPIO.output(trig,True)
time.sleep(0.000015)
GPIO.output(trig,False)
pulse_end0 = pulse_end1

while GPIO.input(echo) == 0:
  pulse_begin = time.time()
while GPIO.input(echo) == 1:
  pulse_end1 = time.time()
  
pulse_width = (pulse_end1 - pulse_begin)
print('Read' +str(x+1) + '/' +str(samp), str(round(pulse_width,9))

dist1 = (pulse_width * SOS * 0.5)
totdist+= dist1
if dist1 < 2 or dist 1 > 400: dist_error = True
velocity = (dist1 - dist0)/pulse_end1 - pulse_end0)
speed = abs(velocity)
dist0 = dist1
totspeed+= speed
totvelocity+= velocity

if dist_error:
  print('Out of range')
else:
  vel= int(totvelocity/samp)
  avgspeed = int(totspeed/samp)
  print('Vel:',vel + 'Avg Speed: ',avgspeed)
