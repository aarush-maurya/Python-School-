n = 15
for i in range(1, 6):
    for j in range(i):
        print(f"{n : <2}", end=" ")
        n-=1
    print()

# 15 
# 14 13 
# 12 11 10 
# 9  8  7  6  
# 5  4  3  2  1  