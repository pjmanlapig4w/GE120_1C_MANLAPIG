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

lat = getLatitude(12, 45)
print(lat)

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

dep = getDeparture(12, 45)
print(dep)

def azimuthtoBearing