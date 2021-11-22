from gpiozero import Button

sound = Button(14)
msg = ""

while True:
    #print(sound.value, end = "\r")
    if sound.value == 1:
        msg = "Intruder!"
    else:
        msg = "All clear"
    print(msg, end = "\r")