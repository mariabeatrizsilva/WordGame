import csv
#from fileinput import filename

sylDict =[{'word': 'cat', 'syllableNumber': '1'},
        {'word': 'dog', 'syllableNumber': '1'},
        {'word': 'running', 'syllableNumber': '2'},
        {'word': 'teenager', 'syllableNumber': '3'},
        {'word': 'mommy', 'syllableNumber': '2'}]
vowelDict =[{'word': 'cat','vowelCount': '1'},
        {'word': 'dog','vowelCount': '1'},
        {'word': 'running', 'vowelCount': '2'},
        {'word': 'teenager','vowelCount': '4'},
        {'word': 'mommy', 'vowelCount': '1'}]
wordsList = list(sylDict)

def question1(word):
    print ("How many syllables does " + word + "have?")
    correctAnswer = sylDict[word]
    ##userAnswer = input (however we have them input the answer)
    ## if userAnswer != correctAnswer --> lose a life
    ## else 

def question2(word):
    print ("How many vowels does " + word + "have?")
    correctAnswer = vowelDict[word]
    ##userAnswer = input (however we have them input the answer)
    ## if userAnswer != correctAnswer --> lose a life
    ## else 

def question3(sound):
    print ("Which word matches the sound you heard? \n")
    for i in range(4):
        n = random.randint(0,5) 
        print(wordsList[n] + "\n")
