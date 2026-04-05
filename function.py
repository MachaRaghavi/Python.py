#Functions
def new_fun():
 print("I am RAGHAVI MACHA")
new_fun()  #calling function

#returning the function 
def my_fun():
  return("Have a good day")
Message=my_fun()
print(Message)

#Arguments 
def add(numbers):
 print(numbers+10)
add(2)
add(14)

#Default values
def my_fun(car="BMW"):
 print("My fav car is:",car)
my_fun("Benz")
my_fun("SUV")
my_fun()

#using *args (we can define as many number of arguments)
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)
my_function("Hello", "Raji", "Dinesh", "Likitha")

#using keyword argument
def personal_details(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print( key + ":", value)
personal_details("dinesh veeramallu", father_name="Ravindhar",age=20,study="Btech" )

  
