#!/usr/bin/python
# -*- coding: utf-8 -*-

from SpellChecker.word2vec import word2vec as w2v
from SpellChecker import editdistance
import SpellChecker.editdistance as ed


def toStringX(x):
    ret = "00"
    ret = str(x/10)+str(x%10)
    return ret

class SuggestionGenerator:
    def __init__(self, fname, savedfile, dictionaryfile, psgfile):
        self.w2vmodel = w2v(fname, savedfile)
        self.dictionary = self.makedictionary(dictionaryfile)    
        self.M = self.makepsg(psgfile)
        
    def makedictionary(self, fname):
        M={}
        V=[]        
        md = open(fname, "r")
        temstr=md.read().splitlines()
        topush=''
        cnt = 1
        for temstrs in temstr:
            topush=''
            topush=str(temstrs)
            ## print    (topush)
            M[topush] = cnt
            cnt = cnt + 1
        md.close()            
        return M
    
    def makepsg(self, fname):
        M={}
        V=[]        
        md = open(fname, "r")
        temstr=md.read().splitlines()
        topush=''
        cnt = 0
        for temstrs in temstr:
            if str(temstrs) is "#":
                cnt+=1
            else :
                topush=''
                topush=str(temstrs)
            #    # print    (topush)
                M[topush] = cnt
        md.close()            
        return M
    
    def inDictionary(self, word):
        if (word in self.dictionary):
            return True
        return False

    def isCorrect(self, sentence):
        ret = -1
        for word in sentence:
            ret = ret + 1
            # print    (word)
            if (self.inDictionary(word) == False):
                return ret
        return -1
    
    def singleWordSuggestions(self, word):
        tmp=''
        tmp=str(word[0:3])
        print    (word, tmp)
        
        filename = "./res/groups/"+toStringX(self.M[tmp])+"/inpy.txt"
 
        md = open(filename, "r")
        temstr=md.read().splitlines()
        
        minval = 100
        ret = []        
        pseudo = []
        for temstrs in temstr:
            cur = str(temstrs)            
            newval = ed.editDistanceBengali(cur, word)
            pseudo.append([cur, newval])             
        pseudo = sorted(pseudo, key=lambda sug: sug[1])
        idx = 0
        lim = min(len(pseudo), 100)
        while (idx < lim):
            ret.append(pseudo[idx]) 
            idx = idx + 1
        # print    ("single owrd suggestions: ", str(len(ret)))       
        return ret
        
    def sed (self, sentence, idx):
        gen = self.singleWordSuggestions(sentence[idx])
        ret = [] 
        for suggestion in gen:
            newsuggestion = []
            i = 0
            for word in sentence:
                if (idx != i):
                    newsuggestion.append(sentence[i]) 
                else:
                    newsuggestion.append(suggestion[0])               
                i = i + 1       
            ret.append([newsuggestion, suggestion[1]])
        # print    ("them suggestions: ", len(ret))        
        return ret
    
    def magic(self, sentence):
        return sentence[1] * self.w2vmodel.probabilityOfText(sentence[0])            

    def trim (self, suggestions):
        ret = []
        print    (len(suggestions))        
        for sug in suggestions:
            #print    ("at")            
            for s in sug[0:min(100, len(sug) )]:
                ## print    (s)
                ret.append(s)
        # print    (ret[0])

        ret = sorted(ret, key=lambda sug: sug[1])
        print(len(ret))
        
        for rets in ret:
            rets.append(self.w2vmodel.probabilityOfText([rets[0]]))

        ## print    (ret)
        ret = sorted(ret, key=lambda sug: sug[2][0], reverse = True)
        okay = []        
        for rets in ret:
            okay.append(' '.join(rets[0]) )        
        return okay   

     
    def gen(self, sentence):
        listOfSuggestions = []       
        sentence = sentence.split() 
        idx = self.isCorrect(sentence) 
        # idx stores the index of the misspelt word
        # if no word is misspelt, then idx is -1        
        if (idx != -1):
            listOfSuggestions.append(self.sed(sentence, idx) )
        else:
            idx = 0
            for word in sentence:
                listOfSuggestions.append(self.sed(sentence, idx ) )
                idx = idx + 1
        listOfSuggestions = self.trim(listOfSuggestions)
        for trims in listOfSuggestions:
            print(trims)     
        return listOfSuggestions[0:min(10, len(listOfSuggestions))]

 
