#!/usr/bin/python
# -*- coding: utf-8 -*-
from pathlib import Path
from gensim.models.word2vec import Word2Vec
import os
import gensim
import sys
from sklearn.manifold import TSNE
from sklearn.datasets import fetch_20newsgroups
import re
import matplotlib.pyplot as plt



class MySentences(object):
        def __init__(self, fname):
            self.fname = fname
     
        def __iter__(self):
            for line in open(self.fname):
                yield line.split()
    
class word2vec:
    def __init__(self, fname, savedfile):
        sentences = MySentences(fname) # a memory-friendly iterator
        my_file = Path(savedfile)
        if my_file.is_file():
            self.model = Word2Vec.load(savedfile)
        else:
            self.model = gensim.models.Word2Vec(sentences, hs=1, negative=1)
            self.model.save(savedfile)
       
    def probabilityOfText (self, sentence, index):
        temp = sentence[:]
        temp.pop(index)
        try:
            return self.model.wv.similarity(
                self.model.predict_output_word(temp, topn = 1)[0][0], sentence[index]
            )
        except KeyError:
            return 0
        
