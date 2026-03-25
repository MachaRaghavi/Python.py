input values for datatypes.
a=input("Enter your name:") #strings
#integers
b=int(input("Enter your Age:"))
#float values
c=float(input("Enter your salary:"))
#List
d=list(map(int,input("Enter your fav numbers:").split()))
e=input("Enter your fav colours:").split()
#tuple
f=tuple(map(int,input("Enter your values:").split()))
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
