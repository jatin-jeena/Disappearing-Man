import random
man1 = ["            ___ \n", "           (o ", "o)\n", "           --", "|", "--\n", "            / ", "\ \n" ]
Library=["Vikram Vedha", "Taare Zameen Par", "Andhadhun", "Bhaag Milkha Bhaag", "Jo Jeeta Wohi Sikandar", "Paan Singh Tomar", "Rang De Basanti", "Gangs of Wasseypur", "A Wednesday", "Dil Chahta Hai", "Zindagi Na Milegi Dobara", "Lage Raho Munna Bhai", "Baahubali", "Bajrangi Bhaijaan", "Gangaajal"]
Guesses = 0
wrongGuess = []
word = random.choice(Library).lower()
word = list(word)
n = word.__len__()
current = []
j = 3
for i in range(n):
    if word[i] != " ":
        current.append("__")
    else:
        current.append("   ")
while j > 0:
    given = random.randrange(n)
    current[given] = word[given]
    j -= 1


def display():
    print(*man1, sep="")
    print("Wrong Guess :", *wrongGuess, sep=" ")
    print("Guesses :", Guesses)
    print("Current State :  ", end = " ")
    currentState()
    print("\n")
    print("******************************************")


def currentState():
    for i in current:
        print(i, end=" ")


def getData():
    global Guesses
    new = input()
    Guesses += 1
    flag = 1
    if new in word:
        for j in range(n):
            if word[j] == new:
                if current[j] == "__" and flag != 0:
                    current[j] = word[j]
                    flag = 0
        if flag == 1:
            wrongGuess.append(new)
            man1.__delitem__(-1)
    else:
        wrongGuess.append(new)
        man1.__delitem__(-1)


while wrongGuess.__len__() < 8 and current.count("__") != 0:
    display()
    getData()
if wrongGuess.__len__() >= 8:
    print("Correct answer is ", *word, sep = " ")
    print("You Lost!!!!!")
else:
    print("You Won!!!!!!!!")
