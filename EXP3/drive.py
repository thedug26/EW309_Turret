from machine import Pin, PWM
# a - left ; d - right; 'w' - up; 's' - down; q - quit
import ttyacm

tty = ttyacm.open(1)

pwm_12 = PWM(Pin(12))
# duty cycle = 0 goes other way.
# Duty Cycle the same for both inputes > stops motor
pwm_13 = PWM(Pin(13))
pwm_09 = PWM(Pin(9))
pwm_10 = PWM(Pin(10))

pwm_12.freq(50)
pwm_13.freq(50)
pwm_09.freq(50)
pwm_10.freq(50)

freq = 50
speed = 0.25
duty = 65535


class PanTiltDriver:
    def __init__(self, freq):
        self.freq = freq
        pwm_12.freq(freq)
        pwm_13.freq(freq)
        pwm_09.freq(freq)
        pwm_10.freq(freq)

    def pan(self, speed):
        if speed == 0.0:
            pwm_09.duty_u16(round(0))  # Left
            pwm_10.duty_u16(round(0))

        elif 0.0 < speed <= 1.0:
            pwm_09.duty_u16(round(65535 * speed))  # Left
            pwm_10.duty_u16(round(0))  # Right

        elif -1 <= speed < 0.0:
            pwm_09.duty_u16(round(0))  # Left
            pwm_10.duty_u16(round(65535 * speed))  # Right

    def tilt(self, speed):
        if 0.0 < speed <= 1.0:
            pwm_12.duty_u16(round(0))  # Up
            pwm_13.duty_u16(round(65535 * speed))  # Down

        elif -1.0 <= speed < 0.0:
            pwm_12.duty_u16(round(65535 * speed))  # Up
            pwm_13.duty_u16(round(0))  # Down

        elif speed == 0.0:
            pwm_12.duty_u16(round(0))  # Up
            pwm_13.duty_u16(round(0))  # Down


motor = PanTiltDriver(freq)

while True:
    pt = input("Enter 'p' for pan or 't' for tilt or 'q' to stop all:")
    command = input("Enter a number between -1.0 to 1.0:")
    command = float(command)

    if pt == 'p':
        motor.pan(command)
    elif pt == 't':
        motor.tilt(command)
    elif pt == 'q':
        motor.pan(0.0)
        motor.tilt(0.0)
        break
    else:
        pt = input("Enter 'p' for pan or 't' for tilt or 'q' to stop all:")



