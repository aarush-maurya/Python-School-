s = "ABCDEFGHIJKLMNOPQRSTUVWXY"
for i, c in enumerate(s, 1):
    print(c, end="")
    if i%5==0:
        print()

# ABCDE
# FGHIJ
# KLMNO
# PQRST
# UVWXY