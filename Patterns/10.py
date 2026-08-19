n = 1
for i in range(5):
    if i % 2 == 0:
        for j in range(5):
            print(n, end ="")
            if n == 1:
                n = 0
            elif n == 0:
                n=1
    else:
        print("00000", end = "")
    print()

# 10101
# 00000
# 01010
# 00000
# 10101