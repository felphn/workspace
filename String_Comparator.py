from time import sleep
from os import system


inputStr = ''

targetStr = ''

i = j = numOfMatch = 0
while i != len(inputStr):
    #sleep(.056)
    print(f'Comparing ...\n >{inputStr[i]}< vs >{targetStr[j]}<\n')
    if inputStr[i] == targetStr[j]:
        i+=1
        j+=1
        if j == len(targetStr):
            numOfMatch+=1
            j=0
    else:
        i+=1
        j=0

sleep(.5)
print('='*37, '\nIteration over input string finished.\n')
print(f'The number of recurrences of "{targetStr}" was "{numOfMatch}" time(s).\n')
system('pause')
