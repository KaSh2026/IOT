import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)

while(1):
         GPIO.output(7,False)      //1st led to GPIO 7
         print("LED 1 IS OFF")
         time.sleep(1)
         GPIO.output(29,False)      //2st led to GPIO 29 
         print("LED 2 IS OFF")
         time.sleep(1.5)
         GPIO.output(31,False)      //3RD LED TO GPIO 31
         print("LED 3 IS OFF")
         time.sleep(2)
         GPIO.output(33,False)      //4TH LED TO GPIO 33
         print("LED 4 IS OFF")
         time.sleep(2.5)
    
         
         GPIO.output(7,True)
         print("LED 1 IS FINALLY ON")
         time.sleep(3.5)
         GPIO.output(29,True)
         print("LED 2 IS FINALLY ON")
         time.sleep(4)
         GPIO.output(31,True)
         print("LED 3 IS FINALLY ON")
         time.sleep(4.5)
         GPIO.output(33,True)
         print("LED 4 IS FINALLY ON")
         time.sleep(5)
         
         GPIO.output(7,False)
         print("LED 1 IS OFF")
         time.sleep(1)
         GPIO.output(29,False)
         print("LED 2 IS OFF")
         time.sleep(1.5)
         GPIO.output(31,False)
         print("LED 3 IS OFF")
         time.sleep(2)
         GPIO.output(33,False)
         print("LED 4 IS OFF")
         time.sleep(2.5)
         print("PROGRAM COMPLETE!")
         GPIO.cleanup()