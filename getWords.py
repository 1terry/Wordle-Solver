index = 0

letter = [5]

bad_letter = []
all_words = []
good_words = []
possible_words = []

goodL = input("Enter letter")
while (goodL != "!"):
    good_words.append(goodL)
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

    if (looksGood):
        possible_words.append(i)

# for x in all_words:
#     x = x[0:len(x)-1]

print(possible_words)
