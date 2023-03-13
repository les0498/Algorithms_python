Dice_number = input().split(' ')
a = int(Dice_number[0])
b = int(Dice_number[1])
c = int(Dice_number[2])

if (a == b == c):
  print(10000 + a * 1000) 
elif (a == b or a == c): 
  print(1000 + a * 100)
elif (b == c): 
  print(1000 + b * 100)
else: 
  print(max(a, b, c) * 100)