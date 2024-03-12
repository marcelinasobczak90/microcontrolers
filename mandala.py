import board
import digitalio
import neopixel
import time
from adafruit_led_animation.color import (
    PURPLE,
    WHITE,
    AMBER,
    JADE,
    TEAL,
    PINK,
    MAGENTA,
    ORANGE,
    RED,
    GREEN,
    BLUE,
)
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.helper import PixelMap

leds_num = 100
tail_num = 21
brightness = 5.0 #1.0
pixel_order = (2,1,0)
color1 = [144,46,89]
color2 = [144,16,59]
color3 = [255,46,200]
color4 = [75,0,130]

leds = neopixel.NeoPixel(board.GP28, leds_num, brightness=brightness, auto_write=True, pixel_order=pixel_order)

tail = [i for i in range(0,tail_num)]
inner_square = [i for i in range(22,42)]
inner_star = [i for i in range(42,59)] + [21]
sharp_star = [i for i in range(59,73)] + [98,99] 
outer_star = [i for i in range(73,98)] 

tail_pixels = PixelMap(leds, tail, individual_pixels=True)
inner_pixels = PixelMap(leds, inner_square, individual_pixels=True)
inner_star_pixels = PixelMap(leds, inner_star, individual_pixels=True)
sharp_star_pixels = PixelMap(leds, sharp_star, individual_pixels=True)
outer_star_pixels = PixelMap(leds, outer_star, individual_pixels=True)

inner1_1 = Solid(inner_pixels, color=color1)
inner1_2 = Solid(inner_pixels, color=color4)
inner1_3 = Solid(inner_pixels, color=color2)
inner1_4 = Solid(inner_pixels, color=color3)

inner1 = AnimationSequence(
    inner1_1, inner1_2, inner1_3, inner1_4, advance_interval=0.5, auto_clear=False, random_order=False
)

inner2_1 = Solid(inner_star_pixels, color=color3)
inner2_2 = Solid(inner_star_pixels, color=color1)
inner2_3 = Solid(inner_star_pixels, color=color4)
inner2_4 = Solid(inner_star_pixels, color=color2)

inner2 = AnimationSequence(
    inner2_1, inner2_2, inner2_3, inner2_4, advance_interval=0.5, auto_clear=False, random_order=False
)

sharp_1 = Solid(sharp_star_pixels, color=color2)
sharp_2 = Solid(sharp_star_pixels, color=color3)
sharp_3 = Solid(sharp_star_pixels, color=color1)
sharp_4 = Solid(sharp_star_pixels, color=color4)

sharp = AnimationSequence(
    sharp_1, sharp_2, sharp_3, sharp_4, advance_interval=0.5, auto_clear=False, random_order=False
)

outer_1 = Solid(outer_star_pixels, color=color4)
outer_2 = Solid(outer_star_pixels, color=color2)
outer_3 = Solid(outer_star_pixels, color=color3)
outer_4 = Solid(outer_star_pixels, color=color1)

outer = AnimationSequence(
    outer_1, outer_2, outer_3, outer_4, advance_interval=0.5, auto_clear=False, random_order=False
)

while True:
    inner1.animate()
    inner2.animate()
    sharp.animate()
    outer.animate()
