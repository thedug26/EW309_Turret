import ttyacm

tty = ttyacm.open(1)
i = 0
sum_list = []
total = 0
while True:
    print("Reading data from MATLAB")
    msg = tty.readline()
    print(f"got: {msg}")
    if msg == 'x':
        break
    i += 1
    print(f'"i" is {i}')
    msg_contents = msg.split(',')
    nums = []
    # avg = 0
    total = 0

    for j in range(len(msg_contents)):
        num = msg_contents[j]
        num = float(num)
        nums.append(num)
        print(nums)
        total += num
    # avg = total
    # avg = avg/len(nums)
    # max_num = max(nums)
    # min_num = min(nums)
    total = total / i
    sum_list.append(total)

    for r in range(len(sum_list)):
        if r == 0:
            msg_back = f"{sum_list[0]}"
        else:
            msg_back += f",{sum_list[r]}"

    tty.print(msg_back)
