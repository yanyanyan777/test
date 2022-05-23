for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            sum = i * j
            print("{}*{}={}\t".format(i, j, sum), end=" ")
        j += 1
    i += 1
    print(" ")