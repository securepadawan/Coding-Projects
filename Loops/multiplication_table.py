for row in range(1, 10):
    for col in range(1, 10):
        num = row * col
        if num < 10:
            empty = "  "
        else:
            if num < 100:
                empty  = " "
        print(empty, num, end = '')
    print()
