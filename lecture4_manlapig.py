"""
GE120 Intro to OOP Geomatic Application
Lecture 4
Peter John Manlapig
2023-21040
"""

# Funcion: because they uphold the DRY principle ( Don't Repeat Yourself)

# convert a number to a string 
# a=1
# b=str(a)
# print(type(b))

# Defining a function
# def shout(word):
#     # number = 2
#     number = 23

#     print(number)
#     print(word + "!")
#     # print("I created this funcion!")

# shout('Peter')
# shout('John')
# shout("Manlapig")

# x = 1

# def a():
#     x = 25
#     print("local x in a is", x, "afer entering a")
#     x += 1
#     print("local x in a is", x, "before exiting a")


# a()

# variables inside functions are not available globally
# print(word)

# use global variable if not in local parameters

# def shout(word1, word2):
#     print(word1+"!")
#     print(word2+".....")

# shout("mafe","peter")

# def shout(word1, list_of_names):
#     print(word1+"!")
#     print(list_of_names)

# shout("mafe", ["omar", "uste"])

# def shout(word1, num_ulit_last_letter):
#     '''
#     uulitin last letter
#     '''
#     print(word1.upper()+word1[-1].upper()*(num_ulit_last_letter-1)+"!!!!")
#     #  print(list_of_names)

# shout("mafe", 100)

def convertDMStoDEG(dms):
    '''
    Convert DMS to Degrees
    arguments dms - string
    '''

dms = 12-12-12
degrees, minutes, seconds = dms.split("-")
dd = int(degrees) + (int(minutes)/60) + (float(seconds)/3600)
