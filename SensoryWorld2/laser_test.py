from gpiozero import Button

laser = Button(21)
msg = ""

while True:
    #print(laser.value)
    if laser.value == 0:
        msg = "Intruder!"
    else:
        msg = "All clear"
    print(msg, end = "\r")