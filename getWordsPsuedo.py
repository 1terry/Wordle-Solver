index = 0

letter = [5]

bad_letter = []
all_words = []
good_words = []
possible_words = []
possible_locations = [[]]
wordLoc = 0

goodL = input("Enter a determined letter")
location = input("Enter a location")
while (location != "!"):
    try:
        location = int(input("Enter a location"))
    except:
        break
    possible_locations[wordLoc].append(location-1)

wordLoc += 1

while (goodL != "!"):
    good_words.append(goodL)
    goodL = input("Enter letter")

    if (goodL == "!"):
        break

    location = int(input("Enter a location"))
    while (location != "!"):
        location = int(location)    
        possible_locations[wordLoc].append(location-1)
        location = input("Enter a location")

    wordLoc += 1

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
print(good_words)
print(bad_letter)


for i in all_words:
    looksGood = True
    found = False
    for x in bad_letter:
        if x in i:
            looksGood = False

    for y in good_words:
        if (y not in i):
            looksGood = False

    isPossible = False
    for z in possible_locations:
        for a in z:
            if (i[a] == z):
                isPossible

    if not isPossible:
        looksGood = False

    if (looksGood):
        i = i[0:len(i)-1]
        possible_words.append(i)

# for x in all_words:
#     x = x[0:len(x)-1]



print(possible_words)
