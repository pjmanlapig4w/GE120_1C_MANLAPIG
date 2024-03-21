"""
GE120 Intro to OOP Geomatic Application
Peter John Manlapig
2023-21040

Exercise 3
"""
import math
def getLatitude(distance, azimuth):
    '''
    compute for the latitude of the given line

    Input
    distance - float
    azimuth - float

    Output
    latitude - float
    '''

    latitude = -distance * math.cos(math.radians(azimuth))

    return latitude

# lat = getLatitude(12, 45)
# print(lat)

def getDeparture(distance, azimuth):
    '''
    compute for the latitude of the given line

    Input
    distance - float
    azimuth - float

    Output
    departure - float
    '''

    departure = -distance * math.sin(math.radians(azimuth))

    return departure

# dep = getDeparture(12, 45)
# print(dep)

def azimuthtoBearing(azimuth):
    '''
    Compute for the DMS bearing of the given angle

    input
    azimuth - float

    output
    bearing - string
    '''

    if "-" in str(azimuth): #if user gives DMS
        degrees, minutes, seconds = azimuth.split("-")
        azimuth = (int(degrees)) + (int(minutes)/60) + (float(seconds)/3600)%360
    else: #if user gives DD
        azimuth = float(azimuth)%360

    if azimuth > 0 and azimuth < 90:
        bearing = 'S {: ^10} W' .format (azimuth)
    elif azimuth > 90 and azimuth < 180:
        bearing = 'N {: ^10} W' .format (180 - azimuth)
    elif azimuth > 180 and azimuth < 270:
        bearing = 'N {: ^10} E' .format (azimuth - 180)
    elif azimuth > 270 and azimuth < 360:
        bearing = 'S {: ^10} E' .format (360 - azimuth)
    elif azimuth == 00:
        bearing = "DUE SOUTH"
    elif azimuth == 90:
        bearing = "DUE WEST"
    elif azimuth == 180:
        bearing = "DUE NORTH"
    elif azimuth == 270:
        bearing = "DUE EAST"
    else:
        bearing = "UNKNOWN"

    return bearing

# Create a sentinel controlled loop 
counter = 1
lines = []
sumLat = 0
sumDep = 0
sumDist = 0

while True: 
    print()
    print("LINE NO. ", counter)

    bobo_magtype = False
    while not(bobo_magtype):
        distance = input("Distance: ")
        if (bobo_magtype):
            print("Why so bobo magtype")
            continue
        if not(bobo_magtype):
            break

    azimuth = input("Azimuth from South: ")

    bearing = azimuthtoBearing(azimuth)
    lat = getLatitude(azimuth=float(azimuth), distance=float(distance))
    dep = getDeparture(azimuth=float(azimuth), distance=float(distance))

    sumLat += lat
    sumDep += dep
    sumDist += float(distance)

    constCorrLat = -(float(distance)/sumDist)*(sumLat)
    constCorrDep = -(float(distance)/sumDist)*(sumDep)
    
    corr_lat = constCorrLat*float(distance)
    corr_Dep = constCorrDep*float(distance)

    adjlat = lat + corr_lat
    adjDep = dep + corr_Dep

    line = (counter, distance, bearing, round(lat, -3), round(dep, -3), round(corr_lat, -3), round(corr_Dep, -3), round(adjlat, -3), round(adjDep, -3))
    lines.append(line)

    yn = input("Add New Line? ")
    if yn.lower() == "yes" or yn.lower()  == "y":
        counter = counter + 1
        continue
    else:
        break

print("\n\n")
print("------------------------------------------------------------------------------------------")
print('{: ^10} {: ^10} {: ^15} {: ^20} {: ^20}' .format ("LINE NO.", "DISTANCE", "BEARING", "LATITUDE", "DEPARTURE"))
for line in lines:
    print( '{: ^10} {: ^10} {: ^15} {: ^20} {: ^20}'.format(line[0], line[1], line[2], line[3], line[4]))

print("------------------------------------------------------------------------------------------")

print("\n\n")
print("------------------------------------------------------------------------------------------")
print('{: ^20} {: ^20} {: ^25} {: ^25}' .format ("LAT CORRECTION", "DEP CORRECTION", "ADJUSTED LATITUDE", "ADJUSTED DEPARTURE"))
for line in lines:
    print( '{: ^20} {: ^20} {: ^25} {: ^25}'.format(line[5], line[6], line[7], line[8]))
print("------------------------------------------------------------------------------------------")
print("\n\n")
print("SUMMATION OF LAT: ", sumLat)
print("SUMMATION OF DEP: ", sumDep)
print("SUMMATION OF DIS: ", sumDist)

lec = math.sqrt(sumLat**2 + sumDep**2)
print("\n")
print("------------------------------------------------------------------------------------------")
print("LEC: ", lec)

rec = sumDist/lec
print("1: ", rec)

print("\n")

print ("----------------------------------------END----------------------------------------------")