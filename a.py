a = [2.3,3.1,7.5,1.5,6.3]
a.sort()
num = 0
m = 0
for i in range(4):
	num = a[i+1]-a[i]
	if m < num:
		m =num
print(m)
