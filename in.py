from pathlib import Path
from SpellChecker.word2vec import word2vec as w2v

res = '/home/immuntasir/Documents/SpellCheckerContext/res/'
fname = res + 'crawl.txt'
savedfile = res + 'trained'
        
w2vmodel = w2v(fname, savedfile)

print("All set!")
print("You may proceed.")
while (1):
    sentence = str(raw_input())
    sentence = [sentence.split()]
    print(sentence)
    print(w2vmodel.probabilityOfText(sentence))





