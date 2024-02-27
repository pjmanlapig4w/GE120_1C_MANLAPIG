"""
GE120 Intro to OOP Geomatic Application
Peter John Manlapig
2023-21040
"""


dms = 118.42069

# getting the degree part

degree = int(dms)

# getting the minute part 

minutes = (dms - degree) * 60

minutes_whole = int(minutes)

# getting the seconds

seconds = (minutes - minutes_whole) * 60


print("This is Bearing DMS: " + str(degree) + "-" + str(minutes_whole) + "-" + str(round(seconds,2)))

decimal = "118-25-14.48"
values = decimal.split("-")

degrees = int(values[0])
minutes = int(values[1])
seconds = float(values[2])

dd = degrees + (minutes/60) + (seconds/3600)

print("This is the Degree Decimal: " + str(round(dd,6)))
