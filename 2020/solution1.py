with open('input1.txt', 'r') as f:
  input = f.read()

listy1 = list(map(int, input.split()))

def sol(listy): 
	for i in listy:
		for y in listy:
			for z in listy:
				if i + y + z == 2020:
					print(i * y * z)
					return i * y * z

sol(listy1)