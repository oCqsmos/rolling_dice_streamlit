import streamlit as st
import pandas as pd
import numpy as np

import random

def DiceRollsFunction(dieCount):
    temporary=dieCount.split('d')
    # print(temporary)
    rolls=[]
    temporary[0],temporary[1] = int(temporary[0]),int(temporary[1])
    # print(temporary)

    for i in range(0,temporary[0]):
        rolls.append(random.randint(1,temporary[1]))

    rollsResult = 0
    for i in rolls:
        rollsResult+=i

    # print(rolls, rollsResult)

    return [rolls, rollsResult]

# for i in range(0,20):
#     DiceRollsFunction('2d12')



Query = input('enter roll request \n')  #change this to an input('enter roll request')


PluMinDict1={'plus':[], 'minus':[]}
if '+' in Query:
    additions = Query.split('+')

    for i in additions:
        if '-' not in i:
            PluMinDict1['plus'].append(i)
        else:
            subtractions = i.split('-')
            
            for r in range(1,len(subtractions)):
                PluMinDict1['minus'].append(subtractions[r])
            PluMinDict1['plus'].append(subtractions[0])
            
            # subtractions = i.split('-')
            # if len(subtractions) > 1:
            #     for r in range(1,len(subtractions)):
            #         PluMinDict1['minus'].append(subtractions[r])
            #     PluMinDict1['plus'].append(subtractions[0])
            # else:
            #     PluMinDict1['minus'].append(subtractions[0])


    # PluMinDict1['plus'].append(additions[0])
    # print(PluMinDict1)
elif '-' in Query:
    subtractions = Query.split('-')

    for i in range(1,len(subtractions)):
        PluMinDict1['minus'].append(subtractions[i])
    PluMinDict1['plus'].append(subtractions[0])
    # PluMinDict1['plus'].append(Query)
else:
    PluMinDict1['plus'].append(Query)

PluMinDict2 = {'plus':[], 'minus':[]}


AddTemp = []
SubTemp = []

for i in range(0, len(PluMinDict1['plus'])):
    AddTemp.append(PluMinDict1['plus'][i])
for i in range(0, len(PluMinDict1['minus'])):
    SubTemp.append(PluMinDict1['minus'][i])

# print(AddTemp)
# print(SubTemp)

PlusResults = []
MinusResults = []

for i in AddTemp:
    PlusResults.append(DiceRollsFunction(i))
for i in SubTemp:
    MinusResults.append(DiceRollsFunction(i))

# print(PlusResults)
# print(MinusResults)

PlusValues = [i[1] for i in PlusResults]
MinusValues = [i[1] for i in MinusResults]

PlusRolls = [i[0] for i in PlusResults]
MinusRolls = [i[0] for i in MinusResults]

TruePlusRolls = []
for i in PlusRolls:
    for r in i:
        TruePlusRolls.append(r)
TrueMinusRolls = []
for i in MinusRolls:
    for r in i:
        TrueMinusRolls.append(r)


PlusFValue = 0
MinusFValue = 0
for i in PlusValues:
    PlusFValue += i
for i in MinusValues:
    MinusFValue += i

FinalValue = PlusFValue - MinusFValue

print("recorded positive rolls:     ", end='') 
print(TruePlusRolls)
print("recorded negative roles:     ", end='')
print(TrueMinusRolls)
print("final roll result:     ", end='')
print(FinalValue)

