with open('input2.txt', 'r') as f:
  input = f.read()

inp = list(map(str, input.split("\n")))

#print(inp)

hpos = 0
vpos = 0
aim = 0
depth = 0
numbers = []
dirs = []

for x in inp:
  for word in x.split(" "):
    #print(word)
    if word.isdigit():
      numbers.append(int(word))
    else:
      dirs.append(word)

for x in range(len(inp)):
  if dirs[x] == "forward":
    hpos = hpos + numbers[x]
    depth = depth + (aim * numbers[x])
  elif dirs[x]== "up" :
    aim = aim - numbers[x]
  else: 
    aim = aim + numbers[x]
  # print(x)
  # print(vpos)
  # print(depth)
  # print(aim)
  
final = depth * hpos
print(depth)
print(hpos)
print(final)