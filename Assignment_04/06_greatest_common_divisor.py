n = int(input("Enter the first number:\n"))
m = int(input("Enter the second number:\n"))
n_array = []
m_array = []
big_array = []
final_array = []
for i in range (1,n+1):
    if n%i == 0:
        n_array.append(i)
    i+=1
for j in range (1,m+1):
    if m%j == 0:
        m_array.append(j)
    j+=1
big_array = n_array + m_array

for k in big_array:
    if (k in m_array) and (k in n_array):
        final_array.append (k)
    else:
        k=k+1    
gcd= max(final_array)
print (f"Greatest common divisor is: {gcd}")
