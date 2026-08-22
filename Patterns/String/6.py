s = "ABCDE"
for i in range(1, 6):
    for j in s[:i]:
        print(j, end="") #Normal Jindagi
    print()

# A
# AB
# ABC
# ABCD
# ABCDE