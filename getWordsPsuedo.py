import string
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
goodL = input("Enter letter, or ! to enter a bad letter\n")

while (goodL != "!"):
    good_words.append(goodL)

    if (goodL == "!"):
        break

    location = input("Enter a possible location, or ! to move to next letter\n")
    locationsList = []
    while (location != "!"):
        location = int(location)
        locationsList.append(location-1)
        location = input("Enter a possible location, or ! to move on to next letter\n")
    wordsPos[goodL] = locationsList
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


for i in all_words:
    looksGood = True
    found = False
    for x in bad_letter:
        if x in i:
            looksGood = False

    for y in good_words:
        if (y not in i):
            looksGood = False

    # For each letter that is guaranteed
    isPossible = True
    for z in wordsPos:
        impossiblePos = [0, 1, 2, 3, 4]

        for a in wordsPos[z]:
            if (a in impossiblePos):
                impossiblePos.remove(a)

        for a in impossiblePos:
            if (i[a] == z):
                isPossible = False

    if not isPossible:
        looksGood = False

    if (looksGood):
        i = i[0:len(i)-1]
        possible_words.append(i)
        wordScore[i] = 0

# for x in all_words:
#     x = x[0:len(x)-1]


print("\nPossible words:\n", possible_words)
# Counts letter frequencies
for i in letterCount:
    for x in possible_words:
        if i in x and i not in good_words:
            letterCount[i] = letterCount[i] + 1


# creates a sorted list
letterCount = sorted(letterCount.items(), key=lambda x: x[1], reverse=True)

counter = 0
for item in letterCount:
    if counter > 9:
        break

    mostCommon[counter] = item[0]
    counter = counter + 1

# print(letterCount)
print(mostCommon)

def getScore(word, topChars):
    score = 0
    addScore = 5
    scoreAssign = {}

    for i in topChars:
        if i in word:
            score += addScore
        addScore -= 0.2

    return score

highScore = 0

for i in all_words:
    for x in i:
        # Gets rid of dups
        if (x.count(i)) <= 1:
            
            if getScore(i, mostCommon) > highScore:
                highScore = getScore(i, mostCommon)
                wordScore = all_words.index(i)

# print("\nLucky method (seems to be better at the moment): you should try: " + possible_words[0])
print("\nElimination method: you should try: " + all_words[wordScore])


#add a scoring system? we give each word a score based on how many letters it has, make sure to add an if statement






# We want an algorithm to sort through the top 5 words letters that occur
# Then, we want to sort and see which letters are possible