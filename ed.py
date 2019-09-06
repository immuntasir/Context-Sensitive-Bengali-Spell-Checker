import SpellChecker.editdistance as ed

s1 = []
s2 = []
w1 = str(raw_input())
w2 = str(raw_input())
print("edit distance between", w1, w1, ": ", ed.editDistanceBengali(w1, w2))
