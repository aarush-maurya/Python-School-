for i in range(5, 0, -1):
    if i%2 == 0:
        for j in range(i):
            print(1, end = "")
    else:
        for j in range(i):
            print(0, end = "")
    print()

# 00000
# 1111
# 000
# 11
# 0