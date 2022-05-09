# Spedometer-Raspberry-Pi

# Description
This project measures speed and velocity using the HCsr04 ultrasonic sensor on Raspberry Pi. This code also uses an email class with smtplib to send a notication via email when the voltage reading is high. This project assumes that you have already setup your Raspberry Pi and have the Freenove Starter kit directory. If you do not you will need to setup Raspberry Pi and Freenove before you start this project. 

# Materials Needed
## Hardware
1. Raspberry Pi x1
2. GPIO Extension Board & Ribbon Cable x1
3. Breadboard x1
4. HC-SR04 Module
5. Male-to-Female Jumper Wires x6
6. 2 Resistors

## Software
1. speed.py from this repository

# Setup and Configuration
## Hardware
Below is the following pinout for this project:
![image](https://user-images.githubusercontent.com/66813474/167399530-6004d83d-15b5-48e0-a912-4460fa1dacb2.png)

_Note: please plug in your cables BEFORE turning on your Raspberry Pi to prevent shorting out your parts._

# Code Setup
1. Download speed.py
2. Open voltage.py and change the following lines to correspond with the email notication:
    1. line 9: enter the email that you want to send the notification from
    2. line 10: enter the password to the email from line 10
    3. line 94: enter the recipient email
    4. line 95(optional): you can change the email subject
    5. line 96(optional): you can change the contents of the email
4. Run speed.py and move an object in front of the sensor to measure speed and velocity.
