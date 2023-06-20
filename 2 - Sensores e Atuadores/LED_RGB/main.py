import machine
from time import sleep
pin_red = machine.Pin(23, machine.Pin.OUT)
pin_green = machine.Pin(22, machine.Pin.OUT)
pin_blue = machine.Pin(21, machine.Pin.OUT)

pwm_red = machine.PWM(pin_red)
pwm_green = machine.PWM(pin_green)
pwm_blue = machine.PWM(pin_blue)

pwm_red.freq(1000)
pwm_green.freq(1000)
pwm_blue.freq(1000)

def set_rgb_color(red, green, blue):
    pwm_red.duty(red * 4)
    pwm_green.duty(green * 4)
    pwm_blue.duty(blue * 4)

while True:
  set_rgb_color(255, 0, 0)
  sleep(1)
  set_rgb_color(0, 255, 0)
  sleep(1)
  set_rgb_color(0, 0, 255)
  sleep(1)
