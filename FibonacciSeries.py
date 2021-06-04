n = int(input("Enter the value of n: "))
a,b = 0,1
sum, count = 0,1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  a,b,sum = b, sum, a+b