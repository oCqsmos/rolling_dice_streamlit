import streamlit as st

import random

class RollDice:
    def __init__(self):
        self.PluMinDict1 = {'plus':[], 'minus':[]}
        # self.PluMinDict2 = {'plus':[], 'minus':[]}
        self.additions = []
        self.subtractions = []

        self.AddTemp = []
        self.SubTemp = []
        self.PlusValues = []
        self.MinusValues = []
        self.PlusRolls = []
        self.MinusRolls = []
        

    def DiceRollsFunction(self, dieCount):  # ie. diecount = '2d6'
        rolls=[]
        if 'd' in dieCount:
            temporary=dieCount.split('d')
            # print(temporary)
            
            temporary[0],temporary[1] = int(temporary[0]),int(temporary[1])
            # print(temporary)

            for i in range(0,temporary[0]):
                rolls.append(random.randint(1,temporary[1]))
        else:
            rolls.append(int(dieCount))

        rollsResult = 0
        for i in rolls:
            rollsResult+=i

        # print(rolls, rollsResult)

        return [rolls, rollsResult]

    def roll_request(self,Query):
        # PluMinDict1={'plus':[], 'minus':[]}
        if '+' in Query:
            self.additions = Query.split('+')

            for i in self.additions:
                if '-' not in i:
                    self.PluMinDict1['plus'].append(i)
                else:
                    self.subtractions = i.split('-')
                    
                    for r in range(1,len(self.subtractions)):
                        self.PluMinDict1['minus'].append(self.subtractions[r])
                    self.PluMinDict1['plus'].append(self.subtractions[0])
                    
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
            self.subtractions = Query.split('-')

            for i in range(1,len(self.subtractions)):
                self.PluMinDict1['minus'].append(self.subtractions[i])
            self.PluMinDict1['plus'].append(self.subtractions[0])
            # PluMinDict1['plus'].append(Query)
        else:
            self.PluMinDict1['plus'].append(Query)

        # PluMinDict2 = {'plus':[], 'minus':[]}
        self.getting_values()

    def getting_values(self):
        self.AddTemp = []
        self.SubTemp = []

        for i in range(0, len(self.PluMinDict1['plus'])):
            self.AddTemp.append(self.PluMinDict1['plus'][i])
        for i in range(0, len(self.PluMinDict1['minus'])):
            self.SubTemp.append(self.PluMinDict1['minus'][i])

        # print(AddTemp)
        # print(SubTemp)

        self.PlusResults = []
        self.MinusResults = []

        PlusValues = []
        MinusValues = []

        PlusRolls = []
        MinusRolls = []

        for i in self.AddTemp:
            self.PlusResults.append(self.DiceRollsFunction(i))
            # if 'd' in i:
            #     self.PlusResults.append(self.DiceRollsFunction(i))
            # else:
            #     # self.PlusResults.append(int(i))
            #     self.PlusValues.append(int(i))
            #     self.PlusRolls.append(int(i))
        for i in self.SubTemp:
            self.MinusResults.append(self.DiceRollsFunction(i))
            # if 'd' in i:
            #     self.MinusResults.append(self.DiceRollsFunction(i))
            # else:
            #     # self.MinusResults.append(int(i))
            #     self.MinusValues.append(int(i))
            #     self.MinusRolls.append(int(i))

        # print(PlusResults)
        # print(MinusResults)

        PlusValues = [i[1] for i in self.PlusResults]
        MinusValues = [i[1] for i in self.MinusResults]

        PlusRolls = [i[0] for i in self.PlusResults]
        MinusRolls = [i[0] for i in self.MinusResults]

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

        # print("recorded positive rolls:     ", end='') 
        # print(TruePlusRolls)
        slot_positive.write('recorded positive rolls: '+ str(TruePlusRolls))
        # print("recorded negative roles:     ", end='')
        # print(TrueMinusRolls)
        slot_negative.write('recorded negative rolls: '+ str(TrueMinusRolls))
        # print("final roll result:     ", end='')
        # print(FinalValue)
        slot_final_result.write('final value: '+ str(FinalValue))



diceroller = RollDice()
# diceroller.roll_request(input('enter roll request'))


# date_input = st.text_input("Enter a date in the format yyyymm.dd",value="sample date: 202410.26")
roll_input = st.text_input("Enter a roll request, the amount of die followed by the number of sides, for multiple die do not include spaces and seperate using '+' and '-'", value="sample entry --> 2d12+2d6-1d4")

slot_positive = st.empty()
slot_negative = st.empty()
slot_final_result = st.empty()

if st.button("click to roll"):
    diceroller.roll_request(roll_input)