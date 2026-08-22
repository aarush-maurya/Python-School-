n = 1

for i in range(1, 6):
    for j in range(n, n + 2*i - 1, 2):#i genuinely applied AP seq to find the range arg lmao
        print(j, end=" ")
    n+=2
    print()

# 1 
# 3 5 
# 5 7 9 
# 7 9 11 13 
# 9 11 13 15 17 