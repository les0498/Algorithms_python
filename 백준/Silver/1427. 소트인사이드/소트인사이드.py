numbers = list(map(int,str(input())))

numbers.sort(reverse=True)

for i in numbers:
  print(i,end="")