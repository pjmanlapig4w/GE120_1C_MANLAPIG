'''
Create a model of a class that defines a parcel of land.
'''

class Parcel:
    def __init__(self, owner, area):
        self.owner = owner
        self.area = area
    
    def getClassification ():
        """
        if the size of lot is less than 1 hectare
        Residential

        if the size of lot is between 1 hectare and 12 hectares
        Private Agricultural
        """
        if  area > 0 < 10000:
            area = 'Residential' .format ()
        elif area > 10000 < 120000:
            area = 'Private Agricultural' .format ()
        
        else:
            area = "Public Agricultural"

        return area
    

# print ("A parcel of land owned by",self.owner  "with an area of", self.area  "square meters")

# ("Consolidated lot of <self.owner> and <other.owner> with a total area of <sum of two lot areas> square meters")

class Riparian:
    def __init__(self, owner, area, type):
        self.owner = owner
        self.area = area
        self.type = type

    
    def getAdjoiningWaterbody(type):
        if  type == 1:
            type = 'Adjacent to River - can be subject to tilting' .format ()
        elif type == 2:
            type = 'Adjacent to Ocean (Litoral) - cannot be subject to tilting' .format ()
        
        else:
            type = "Invalid Riparian Parcel"

        return type

        
       