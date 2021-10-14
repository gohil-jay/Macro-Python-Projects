  #meter to feet and inches

print("This program will convert a height given meters to a height given in feet and inches.")
meters = float(input("Enter height in meters:"))
meters_in_ft = meters // .3048
meters_in_in = meters_in_ft % 12
print("The height is", meters_in_ft,"feet and",meters_in_in, "inches")
