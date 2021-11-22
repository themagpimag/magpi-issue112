from gpiozero import Button, LED, Buzzer
from time import sleep

laser = Button(21)
sound = Button(14)
led = LED(16)
buzzer = Buzzer(25)

def alarm():
    print("Intruder alert!", end = "\r")
    for i in range (10):
        led.toggle()
        buzzer.toggle()
        sleep(0.5)
        
while True:
    if laser.value == 0 or sound.value == 1:
        alarm()
    else:
        print ("All clear      ", end = "\r")
        led.off()
        buzzer.off()