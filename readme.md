# Teilmagotchi

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
