import uos
import machine

HOSTTYPE = uos.uname()[4]

if HOSTTYPE== 'GALDEANO M5 DEV with ESP32':
    print(HOSTTYPE)
    # Power Management
    from m5core2_power import Power
    power = Power()
    # LCD screen
    from ili9XXX import ili9341
    lcd = ili9341(mosi=23, miso=38, clk=18, dc=15, cs=5, invert=True, factor=16, rot=0x10, width=320, height=240, rst=-1, power=-1, backlight=-1)
    # Touch sensor
    from ft6x36 import ft6x36
    touch = ft6x36(width=320, height=280)
elif HOSTTYPE== 'GALDEANO CLASSIC DEV with ESP32':
    from ili9XXX import ili9341
    from xpt2046 import xpt2046
    disp = ili9341(miso=19, mosi=23, clk=18, cs=15, dc=2, rst=4, power=-1, backlight=-1, backlight_on=0, power_on=0,
        spihost=1, mhz=28, factor=4, hybrid=True, width=320, height=240, start_x=0, start_y=0, invert=False,rot=-4)
    touch=xpt2046()
elif HOSTTYPE== 'GALDEANO CIVER with ESP32S3':
    from ili9XXX import ili9341
    from xpt2046 import xpt2046
    disp = ili9341(miso=13, mosi=11, clk=12, cs=10, dc=16, rst=14, power=0, backlight=0, backlight_on=0, power_on=0,
        spihost=1, spimode=0, mhz=40, factor=16, hybrid=True, width=320, height=240, start_x=0, start_y=0, rot=-4)
    touch=xpt2046()
    