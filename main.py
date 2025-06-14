import lvgl as lv
import sys

if sys.platform == 'linux':
    from micropython import const  # NOQA
    import lcd_bus  # NOQA
    import time
    _WIDTH = const(320)
    _HEIGHT = const(240)
    bus = lcd_bus.SDLBus(flags=0)
    buf1 = bus.allocate_framebuffer(_WIDTH * _HEIGHT * 3, 0)
    import sdl_display  # NOQA
    display = sdl_display.SDLDisplay(
        data_bus=bus,
        display_width=_WIDTH,
        display_height=_HEIGHT,
        frame_buffer1=buf1,
        color_space=lv.COLOR_FORMAT.RGB888
    )
    display.init()

    import sdl_pointer
    import task_handler

    mouse = sdl_pointer.SDLPointer()

    # the duration needs to be set to 5 to have a good response from the mouse.
    # There is a thread that runs that facilitates double buffering. 
    th = task_handler.TaskHandler(duration=5)
else:
    import comunication as comu
    import teclado
    import machine
    miTeclado = teclado.teclado()
    tim0 = machine.Timer(1)
    tim0.init(period=200, mode=machine.Timer.PERIODIC, callback=lambda t:miTeclado.key_loop())

#comun arranque
import guiObj1

meGuiObj = guiObj1.guiObj1()
meGuiObj.execScreen()