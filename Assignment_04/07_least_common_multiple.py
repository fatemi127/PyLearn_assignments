n = int(input("Enter the first number:\n"))
m = int(input("Enter the second number:\n"))
multi = n*m
n_array = []
m_array = []
big_array = []
final_array = []
for i in range (1,multi+1):
    if i%n == 0:
        n_array.append(i)
    i+=1
for j in range (1,multi+1):
    if j%m == 0:
        m_array.append(j)
    j+=1
big_array = n_array + m_array
for k in big_array:
    if (k in m_array) and (k in n_array):
        final_array.append (k)
    k=k+1    
lcd= min(final_array)
print (f"Least common multiple is: {lcd}")
