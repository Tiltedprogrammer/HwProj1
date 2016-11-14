n = int(input("Вывод простых чисел до числа(включительно): ")) +1
vsechisla = [True for i in range(n)]
for x in range(2,n):
	for j in range(x * 2,n,x):
		vsechisla[j] = False
prostyechisla =[i for i in range(2,n) if vsechisla[i]]
print(prostyechisla)		


