a = int(input())
b = int(input())
i = 0
if b == 0:
	print("Division by zero is not possible")
if (a >= 0 and b > 0) or (a <0 and b <0):
	while abs(a) >= abs(b):
		a-=b
		i+=1
if (a < 0 and b >0) or(a > 0 and b < 0):
	while abs(a) >= abs(b):
		a=abs(a)-abs(b)
		i -=1
print(i)		
