# Teilmagotchi

![Pinout](https://circuitstate.com/wp-content/uploads/2022/12/ESP32-DevKit-V1-Pinout-Diagram-r0.1-CIRCUITSTATE-Electronics-2.png)

Installieren von Micropython
https://docs.micropython.org/en/latest/esp32/tutorial/intro.html#esp32-intro


mit Wlan verbinden und library für das Display auf dem ESP installieren

```py
import network
# enable station interface and connect to WiFi access point
nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect('your-ssid', 'your-key')
nic.isconnected()
# now use sockets as usual

import mip
mip.install("github:peterhinch/micropython-nano-gui/drivers/ssd1306")
```
