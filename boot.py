import sys
import lcd_bus
import ili9341
from machine import SPI, Pin
import lvgl as lv
import uos

HOSTTYPE = uos.uname()[4]

if HOSTTYPE.find("GALDEANO CLASSIC") >=0:
    mosiPIN = 23
    misoPIN = 19
    sckPIN  = 18
    dcPIN   = 2
    csPIN   = 15
    rstPIN  = 4
    cs_touch = 21
    tactil = 'xpt2046'
elif HOSTTYPE.find("GALDEANO CIVER") >=0:
    mosiPIN = 11
    misoPIN = 13
    sckPIN  = 12
    dcPIN   = 16
    csPIN   = 10
    rstPIN  = 14
    cs_touch = 15
    tactil = 'xpt2046'
elif HOSTTYPE.find("GALDEANO M5") >=0:
    mosiPIN = 23
    misoPIN = 38
    sckPIN  = 18
    dcPIN   = 15
    csPIN   = 5
    rstPIN  = None
    cs_touch = None
    tactil = 'ft6x36'
else:
    print("NO GRAFICS")


spi_bus = SPI.Bus(
    host=1,
    mosi=mosiPIN,
    miso=misoPIN,
    sck=sckPIN
)
display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    dc=dcPIN,
    cs=csPIN,
    freq=40000000,
)
display = ili9341.ILI9341(
    data_bus=display_bus,
    display_width=240,
    display_height=320,
    reset_pin=rstPIN,
    # comment the next line if you still don't get something on the display
    reset_state=ili9341.STATE_LOW,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=ili9341.BYTE_ORDER_BGR,
    rgb565_byte_swap=False
)

display.init(2)
if tactil == 'xpt2046':
    import xpt2046
    touch_dev = SPI.Device(
        spi_bus=spi_bus,
        freq=100000,
        cs=cs_touch
    )

    indev = xpt2046.XPT2046(touch_dev)
elif tactil == 'ft6x36':
    from ft6x36 import ft6x36
    touch = ft6x36(width=320, height=280)
    indev = ft6x36.ft6x36()
    
if not indev.is_calibrated:
    display.set_backlight(100)
    indev.calibrate()

display.set_rotation(lv.DISPLAY_ROTATION._270)

import task_handler
th = task_handler.TaskHandler(20)
