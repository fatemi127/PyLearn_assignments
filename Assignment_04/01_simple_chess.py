n = int (input("N?\n"))
m = int (input("M?\n"))


for i in range (n):
    for j in range (m):
        if i % 2 == 0:
            print ('*',end='')
        else:
            print ('#',end='')
        i-=1
    print ('\n')
    

