
import string
file = open('AdjectivesList.txt', 'r')
lines = file.readlines()
file.close()
file2 = open('AdverbsList.txt', 'r')
lines2 = file2.readlines()
file.close()
verbs = open('VerbsList.txt', 'r')
lines3 = verbs.readlines()
verbs.close()
conjunctions = ['and','but','for','or','yet','nor','after', 'so', 'although', 'as', 'because', 'before', 'how', 'if', 'since', 'so', 'provided', 'than', 'that', 'though', 'unless' , 'when', 'whenever' , 'where', 'wherever', 'which', 'while']
conjunctions2 = ['and','but','for','or','yet','nor','after', 'so']
while True:
    d = 0
    e = 0
    protectedWords = []
    v = 0
    ca = 0
    b = 0
    posadj = []
    posadv = []
    re = 93829048
    posverb = []
    posiop2 = 324989832904703924729846328964392
    posapre = 498329074
    posword1 = 349027390274
    viableConjunctions = []
    wordspre1 = []
    posaprechecker = 348092403284032840
    pos = -100000
    pos2 = -1009382098
    posa = -809238098
    posiop = 93205749832649832649806
    posa2 = 4238904839026754932605
    i = 0 #Words
    c = 1 #Independent Clauses (All sentences have at least one right?)
    s = 0 #Dependent Clauses
    GG = str("Hello") #Eventually displays sentence type
    Sentence = input("S") #Input Sentence
    Sentence2 = Sentence
    Sentence = Sentence.translate(str.maketrans('','',string.punctuation))
    words2 = Sentence2.split()
    words3 = Sentence.split()
    print(words2)
    words = Sentence.split() #Splits sentence into words
    size = len(words)
    size2 = size - 1
    gg = (words[size2])
    ggg = gg.lower()
    print (words[size2])
    print(words3)
    for word in words2:
        if ';' in word:
            c+=1
            v+=1
            print("Semicolon found")
    for y, lol in enumerate(lines3):
        lolol = lol.lower().strip()
        if gg == lolol:
            v+=1
            print("Last word of sentence is a verb! Factored into calculation")
    for word in words:
        e+=1
    print("words:", e)
    keyword = "the"
    if keyword in words:
        for keyword in words:
            pos = words.index(keyword)
    keyword2 = "a"
    if keyword2 in words:
        for keyword in words:
            posa = words.index(keyword2)
            posa2 = (posa + 1)
    for word in words:
        dd = word
        pos2 = words.index(dd)
        lololol = ((pos2))
        nw = word.lower()
        ty = str(nw)
        for x, lol in enumerate(lines3):
            gg = (lol.lower().strip())
            hh = str(gg)
            if ty == hh:
                if not pos == lololol:
                    if not pos2 == posa2:
                        protectedWords.append(word)
                        print("Verb Detected pre removal, placed on protected list")
    for word in words:
        nw = word.lower()
        ty = str(nw)
        for x, lol in enumerate(lines):
            gg = (lol.lower().strip())
            hh = str(gg)
            if ty == hh:
                if not nw == "the":
                    if not word in protectedWords:
                        pr4 = words.index(word)
                        posadj.append(pr4)
                        print("Adjective identified", word, ",position noted pre-removal")
    for word in words:
        nw = word.lower()
        ty = str(nw)
        for x, lol in enumerate(lines2):
            gg = (lol.lower().strip())
            hh = str(gg)
            if ty == hh:
                if not nw == "the":
                    if not nw in conjunctions:
                        if not word in protectedWords:
                            pr5 = words.index(word)
                            posadv.append(pr5)
                            print("Adverb identified,", word, "position noted pre-removal")
    for word in words:
        nw = word.lower()
        ty = str(nw)
        if word in conjunctions:
            pr6 = words.index(word)
            pr7 = (pr6 + 1)
            if (pr7 in posadj):
                words.remove(word)
            if (pr7 in posadv and not pr7 in posadj):
                words.remove(word)
    #The following for statement removes all adjectives (accuracy + 1 - 2%)
    for word in words:
        nw = word.lower()
        ty = str(nw)
        for x, lol in enumerate(lines):
            gg = (lol.lower().strip())
            hh = str(gg)
            if ty == hh:
                if not nw == "the":
                    if not word in protectedWords:
                        if not nw in conjunctions:
                            words.remove(word)
                            print("Adjective identified", word, "Removed from calculation")
    for word in words:
        nw = word.lower()
        ty = str(nw)
        for x, lol in enumerate(lines2):
            gg = (lol.lower().strip())
            hh = str(gg)
            if ty == hh:
                if not nw == "the":
                    if not nw in conjunctions:
                        if not word in protectedWords:
                            words.remove(word)
                            print("Adverb identified,", word, "Removed from calculation")
    print(words)
    for word in words:
        d+=1
    keyword = "the"
    if keyword in words:
        for keyword in words:
            pos = words.index(keyword)
    keyword2 = "a"
    if keyword2 in words:
        for keyword in words:
            posa = words.index(keyword2)
            posa2 = (posa + 1)
    k = (d-1)
    for word in words:
        dd = word
        pos2 = words.index(dd)
        lololol = ((pos2))
        nw = word.lower()
        ty = str(nw)
        for x, lol in enumerate(lines3):
            gg = (lol.lower().strip())
            hh = str(gg)
            if ty == hh:
                if not pos == lololol:
                    if not pos2 == posa2:
                        v+=1
                        print("Verb identified" , word)
    for word in words2:
        if ',' in word:
            posword1 = words2.index(word)
            wordspre1.append(posword1)
            ca+=1
            print(word, "Had a comma, noted in calculation position ", posword1)
    for word in words2:
        if word in conjunctions:
            posapre = words2.index(word)
            posaprechecker = posapre - 1
            if posaprechecker in wordspre1:
                viableConjunctions.append(posapre)
                print("Added to viable conjunctions word ", posapre)
    for word in words: #For each word in the sentence
        i+=1 #Add 1 to the word count
        r = i+1
        #All of the words you said introduce an independent clause
        if (word == "and" or word == "but" or word == "for" or word == "or" or word == "nor" or word == "yet" or word == "so" or word == "And" or word == "But" or word == "For" or word == "Or" or word == "Nor" or word == "Yet" or word == "So"):
            posiop = words2.index(word)
            print('pos', posiop)
            print('Viable Conjunctions', viableConjunctions)
            if posiop in viableConjunctions:
                b = 1
                print(b)
                print("This word is a viable conjunction")
            if not posiop in viableConjunctions:
                b = 0
                print("This is not a viable conjunction")
            if (i == (d-2)):
                if not i == 1: #Makes sure the sentence doesnt start with and
                    print('Condition1 true')
                    if not i == 2: #Makes sure the thing isnt introducing an object (Increases accuracy by ~ 25%)
                        print('Condition2 true')
                        if not (i == k): #' ' (Increases accuracy by ~10%, right 85% of the time)
                              if (b):
                                  print("Condition5 True")
                                  if not i == d: #Fixes "ands" at end of sentence due to adjective removal (increases accuracy by 1%)
                                     print('Condition6 True')
                                     c+=1 #Adds one to independent clause amount
                                     b=0 #Resets viability
                                     print('Independent clause identified after word',word)
            if not (i == (d-2)):
                if not i == 1: #Makes sure the sentence doesnt start with and
                    if not i == 2: #Makes sure the thing isnt introducing an object (Increases accuracy by ~ 25%)
                        if not (i == k): #' ' (Increases accuracy by ~25%, right 95% of the time)
                            if not i == d:#Fixes "ands" at end of sentence due to adjective removal (increases accuracy by 1%)
                                if b:
                                    c+=1 #Adds one to independent clause amount
                                    b = 0
                                    print('Independent clause identified after word', word)
        if c > v and not v == 0: #Makes sure there are enough verbs for a new independent clause (Accuracy + ~3%)
            t = c-v
            c = c-t
            
        #All of the words you said introduce a Dependent Clause        
        if (word == "after" or word == "although" or word == "as" or word == "because" or word == "before" or word == "how" or word == "if" or word == "since" or word == "so" or word == "provided" or word == "than" or word == "that" or word == "though" or word == "unless" or word == "when" or word == "whenever" or word == "where" or word == "wherever" or word == "which" or word == "while" or word == "After" or word == "Although" or word == "As" or word == "Because" or word == "Before" or word == "How" or word == "If" or word == "Since" or word == "So" or word == "Provided" or word == "Than" or word == "That" or word == "Though" or word == "Unless" or word == "When" or word == "Whenever" or word == "Where" or word == "Wherever" or word == "Which" or word == "While"):
            posiop2 = words3.index(word)
            ll = word.lower().strip()
            if ll in conjunctions2:
                print("Confliction detected: Calculationg")
                if not (posiop2 in viableConjunctions):
                    s+=1 #Adds one to dependent clause amount
                    print("Dependent clause identified after word", word)
            if not ll in conjunctions2:
                s+=1
                print("Dependent clause identified after word", word)
        if s > ca:
            re = s - ca
            s = s-re #Removes "When will he come" etc.
         #If there is exactly 1 independent clause and 0 dependent clauses:   
        if (c == 1 and s == 0):
            GG = str("Simple") #Sentence type is simple

         #Ind. >1, Dep = 0:
        if (c > 1 and s == 0):
            GG = str("Compound") #S.T. Compound

         #I am too lazy to annotate the rest. It is self explanatory
        if (c == 1 and s >= 1):
            GG = str("Complex")
        if (c > 1 and s >= 1):
            GG = str("Compound-Complex")
    print(GG) #Display sentence type
    protectedWords.clear()
    posadj.clear()
    posadv.clear()
    viableConjunctions.clear()
    wordspre1.clear()
    b = 0
    
