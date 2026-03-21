#Global variables
x,y=5,6
def mul():
  print("Multiplication of numbers is:",x*y) #inside function
mul()
print("Multiplication of numbers is:",x*y)  #outside function

# using global keyword
x="raghavi"
def func():
 global x
 print("Name is:"+x)
func()
# variable inside the function
def my():
 global x
 x="Raghavi"
 print("Name is:"+x)
my()
print("Name is :"+x)
 
