Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> total = int(input())

num = int(input())

sum = 0

for i in range(num):
  a,b = map(int,input().split())
  sum += a*b

if total == sum: 
  print("Yes")
else: 
  print("No")