#for loop
colours=["red","blue","white","Black"] 
for x in colours:
 print(x)
for x in  "white":
 print(x)

#break statement 
for x in colours:
 if x=="blue":
  break
 print(x)

#continue 
for x in colours:
 if x=="white":
  continue 
print(x)

#range
for x in range(2,20):
 print(x)

#else in for loop
for x in range(6):
 print(x)
else:
 print("Finished")
