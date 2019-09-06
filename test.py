#!/usr/bin/python
# -*- coding: utf-8 -*-
import SpellChecker.suggestiongenerator as generator


resfolder = '/home/immuntasir/Documents/SpellCheckerContext/res/'
fname = resfolder + 'crawl.txt'
savedfile = resfolder + 'trained'
dictionaryfile = resfolder + 'dict.txt'
psgfile = resfolder + 'psg.txt'
Gen = generator.SuggestionGenerator(fname, savedfile, dictionaryfile, psgfile)
sentence = str(raw_input())
print(str)
ret = Gen.gen(sentence)
for rets in ret:
    print(rets)
