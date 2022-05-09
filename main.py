inputArray = [1, 5, 3, 9, 9]  # Given array

hour, minute = 0, 0

for i in range(len(inputArray)):
    for j in range(len(inputArray)):
        if i == j:
            continue
        c = str(inputArray[i]) + str(inputArray[j])
        if 24 > int(c) > int(hour):
            hour = c
if hour == 0:
    print(-1)
else:
    inputArray.remove(int(hour[0]))
    inputArray.remove(int(hour[1]))
    for i in range(len(inputArray)):
        for j in range(len(inputArray)):
            if i == j:
                continue
            c = str(inputArray[i]) + str(inputArray[j])
            if 60 > int(c) > int(minute):
                minute = c
    if minute == 0:
        print(-1)
    else:
        print(hour, ":", minute)
