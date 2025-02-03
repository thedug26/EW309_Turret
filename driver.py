from machine import Pin, PWM

# a - left ; d - right; 'w' - up; 's' - down; q - quit

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

    def drive(self, speed):
        if 0 < speed < 0.5:
            pwm_09.duty_u16(round(65535 * speed))  # Left
            pwm_10.duty_u16(round(0))  # Right

        elif 1 >= speed > 0.5:
            pwm_09.duty_u16(round(0))  # Left
            pwm_10.duty_u16(round(65535 * speed))  # Right

        elif speed == 0.5:
            pwm_09.duty_u16(round(0))  # Left
            pwm_10.duty_u16(round(0))

        elif -1.0 <= speed < -0.5:
            pwm_12.duty_u16(round(65535 * -1 * speed))  # Up
            pwm_13.duty_u16(round(0))  # Down

        elif 0 > speed > -0.5:
            pwm_12.duty_u16(round(0))  # Up
            pwm_13.duty_u16(round(65535 * -1 * speed))  # Down

        elif speed == -0.5:
            pwm_12.duty_u16(round(0))  # Up
            pwm_13.duty_u16(round(0))  # Down

        else:
            pwm_09.duty_u16(round(0))  # Left
            pwm_10.duty_u16(round(0))
            pwm_12.duty_u16(round(0))  # Left
            pwm_13.duty_u16(round(0))  # Right


motor = PanTiltDriver(freq)

while True:
    command = input(
        "Enter a number between 0.0 to 1.0 for pan and -1.0 to 0.0 for tilt: \n(0.5 will stop the pan; -0.5 will stop the tilt; 0 will stop all)")
    command = float(command)
    motor.drive(command)


