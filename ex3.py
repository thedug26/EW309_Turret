import serial

while True:
    num_list = []
    while True:
        num = input('Type numbers to put in a list. Press "q" to quit. (run thonny idiot) ')
        if num == 'q':
            break
        else:
            print(num)
            num_list.append(num)
            print(num_list)
    num_str = ','.join(num_list)
    num_byte = num_str.encode('utf-8') # encodes to bytes

    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = 'COM9'
    ser.open()

    msg_1 = num_byte+b"\n" # DONT FORGET \n
    ser.write(msg_1)

    sum_stats = ser.readline()
    sum_stats = sum_stats.decode('utf-8')
    int_list = [float(x) for x in sum_stats.split(',')]
    print(int_list)

    stop = input('To stop press "x" or type anything else to do it again: ')
    if stop == 'x':
        quit_msg = b"x\n" # Why do we use bytes? -
        ser.write(quit_msg)
        break
    else:
        continue
