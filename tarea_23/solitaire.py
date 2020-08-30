import random
from enum import Enum

joker_A = 'A'
joker_B = 'B'


def __getShuffledCards():
    return [
        6, 22, 36, 35, 45, 18, 43, 21, 11, 31, 13, 25, 28, 37, 39, 2, 27, 44,
        49, 17, 30, 47, 10, 40, 14, 15, 12, 24, 1, 5, 42, 19, 52, 20, 46, 23,
        26, 'B', 51, 3, 9, 32, 4, 7, 38, 'A', 8, 34, 16, 29, 48, 33, 41, 50
    ]
    # cards = list(range(1, 53)) + [joker_A, joker_B]
    # random.shuffle(cards)
    # print("shuxffle", cards)
    # return cards


def __swapA(cards):
    currentPos = cards.index(joker_A)
    nextPos = currentPos + 1 if currentPos < len(cards) - 1 else 1
    del cards[currentPos]
    cards.insert(nextPos, joker_A)


def __swapB(cards):
    currentPos = cards.index(joker_B)
    nextPos = None
    if currentPos == len(cards) - 1:
        nextPos = 2
    elif currentPos == len(cards) - 2:
        nextPos = 1
    else:
        nextPos = currentPos + 2
    del cards[currentPos]
    cards.insert(nextPos, joker_B)


def __swapEnds(cards):
    aPos = cards.index(joker_A)
    bPos = cards.index(joker_B)
    indexes = [aPos, bPos]
    indexes.sort()
    firstEnd = cards[:indexes[0]] if indexes[0] > 0 else []
    middleChunk = cards[indexes[0]:indexes[1] + 1]
    lastEnd = cards[indexes[1] + 1:] if indexes[1] + 1 < len(cards) else []
    cards[:] = lastEnd + middleChunk + firstEnd


def __isJoker(card):
    return [joker_A, joker_B].__contains__(card)


def __checkLastAndSwap(cards):
    lastCard = cards[-1]
    if __isJoker(lastCard):
        return cards
    firstEnd = cards[lastCard:cards.__len__() - 1]
    middleEnd = cards[:lastCard]
    lastEnd = [lastCard]
    cards[:] = firstEnd + middleEnd + lastEnd


def __module26(number):
    return number if number <= 26 else number - 26


def __charToNumber(char):
    charToNumberMap = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }
    return charToNumberMap[char]


def __numberToChar(number):
    chars = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    index = __module26(number) - 1
    return chars[index]


def __solitaire(cards):
    __swapA(cards)
    __swapB(cards)
    __swapEnds(cards)
    __checkLastAndSwap(cards)
    topCard = cards[0]
    if (__isJoker(topCard)):
        return
    outputCard = cards[topCard - 1]
    if (__isJoker(outputCard)):
        return
    return __module26(outputCard)


def __getSolitaireNumbers(msgLen, cards):
    solitaireNumbers = []
    while (msgLen > len(solitaireNumbers)):
        number = __solitaire(cards)
        if (number != None):
            solitaireNumbers = solitaireNumbers + [number]
    return solitaireNumbers


def __makeChunk(chars):
    return [''.join(chars[i:i + 5]) for i in range(0, len(chars), 5)]


def __mergeChunks(chunks):
    text = ''
    for chunk in chunks:
        text = text + chunk
    return text


def encrypt(msg):
    shuffledCards = __getShuffledCards()
    cardsCopy = list(shuffledCards)
    msgChars = list(msg.upper().replace(" ", ""))
    solitaireNumbers = __getSolitaireNumbers(len(msgChars), shuffledCards)
    coded = []
    for i in range(len(msgChars)):
        charNumber = __charToNumber(msgChars[i])
        addition = charNumber + solitaireNumbers[i]
        coded = coded + [__numberToChar(addition)]
    return [__makeChunk(''.join(coded)), cardsCopy]


def decrypt(chunks, cards):
    msg = __mergeChunks(chunks)
    msgChars = list(msg.upper().replace(" ", ""))
    solitaireNumbers = __getSolitaireNumbers(len(msgChars), cards)
    decoded = []
    for i in range(len(msgChars)):
        charNumber = __charToNumber(msgChars[i])
        solNumber = solitaireNumbers[i]
        substraction = charNumber - solNumber if charNumber > solNumber else charNumber - solNumber + 26
        decoded = decoded + [__numberToChar(substraction)]
    return [''.join(decoded[i:i + 5]) for i in range(0, len(decoded), 5)]
