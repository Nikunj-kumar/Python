from math import sin, cos, atan2, sqrt, radians

R = 6373.0

latitude1 = float(input("Enter the first latitude: "))
longitude1 = float(input("Enter the first longitude: "))
latitude2 = float(input("Enter the second latitude: "))
longitude2 = float(input("Enter the second longitude: "))

latitude1 = radians(latitude1)
latitude2 = radians(latitude2)
longitude1 = radians(longitude1)
longitude2 = radians(longitude2)


print()
print("Calculating distnace between (", latitude1,',', longitude1,") and (", latitude2,',',longitude2,")")
print()

d_latitude = latitude2 - latitude1
d_longitude = longitude2 - longitude1

a = sin(d_latitude / 2)**2 + cos(latitude1) * cos(latitude2) * sin(d_longitude / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = R * c

print("Distance is ", distance)
