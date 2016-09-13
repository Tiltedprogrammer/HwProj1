n = int(input("Вывод простых числе до числа(включительно): ")) +1
vsechisla = [True for i in range(n)]
for x in range(2,n):
	for j in range(x * 2,n,x):
		a[j] = False
prostyechisla =[i for i in range(2,n) if a[i]]
print(b)		


