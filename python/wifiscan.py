#!/usr/bin/python3
#
# very simple and basic scanner for available wifis. One line per Wifi, 
# most stuff I need included.
# may work best with watch -n1 and grep or something like that.

import wifi

for cell in wifi.Cell.all('wlp3s0'):
    print(cell.signal, cell.quality, cell.channel, cell.frequency, cell.encrypted, cell.encryption_type, cell.mode, cell.address, cell.ssid)

