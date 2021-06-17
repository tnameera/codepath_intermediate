def multiple(n):
    sum = 0
    for i in range(1,n,1):
        if (i % 3 == 0):
            #print(i)
            sum = sum + i
        elif( i % 5 == 0):
            #print(i)
            sum = sum + i
    return(sum)

print(multiple(1000))
    