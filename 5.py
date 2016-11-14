n = int(input("Введите длину первой части массива: "))
m = int(input("Введите длину второй части массива: "))
a = []
for i in range(n+m):
	a.append(input("Введите элемент массива"))
p = n-1 
v = 0
r = n-1
for i in range(n//2):
	v = a[i]
	a[i]=a[p]
	a[p]=v
	p-=1
for i in range(n,m//2+n):
	v=a[i]
	a[i]=a[r+m]
	a[r+m]=v
	r-=1
print(a[::-1])	

