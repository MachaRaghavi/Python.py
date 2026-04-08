#Lambda expression
add=lambda x,y:x+y
print(add(40,22))

#lambda functions
def my_fun(n):
 return lambda x:x*n
my_val=my_fun(6)
print(my_val(8))

#lambda with build functions
num=[1,2,3,4,5,6,7,8]
value=list(map(lambda x:x*3,num))
even-val=list(filter(lambda x:x%2==0,num))
names=["kunna","dinnu","likky","divi"]
sorted_list=sorted(names, key=lambda x:x)
print(value)
print(even_val)
print(sorted_list)
