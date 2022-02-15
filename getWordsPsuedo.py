index = 0

letter = [5]

bad_letter = []
all_words = []
good_words = []
possible_words = []
wordsPos = {}
impossiblePos = []
wordLoc = 0
goodL = input("Enter letter")

while (goodL != "!"):
    good_words.append(goodL)

    if (goodL == "!"):
        break

    location = input("Enter a location")
    locationsList = []
    while (location != "!"):
        location = int(location)
        locationsList.append(location-1)
        location = input("Enter a location")
    wordsPos[goodL] = locationsList
    goodL = input("Enter letter")

badL = input("Enter bad letter")
while (badL != "!"):
    bad_letter.append(badL)
    badL = input("Enter bad letter")

f = open("wordList.txt", "r")

counter = 0

for x in f:
    # x = x[0:len(x)-1]
    all_words.append(x)

# bad_letter.remove("!")
# good_words.remove("!")
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

    for z in wordsPos:
        impossiblePos = [1, 2, 3, 4, 5]

        isPossible = False
        for a in wordsPos[z]:
            if (a in impossiblePos):
                impossiblePos.remove(a)

            if (z in i):
                if (i[a] == z):
                    isPossible = True

    if not isPossible:
        looksGood = False

    if (looksGood):
        i = i[0:len(i)-1]
        possible_words.append(i)

# for x in all_words:
#     x = x[0:len(x)-1]


print(possible_words)
