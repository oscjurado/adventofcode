with open('input33.txt', 'r') as f:
  input = f.read()

bitlist = input.split("\n")

onecounts = list(range(0,12))
zerocounts = list(range(0,12))
base = [1,0,1,1,1,1,1,1,1,1,0,1]

for lines in bitlist:
  for index in range(len(lines)):
    bit = lines[index]
    if bit == "1":
      onecounts[index] += 1
    else:
      zerocounts[index] += 1
    #if bit[index] != base[index]:
      #bitlist.pop()
    #print(bit, index, lines)

for index in range(len(bitlist)):
  #print(index, bitlist[index])
  for char in bitlist[index]:
    if char != base[index]:
      print(bitlist[index])

#for lines in bitlist:




#print(onecounts)
#print(zerocounts)


  

