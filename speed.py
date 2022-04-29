import RPi.GPIO as GPIO
import time
import math
import smtplib

#Email Notification
SMTP_SERVER = 'smtp.gmail.com' #Email Server (don't change!)
SMTP_PORT = 587 #Server Port (don't change!)
GMAIL_USERNAME = #email
GMAIL_PASSWORD = #password

class Emailer:
    def sendmail(self, recipient,  subject, content):
        #Creating the headers
        headers = ["From: " + GMAIL_USERNAME, "Subject: " +subject, 
            "To: " + recipient, "MIME-Version 1.0", "Content-Type: text/html"]
        headers = "\r\n".join(headers)

        #Connect to Gmail Server
        session = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        session.ehlo()
        session.starttls()
        session.ehlo()

        #Login to Gmail
        session.login(GMAIL_USERNAME, GMAIL_PASSWORD)

        #Send Email & Exit
        session.sendmail(GMAIL_USERNAME, recipient, headers + "\r\n\r\n" + content)
        session.quit

GPIO.setmode(GPIO.BOARD)
trig=11
echo=13
GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)
samp = 20
offset = 0.0
SOS = 34300

totdist = 0
avgdist = 0
distZero = 0
distOne = 0

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
print('Read' +str(x+1) + '/' +str(samp), str(round(pulse_width,9)))

distOne = (pulse_width * SOS * 0.5)
totdist+= distOne
if distOne < -100000 or distOne > 400000: dist_error = True
velocity = ((distOne - distZero)/pulse_end1 - pulse_end0)
speed = abs(velocity)
distZero = distOne
totspeed+= speed
totvelocity+= velocity

if dist_error:
  print('Out of range')
else:
  vel= (totvelocity/samp)
  vel= str(vel)
  avgspeed = (totspeed/samp)
  avgspeed = round(avgspeed,2)
  avgspeed = str(avgspeed)
  print('Vel:'+ vel + 'Avg Speed: '+avgspeed)
  sender = Emailer()
  sendTo = '#recipient email
  emailSubject = "IOT Research: Speed"
  emailContent = "This is the Pi in the lab.\n Avg Speed and Velocity detected! \nAvg Speed: "+avgspeed+ "\nAvg: Velocity: "+vel
  sender.sendmail(sendTo, emailSubject, emailContent)
  
  GPIO.cleanup()
  print('Finished')
