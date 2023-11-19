from time import sleep_ms
from machine import Pin, SPI, SoftI2C, UART
import gc
from drivers.ssd1306.ssd1306 import SSD1306_I2C as SSD
import framebuf

pLED = Pin(2, Pin.OUT)
pTasterA = Pin(5,Pin.IN, Pin.PULL_UP)
pTasterB = Pin(18,Pin.IN, Pin.PULL_UP)

i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
gc.collect()
ssd = SSD(128, 64, i2c)

alpaca = framebuf.FrameBuffer(bytearray(11 * 11 * 2), 11, 11, framebuf.MONO_HLSB)
alpaca.hline(1, 0, 2, 1)
alpaca.hline(8, 0, 2, 1)
alpaca.rect(0, 1, 4, 3, 1, True)
alpaca.rect(7, 1, 4, 3, 1, True)
alpaca.rect(4, 2, 4, 2, 1, True)
alpaca.vline(0, 4, 5, 1)
alpaca.vline(10, 4, 5, 1)
alpaca.pixel(1, 4, 1)
alpaca.pixel(9, 4, 1)
alpaca.vline(1, 8, 2, 1)
alpaca.vline(2, 9, 2, 1)
alpaca.vline(9, 8, 2, 1)
alpaca.vline(8, 9, 2, 1)
alpaca.hline(3, 10, 5, 1)
alpaca.pixel(2, 6, 1)
alpaca.pixel(8, 6, 1)
alpaca.pixel(4, 7, 1)
alpaca.pixel(6, 7, 1)
alpaca.hline(4, 8, 3, 1)

ssd.blit(alpaca, 59, 27)
ssd.show()


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
            uart.write("A")
            print("A sent")
        if pTasterA.value() == 1:
            wassentA = False

        if pTasterB.value() == 0 and wassentB == False:
            wassentB = True
            uart.write("B")
            print("B sent")
        if pTasterB.value() == 1:
            wassentB = False

        # sleep_ms(2000)
        pLED.value(uart.any())
        while uart.any():
            x=uart.read().decode("utf-8")
            print("Got", x)
            ssd.fill(0)
            ssd.text(x,15,5)
            ssd.blit(alpaca, 59, 27)
            ssd.show()
            # uart.write(x)
        sleep_ms(100)
    
serialecho()