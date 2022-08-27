num=int(input("Enter the number:\n"))
arr=[]
for i in range(num):
    arr.append([1]*(i+1))
        
for i in range(2,num):  
    for j in range(1,i):
        arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
for i in range(num):
    print (arr[i])
    i+=1
