from time import sleep_ms
from machine import UART

def serialecho():
    print("serial echo server started")
    uart = UART(2,baudrate=115200) # 16:RX 17:TX
    # uart.init(, bits=8, parity=None, stop=1)
    while True:
        if uart.any():
            x=uart.read()
            print("Got", x)
            uart.write(x)
        sleep_ms(50)

serialecho()