import random
import copy

markov = {}
for i in range(26):
    markov[chr(97 + i)] = [1] * 27

markov[''] = [1] * 27

def find(l):
    s = sum(l)
    r = random.randint(1, s)
    pref = 0
    for i in range(len(l)):
        pref += l[i]
        if r <= pref:
            return i
    return len(l) - 1

words = []

def sim(word, isword):
    global markov
    string = ''
    cur = ''
    newm1 = copy.deepcopy(markov)
    newm2 = copy.deepcopy(markov)
    for i in range(len(word)):
        f = ord(word[i]) - 97
        newm1[cur][f] += 50
        if newm2[cur][f] == 1:
            for i in range(len(newm2[cur])):
                if i != f:
                    newm2[cur][f] += 1
        else:
            newm2[cur][f] = newm2[cur][f] - 5
        cur = chr(97 + f)
        string += cur
    if isword:
        markov = newm1
    else:
        markov = newm2

training = [["cat", True],
            ["dog", True],
            ["bat", True],
            ["rat", True],
            ["cog", True],
            ["elephant", True],
            ["pig", True],
            ["noise", True],
            ["light", True],
            ["computer", True],
            ["bog", True],
            ["qrx", False],
            ["sdfsd", False],
            ["csad", False],
            ["gfdh", False],
            ["asdf", False],
            ["qgg", False],
            ["adff", False],
            ["faf", False],
]

for i in training:
    sim(i[0], i[1])

while (1):
    string = ''
    cur = ''
    newm1 = copy.deepcopy(markov)
    newm2 = copy.deepcopy(markov)
    while (1):
        f = find(markov[cur])
        newm1[cur][f] += 50
        if newm2[cur][f] == 1:
            for i in range(len(newm2[cur])):
                if i != f:
                    newm2[cur][f] += 1
        else:
            newm2[cur][f] = newm2[cur][f] - 5
        if (f >= 26):
            break
        cur = chr(97 + f)
        string += cur
    print(f"Word generated: '{string}'")
    y = input("Is word? (y/N): ")
    if y == "y":
        words.append(string)
        markov = newm1
    elif y == "q":
        break
    else:
        markov = newm2
    
    
print(*words)