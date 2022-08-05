import random
rd_list= []

n = int (input("Enter the number:\n"))
a_bazeh = 1 # هر عددی برای تولید تصادفی از بازه آ تا ب
b_bazeh = 30
while n > 0:
    rd_nums = random.randint(a_bazeh,b_bazeh)
    while rd_nums in rd_list:
        rd_nums = random.randint(a_bazeh,b_bazeh)
    while rd_nums not in rd_list:
        rd_list.append(rd_nums)
    n = n-1
    a = list(set(rd_list))
rd_list.sort()#لیست تصادفی مرتب
print (rd_list)