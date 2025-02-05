from machine import Pin, PWM

# import keyboard

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

speed = 0.25

while True:
    command = input("Enter a directional key: ")

    if command == 'a':
        duty_cycle_09 = 65535 * speed
        duty_cycle_10 = 0

        pwm_09.duty_u16(round(duty_cycle_09))  # Left
        pwm_10.duty_u16(round(duty_cycle_10))  # Right

    elif command == 'd':
        duty_cycle_10 = 65535 * speed
        duty_cycle_09 = 0

        pwm_09.duty_u16(round(duty_cycle_09))  # Left
        pwm_10.duty_u16(round(duty_cycle_10))  # Right

    elif command == 'w':
        duty_cycle_12 = 65535 * speed
        duty_cycle_13 = 0

        pwm_12.duty_u16(round(duty_cycle_12))  # Up
        pwm_13.duty_u16(round(duty_cycle_13))  # Down

    elif command == 's':
        duty_cycle_13 = 65535 * speed
        duty_cycle_12 = 0

        pwm_12.duty_u16(round(duty_cycle_12))  # Up
        pwm_13.duty_u16(round(duty_cycle_13))  # Down

    elif command == 'x':  # STOP ALL MOTORS
        duty_cycle_09 = 0
        duty_cycle_10 = 0
        duty_cycle_12 = 0
        duty_cycle_13 = 0

        pwm_09.duty_u16(round(duty_cycle_09))  # Left
        pwm_10.duty_u16(round(duty_cycle_10))  # Right
        pwm_12.duty_u16(round(duty_cycle_12))  # Up
        pwm_13.duty_u16(round(duty_cycle_13))  # Down

    else:
        print("Enter 'a' 'd' 'w' 's' 'x' or 'q'")
        continue


