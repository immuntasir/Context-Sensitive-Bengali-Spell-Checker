# -*- coding: utf-8 -*-
from SpellChecker.kneser_ney import KneserNeyLM 
from nltk.util import ngrams
class MySentences(object):
    def __init__(self, fname):
        self.fname = fname
 
    def __iter__(self):
        for line in open(self.fname):
            yield line.split()
 
fname = '/home/immuntasir/Documents/SpellCheckerContext/res/okay.txt'
sentences = MySentences(fname)
gut_ngrams = (
    ngram for sent in sentences for ngram in ngrams(sent, 3,
    pad_left=True, pad_right=True))
lm = KneserNeyLM(3, gut_ngrams, end_pad_symbol='<s>')
print(lm.score_sent(('আমি', 'ভাত', 'খাও')))
