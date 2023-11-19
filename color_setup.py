# color_setup.py Customise for your hardware config

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2020 Peter Hinch

# As written, supports:
# ili9341 240x320 displays on Pi Pico
# Edit the driver import for other displays.

# Demo of initialisation procedure designed to minimise risk of memory fail
# when instantiating the frame buffer. The aim is to do this as early as
# possible before importing other modules.

# WIRING
# Pico      Display
# GPIO Pin
# 3v3  36   Vin
# IO6   9   CLK  Hardware SPI0
# IO7  10   DATA (AKA SI MOSI)
# IO8  11   DC
# IO9  12   Rst
# Gnd  13   Gnd
# IO10 14   CS

from machine import Pin, SPI, SoftI2C
import gc

# *** Choose your color display driver here ***
# ili9341 specific driver
#from drivers.ili94xx.ili9486 import ILI9486 as SSD
from drivers.ssd1306.ssd1306 import SSD1306_I2C as SSD

i2c = SoftI2C(scl=Pin(25), sda=Pin(26))

# Kept as ssd to maintain compatability
gc.collect()  # Precaution before instantiating framebuf
# See DRIVERS.md re overclocking the SPI bus
ssd = SSD(128, 64, i2c)
