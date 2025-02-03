import serial

ser=serial.Serial()

ser.baudrate=9600

msg_in="yo"

ser.write(msg_in)