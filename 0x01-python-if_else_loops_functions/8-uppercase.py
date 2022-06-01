def uppercase(str):
    for ch in range(len(str)):
        if ord(str[ch]) >= 97 and ord(str[ch]) <= 122:
            dif = 32
        else:
            dif = 0
    print("{:c}".format(ord(str[ch])-dif), end='')
    print()
