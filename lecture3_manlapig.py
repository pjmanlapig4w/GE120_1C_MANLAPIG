"""
GE120 Intro to OOP Geomatic Application
Lecture 3
Peter John Manlapig
2023-21040
"""

# list = [123, 'abcd', 10.2, 'd']
# list1 = ['hello', 'world']

# print (list)
# print (list [1])
# print (list1 * 2)
# print (list + list1)

# # LISTS
# listahan = ["mafe", "justin", "mika", "uste"]
# print(listahan)

# # gusto si mika makuha (position)
# print(listahan[2])

# # subset of the list, mafe and si justin
# print(listahan[0:2])

# print(listahan[1:3])

# # nagstastart sa simula
# print(listahan[3])

# # start from index, end sa dulo
# print(listahan[2:])

# print(listahan[-1])

# # gets first item, last item, then those in between
# print(listahan[-3:3])

# # Addition 

# listahan[0] = "chelzy"

# #TUPLES
# tuple_1 = ("maja", "gianna", "jewel")
# print(tuple_1)

# # tuples are immutable
# # tuple_1 = "quinmar"

# # NESTED LISTS
# list_1 = [ ["apple", "bola", "carton"], ["apricot", "banana", "cow"]]
# print(list_1[0][2])

# # NESTED TUPLES
# tuple_2 = ((12.1244, -12.1244),(35.46261,-67.1231),(123.124, 56.232))
# print(tuple_2[2][0])

# # DICTIONARIES - key value pairs
# dog = {"name": "Bogart", "age": 2, "color": "white", "favorite_num": 3.14, 1: 45 }
#         # pwede si number as key (float or int)

# print(dog[1]) 
# print(dog.values()) #returns a list of values
# print(dog.keys()) #returns a list of keys

# dog["favorite_num"] = 39

# print(dog["favorite_num"]) 

# score = (99)
# print (score)

# if score >= 92:
#     print ('Passed with flying colors')

# elif score >= 60:
#     print ('passed')

# else:
#     print ('Failed')


# i = 0
# while 1==1:
#        print (i)
#        i += 1
#        if  i >= 5:
#         print ('breaking...')
#         break
# print ('Loop Exit')

# LOOPS AND BREAK CONTINUE AND PASS 

# for number in range (10):
#     if number == 5:
#         print (number)


rec = 100
while rec < 5000:
    rec = int(input ('enter REC: '))
    kulang = 5000 - rec
    if rec >= 4500:
        pass
    print("kulang ka ng Rec na", kulang)

print ('PASOK NA REC')
print ("-----end----")


    