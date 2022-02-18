from random import randrange
import string

from matplotlib.backend_bases import LocationEvent
from helperMethods import getScore

letterCount = dict.fromkeys(string.ascii_lowercase, 0)

index = 0

letter = [5]
mostCommon = [None] * 10
bad_letter = []
all_words = []
good_words = []
possible_words = []
wordsPos = {}
wordScore = {}
highestScore = ""
impossiblePos = []
wordLoc = 0
guaranteedPos = {}
takenPositions = []

goodL = input("Enter letter, or ! to enter a bad letter\n")

while (goodL != "!"):
    good_words.append(goodL)

    if (goodL == "!"):
        break

    location = input("Enter a location\n")
    color = input("Enter a color, g for green and y for yellow\n")

    location = int(location)-1
    locationList = []

    if (color == 'g'):
        guaranteedPos[goodL] = location
        takenPositions.append(location)

    for i in range(5):
        if i != location and (i not in takenPositions):
            locationList.append(i)
    wordsPos[goodL] = locationList
    goodL = input("Enter letter, or ! to enter bad letter\n")

badL = input("Enter bad letter, or ! to quit\n")
while (badL != "!"):
    bad_letter.append(badL)
    badL = input("Enter bad letter, or ! to quit\n")

f = open("wordList.txt", "r")

counter = 0

for x in f:
    # x = x[0:len(x)-1]
    all_words.append(x)

print("good letters", good_words)
print("bad letters", bad_letter)

# Method for adding good words
for i in all_words:
    looksGood = True
    found = False
    for x in bad_letter:
        if x in i:
            looksGood = False

    for y in good_words:
        if (y not in i):
            looksGood = False

    for z in guaranteedPos:
        if i[guaranteedPos[z]] != z:
            looksGood = False

    if (looksGood):
        i = i[0:len(i)-1]
        possible_words.append(i)
        wordScore[i] = 0

print("\nPossible words:\n", possible_words)
# Counts letter frequencies
for i in letterCount:
    for x in possible_words:
        if i in x and i not in good_words:
            letterCount[i] = letterCount[i] + 1


# creates a sorted list
letterCount = sorted(letterCount.items(), key=lambda x: x[1], reverse=True)

counter = 0

# Counts most common letters
for item in letterCount:
    if counter > 9:
        break

    mostCommon[counter] = item[0]
    counter = counter + 1

# print(letterCount)
print(mostCommon)

# Gets score of each word in every word

highScore = 0

for i in all_words:
    for x in i:
        # Gets rid of dups
        if (x.count(i)) <= 1:

            if getScore(i, mostCommon) > highScore:
                highScore = getScore(i, mostCommon)
                wordScore = all_words.index(i)
# print("\nLucky method (seems to be better at the moment): you should try: " + possible_words[0])

if len(possible_words) <= 4:
    if len(possible_words) == 1:
        print("The word is: ", possible_words)
    else:
        print("You should guess: ", possible_words[int(
            randrange(len(possible_words)))])

else:
    print("You should try: " + all_words[wordScore])


# add a scoring system? we give each word a score based on how many letters it has, make sure to add an if statement


# Add green square checker


# We want an algorithm to sort through the top 5 words letters that occur
# Then, we want to sort and see which letters are possible
