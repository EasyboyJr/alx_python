
for i in range(10):
    for j in range(i +1, 10):
        if i+j == 89:
            print("{}{}".format(i, j), end="\n")
        else:
            print("{}{}".format(i, j), end=", ")-