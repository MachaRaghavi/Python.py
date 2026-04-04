match statement 
fav_day=5
match fav_day:
 case 1:
  print("Monday")
 case 2:
  print("Tuesday")
 case 3:
  print("Wednesday")
 case 4:
  print("Thursday")
 case 5:
  print("Friday")
 case _: 
  print("Day not found")

#Combine values
day=3
match day:
 case 1|2|3|4:
  print("My favourite day")
 case 5|6|7:
  print("My weekend days")

#using if statement 
day=1
month=8
match day:
 case 1|2|3|4 if month==4
  print("My favourite day")
 case 5|6|7 if month==5
  print("My weekend days")
 case _:
  print("No match")

