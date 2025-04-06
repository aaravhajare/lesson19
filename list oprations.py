a = [1 , 2 ,3 ,4 ,5 ,6, 7, 8,]
print(a)

count = 0

for i in a:
    count += i
    
print(count)

avg = count / len(a)

print(avg)

a.sort()

print(a)

print("first",  a[0])

print("last" , a[-1])