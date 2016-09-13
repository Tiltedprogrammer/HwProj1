stack = []
skobki = '(){}[]'
stroka = input()
for i in stroka:
	if i in skobki:
		if skobki.find(i) % 2 == 0:
			stack.append(i)
		elif skobki.find(i) % 2 != 0:
			if len(stack) == 0:
				print('Is not balanced')
			elif (stack.pop()+i) not in skobki:
					print('Is not balanced')
