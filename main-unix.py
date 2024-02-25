
import lvgl as lv
import fb
import evdev
import time

lv.init()
fb.init()

# Register FB display driver

disp_buf1 = lv.disp_draw_buf_t()
buf1_1 = bytes(320*10)
disp_buf1.init(buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
disp_drv.init()
disp_drv.draw_buf = disp_buf1
disp_drv.flush_cb = fb.flush
disp_drv.hor_res = 320
disp_drv.ver_res = 240
disp_drv.register()

# Create a screen and a button

scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Hello Angel2")


mouse = evdev.mouse_indev(scr)

# Load the screen

lv.scr_load(scr)

while True:
	time.sleep(1)

