print("Enter Date of Birth!(dd/mm/yyyy)")
d1 = int(input("Enter your Day: "))
d2 = int(input("Enter your Month: "))
d3 = int(input("Enter your Year: "))

print("Enter Your Disired Date!(dd/mm/yyyy)")
c1 = int(input("Enter  Day: "))
c2 = int(input("Enter Month: "))
c3 = int(input("Enter Year: "))

#Day
d = c1 - d1
if (d>0):
    dy=d
elif c2 in (1,3,5,7,8,10,12):
    dy = d + 31
elif c2 in (4,6,9,11):
    dy = d + 30
elif (c2 == 2):
    if c3 % 400 == 0:
        dy = d + 29
    elif c3 % 4 == 0 and c3 % 100 != 0:
        dy = d + 29
    else:
        dy = d + 28
#Year
if(c3 > d3):
    yr = c3-d3
else:
    print("Invalid!")

#Month
if(d < 0):
    c2 = c2-1
    if c2 < d2:
        c2 =  c2 + 12
        m = c2 - d2
        yr = yr - 1
    else:
        m = c2 - d2
elif(d >= 0):
    if c2 < d2:
        c2 =  c2 + 12
        m = c2 - d2
        yr = yr - 1

print("Your calculated desired age is",dy,"Day",m,"Month",yr,"Year!")