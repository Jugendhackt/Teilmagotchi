from time import sleep_ms
from machine import UART
from machine import Pin

pLED = Pin(2, Pin.OUT)

def serialecho():
    print("serial hello started")
    uart = UART(2,baudrate=115200) # 16:RX 17:TX
    # uart.init(, bits=8, parity=None, stop=1)
    # sleep_ms(100)
    counter = 0

    while True:
        counter += 1
        if counter >= 20:
            counter = 0
            uart.write("hello\n")
            print("hello sent")
        # sleep_ms(2000)
        pLED.value(uart.any())
        while uart.any():
            x=uart.read().decode("utf-8")
            print("Got", x)
            # uart.write(x)
        sleep_ms(100)
    
serialecho()