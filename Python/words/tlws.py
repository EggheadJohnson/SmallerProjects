# Three Letter Words.  My family loves word games.  So when we were all together at christmas,
# I posed the question to my family: "How many sets of three letter words exist such that
# each vowel can be the center letter and all five options are all words?  e.g. bat, bet, bit, bot, but"
# After we found a few, I wrote this to find out the answer based on a comprehensive list of three
# letter words.  There are 17 such sets.
# Paul Johnson
# December 2013

# My strategy here was this: Put the vowels last, sort the words, and find any sequence of
# five words that have the same first two letters.

def swapper(l):
    for x in range(len(l)):
        w = l.pop(0)
        w2 = w[0]+w[2]+w[1]
        l.append(w2)
    return l

def checker(l):
    if l[0][2] not in 'AEIOU': return 0
    test = l[0][:-1]
    for x in l[1:]:
        if x[:-1] != test or x[2] not in 'AEIOU':
            return 0
    return l

f = open('Wordlist.txt','r')
words = []
for line in f:
    words.append(line)

words = swapper(words)

words.sort()

answers = []
for x in range(len(words)-4):
    set = words[x:x+5]
    testing = checker(set)
    if testing:
        testing = swapper(testing)
        answers.append(testing)


for set in answers: print set
print len(answers), " found!"

