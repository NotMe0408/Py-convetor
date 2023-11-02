print("welcome to py convertor by notme0408")
print("enter the physical quantity want to convert")
quantity = input()
print("enter the unit u want to convert from")
unit = input()
print("enter the unit u want to convert to")
unit2 = input()
print("enter the value")
value = float(input())
if quantity == "length":
  if unit == "mm" and unit2 == "cm":
    print(value/10)
  elif unit == "cm" and unit2 == "mm":
    print(value*10)
  elif unit == "cm" and unit2 == "m":
    print(value/100)
  elif unit == "m" and unit2 == "cm":
    print(value*100)
  elif unit == "m" and unit2 == "km":
    print(value/1000)
  elif unit == "km" and unit2 == "m":
    print(value*1000)
  elif unit == "km" and unit2 == "mi":
    print(value/1.609)
  elif unit == "mi" and unit2 == "km":
    print(value*1.609)
  elif unit == "mi" and unit2 == "km":
    print(value/1.609)
elif quantity == "mass":
  if unit == "kg" and unit2 == "g":
    print(value*1000)
  elif unit == "g" and unit2 == "kg":
    print(value/1000)
  elif unit == "g" and unit2 == "lbs":
    print(value/453.6)
  elif unit == "lbs" and unit2 == "g":
    print(value*453.6)
  elif unit == "lbs" and unit2 == "kg":
    print(value/2.205)
  elif unit == "kg" and unit2 == "lbs":
    print(value*2.205)
elif quantity == "time":
  if unit == "s" and unit2 == "ms":
    print(value*1000)
  elif unit == "ms" and unit2 == "s":
    print(value/1000)
  elif unit == "ms" and unit2 == "min":
    print(value/60)
  elif unit == "min" and unit2 == "ms":
    print(value*60)
  elif unit == "min" and unit2 == "h":
    print(value/60)
  elif unit == "h" and unit2 == "min":
    print(value*60)
elif quantity == "temperature":
  if unit == "c" and unit2 == "f":
    print(value*9/5+32)
  elif unit == "f" and unit2 == "c":
    print((value-32)*5/9)
  elif unit == "c" and unit2 == "k":
    print(value+273.15)
  elif unit == "k" and unit2 == "c":
    print(value-273.15)
  elif quantity == "volume":
   if unit == "l" and unit2 == "ml":
    print(value*1000)
   elif unit == "ml" and unit2 == "l":
    print(value/1000)
  elif unit == "l" and unit2 == "gal":
    print(value/3.785)
elif quantity == "speed":
  if unit == "km/h" and unit2 == "m/s":
    print(value/3.6)
  elif unit == "m/s" and unit2 == "km/h":
    print(value*3.6)
  elif unit == "km/h" and unit2 == "mi/h":
    print(value/1.609)
  elif unit == "mi/h" and unit2 == "km/h":
    print(value*1.609)
  elif unit == "km/h" and unit2 == "mph":
    print(value/1.609)
  elif unit == "mph" and unit2 == "km/h":
    print(value*1.609)
  elif unit == "km/h" and unit2 == "fps":
    print(value/3.6)
  elif unit == "fps" and unit2 == "km/h":
    print(value*3.6)
  elif unit == "km/h" and unit2 == "knot":
    print(value/1.852)
elif quantity == "force"
 if unit == "N" and unit2 == "lbf":
  print(value*0.2248)
 elif unit == "lbf" and unit2 == "N":
   print(value/0.2248)
  elif unit == "N" and unit2 == "kgf":
   print(value/4.448)
  elif unit == "kgf" and unit2 == "N":
   print(value*4.448)
  elif unit == "N" and unit2 == "kN":
   print(value/1000)
  elif unit == "kN" and unit2 == "N":
   print(value*1000)
  elif unit == "N" and unit2 == "MN":
   print(value/1000000)  
else:
  print("ufffff")
