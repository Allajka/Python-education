a = int(input('a = '))
b = int(input('b = '))
if a > b:
    print(a, "больше", b)
else:
    print(b, "больше", a)

holiday = False
temperature = -28
temperatureLimit = -27
age = 8
ageLimit = 12

if holiday == True:
  print ("go to friends")
elif temperatureLimit < temperature:
  print ("go to school")
elif age > ageLimit:
  print ("need to go to school")
else:
  print ("sit at home")

