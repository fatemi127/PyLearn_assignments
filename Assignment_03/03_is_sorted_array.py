arr  = []
num = int(input ("What is the length of the array?\n"))
for i in range (num):
    n = int (input(f"Enter the number {i+1}\n"))
    arr.append(n)
if sorted(arr) == arr:
    print(f"Sorted array is: {arr}")
else:
    print (f"Unsorted array is:{arr}")