def getScore(word, topChars):
    score = 0
    addScore = 5
    scoreAssign = {}

    for i in topChars:
        if i in word:
            score += addScore
        addScore -= 0.2

    return score
