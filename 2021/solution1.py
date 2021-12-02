with open('input1.txt', 'r') as f:
  input = f.read()

inty = list(map(int, input.split()))

init = 0
count = 1
third = 2
sets = [0, 1, 2, 3, 4, 5]
morethan = 0 

for x in inty:
  firstTrip = inty[init] + inty[count] + inty[third]
  secondTrip = inty[init+1] +inty[count+1] + inty[third+1]
  print(firstTrip)
  print(inty[count])
  if firstTrip > secondTrip:
    morethan = morethan + 1
  if third + 3 != (len(inty) - 1):
    init = init + 1
    count = count + 1
    third = third + 1

print(morethan)
