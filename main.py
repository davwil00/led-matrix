from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
from PIL import ImageFont
from luma.core.virtual import viewport
import time

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=4)


font = ImageFont.truetype("pixelmix.ttf", 8)

virtual = viewport(device, width=200, height=100)

with canvas(virtual) as draw:
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((3, 3), "Hello world", fill="white")

for offset in range(8):
    virtual.set_position((offset, offset))
    time.sleep(0.1)
