from machine import Pin, PWM
# a - left ; d - right; 'w' - up; 's' - down; q - quit
import ttyacm
from bno055 import *
import time

tty = ttyacm.open(1)

i2c = machine.I2C(1, sda=machine.Pin(2), scl=machine.Pin(3))  # EIO error almost immediately
imu = BNO055(i2c)
calibrated = False

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
            pwm_10.duty_u16(round(65535 * -1 * speed))  # Right

    def tilt(self, speed):
        if 0.0 < speed <= 1.0:
            pwm_12.duty_u16(round(0))  # Up
            pwm_13.duty_u16(round(65535 * speed))  # Down

        elif -1.0 <= speed < 0.0:
            pwm_12.duty_u16(round(65535 * -1 * speed))  # Up
            pwm_13.duty_u16(round(0))  # Down

        elif speed == 0.0:
            pwm_12.duty_u16(round(0))  # Up
            pwm_13.duty_u16(round(0))  # Down


motor = PanTiltDriver(freq)
angles = []
yaw = []
pitch = []
times = []
total_time = 0
clock = []
previous_yaw = 0
previous_pitch = 0
while True:
    msg = tty.readline()
    num = msg
    if msg == 'x':
        start_time = time.time()
        while total_time <= 5:
            time.sleep(0.1)
            if not calibrated:
                calibrated = imu.calibrated()
                print('Calibration required: sys {} gyro {} accel {} mag {}'.format(*imu.cal_status()))
                calibrated = True
            print('Yaw {:4.0f}; Pitch {:4.0f}'.format(*imu.euler()))
            yawL, pitchL, rollL = imu.euler()
            # yaw.append(yawL)
            # pitch.append(pitchL)
            # print(imu.euler())
            # print(yaw)
            # print(pitch)
            # print(roll)
            # angles.append(imu.euler())
            # print(angles)

            # velocities
            yaw.append(yawL - previous_yaw)
            pitch.append(pitchL - previous_pitch)

            # motor.pan(-1.0)
            motor.tilt(-1.0)

            end_time = time.time()
            total_time = end_time - start_time
            previous_yaw = yawL
            previous_pitch = pitchL
    # motor.pan(0.0)
    motor.tilt(0.0)
    # print(yaw)
    # tty.print(yaw)
    print(pitch)
    tty.print(pitch)




