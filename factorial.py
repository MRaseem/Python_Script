a=int(input("Enter the Factorial Number"))
#print Enter the factorial
if a==0 or a==1:
  print("1")
else:
  def factorial(a):
    s=1
    for i in range(1,a+1):
      s=s*i
    print(s)
  factorial(a)
