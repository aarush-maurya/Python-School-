for i in range(5, 0, -1):
    if i%2 == 0:
        for j in range(i):
            print(0, end = "")
    else:
        for j in range(i):
            print(1, end = "")
    print()

# 11111
# 0000
# 111
# 00
# 1