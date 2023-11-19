from color_setup import ssd
import framebuf
import time

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

i = 0
while True:
    if (i % 10 < 5):
        shift = -1
    else:
        shift = 1

    ssd.scroll(0, shift)
    ssd.show()

    time.sleep_ms(50)
    i += 1
