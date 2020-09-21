from random import randint
from os import remove,rename

def getUserPoint(userName):
    try:
        input = open('userScores.txt', 'r')
        for line in input:
            content = line.split(',')
            if content[0] == userName:
                input.close()
                return content[1]
        input.close()
        return '-1'
    except IOError:
        print('\nFile userScores.txt not found. A new file will be created.')
        input.open('userScores.txt','w')
        input.close()
        return "-1"

def updateUserPoints(newUser, userName, score):
    if newUser==True:
        input = open('userScores.txt','a')
        input.write('\n' + userName + ', ' + score)
        input.close
    else:
        input = open('userScores.txt','r')
        output = open('userScores.tmp', 'w')
    for line in input:
        content = line.split(',')
        if content[0] == userName:
           content[1] = score
           line = content[0] + ', ' + content[1] + '\n'
        output.write(line)
    input.close()
    output.close()
    
    remove('userScores.txt')
    rename('userScores.tmp', 'userScores.txt')

def generateQuestion():
    operandList  = [0,0,0,0,0]
    operatorList = ['','','','']
    operatorDict = {1:'+', 2:'-', 3:'*', 4:'**'}

    for index in range(0,5):
        operandList[index] = randint(1,3)

    for index in range(0,4):
        if index > 0 and operatorList[index-1] != '**':
            operator = operatorDict[randint(1,4)]
        else:
            operator = operatorDict[randint(1,3)]
        operatorList[index] = operator

    questionString = str(operandList[0])

    for index in range (1,5):
        questionString = questionString + operatorList[index-1] + str(operandList[index])
    
    result = eval(questionString)
    questionString = questionString.replace('**','^')
    print ('\n' + questionString)
    userResult = input('Answer: ')
    while True:
        try:
          if int(userResult) == result:
           print('\nCorrect!!!')
           return 1
          elif int(userResult) != result:
            print('WRONG\nResult: ' + result)
            return 0
            
        except Exception as e:
            print('That is not a number. Try again')
            userResult = input('Answer: ')
        

    

