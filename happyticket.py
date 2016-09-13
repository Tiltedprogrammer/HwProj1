count = 0
for i in range(10):
	for j in range(10):
		for g in range(10):
			for m in range(10):
				for n in range(10):
					for p in range(10):
						if i+j+g == m+n+p:
							count+=1
print(count)	