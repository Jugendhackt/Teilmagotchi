from time import sleep_ms
from machine import UART
from machine import Pin

pLED = Pin(2, Pin.OUT)
pTasterA = Pin(5,Pin.IN, Pin.PULL_UP)
pTasterB = Pin(18,Pin.IN, Pin.PULL_UP)

def serialecho():
    print("serial hello started")
    uart = UART(2,baudrate=115200) # 16:RX 17:TX
    # uart.init(, bits=8, parity=None, stop=1)
    # sleep_ms(100)
    wassentA = False
    wassentB = False

    while True:
        
        if pTasterA.value() == 0 and wassentA == False:
            wassentA = True
            uart.write("A\n")
            print("A sent")
        if pTasterA.value() == 1:
            wassentA = False

        if pTasterB.value() == 0 and wassentB == False:
            wassentB = True
            uart.write("B\n")
            print("B sent")
        if pTasterB.value() == 1:
            wassentB = False

        # sleep_ms(2000)
        pLED.value(uart.any())
        while uart.any():
            x=uart.read().decode("utf-8")
            print("Got", x)
            # uart.write(x)
        sleep_ms(100)
    
serialecho()