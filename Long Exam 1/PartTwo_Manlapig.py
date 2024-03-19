'''
Print a title for your program. Include your name and a short description of your program.
'''

print("DIRECT LEVEL COMPUTER")
print("Peter John Manlapig")
print("This program solves direct levelling computations.")

import math

def floatInput():
    '''
    Input function

    Input
    BS reading 
    FS reading 
    HI
    Elev

    Output
    float data type
    '''

    backsight = elev_turn_point + height_of_instrument

    return backsight

BS_Reading = floatInput(backsight)
FS_Reading = floatInput(foresight)
height_of_instrument = backsight - elev_turn_point
# print(BS_Reading)

'''
Idedefine yung mga variables na gagamitin for leveling computation
'''
# backsight = ()
# foresight = ()
# height_of_instrument = ()
# elev_turn_point = ()
# levelling_table = [(backsight), (foresight), (height_of_instrument), (elev_turn_point)]

tp_counter = 1
lines = []
total_distance = 0
height_of_instrument = 0

while True: 
    print()
    print("TP No. ", tp_counter)

    distance = input("Distance: ")
    azimuth = input("Azimuth from South: ")

    elev_turn_point = floatInput()
    backsight = floatInput(=float())
    foresight = floatInput(=float())

    line = (tp_counter, BS_Reading, height_of_insrument, FS_Reading, elev_turn_point)
    lines.append(line)

    yn = input("Add New Turning Point? ")
    if yn.lower() == "yes" or yn.lower()  == "y":
        tp_counter = tp_counter + 1
        continue
    else:
        break

print("\n")
'''
Ipiprint yung guide table
push
'''
print('{: ^10} {: ^15} {: ^25} {: ^15} {: ^15}' .format ("STATION", "BACKSIGHT", "INSRUMENT HEIGHT", "FORESIGHT", "ELEVAION"))
for line in lines:
    print( '{:^10} {: ^15} {: ^25} {: ^15} {: ^15}'.format(line[0], line[1], line[2], line[3], line[4]))

