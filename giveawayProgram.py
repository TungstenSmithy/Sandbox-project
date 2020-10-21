#imports
import random

#variables and dictionaries
info = {
    'totalEntrees' : 0
}
secRange = {
    #Do not delete, variables will be added later
}
prekNum = {
    "prevNum" : 0
}
lowEntreeRange = {
}
#function
def makeEntree(name, numEntrees):
    
    #function execution
    info['totalEntrees'] = info['totalEntrees'] + numEntrees
    prekNum["prevNum"] = numEntrees + 1
    secRange[name] = numEntrees + info['totalEntrees'] - prekNum["prevNum"]
    lowEntreeRange[name] = info['totalEntrees'] - numEntrees
#Entrees
"""
Note: You have to manually add each entry. The first argument is the name of the enterer, and the 2nd argument is the number
of entrees that enterer entered.
"""


#Example entrees
makeEntree('Arknight444', 1000)
makeEntree('MightyWolf_', 2000)
makeEntree('BillyBobJoe', 1000)
makeEntree("Bobby", 2000)
makeEntree("Dan", 1000)

#Important Variables
pinkVar = info['totalEntrees']
randomNum = random.randint(0, pinkVar)

#Printing
"""
IMPORTANT: The first number displayed is the total number of entrees
The second number is the random number chosen
The third dictionary displayes each enterer's name and the last number of their range.
So each person's range is from the previous person's last number +1 to the number displayed next
to their name. Still working on display for winner.
"""
print('')
print('')
print(pinkVar)
print(secRange)
print(lowEntreeRange)
print(randomNum)
print(info)
print(prekNum)
#lol