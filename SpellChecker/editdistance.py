#!/usr/bin/python
# -*- coding: utf-8 -*-
def editDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
def makeList(string1, s1, jmp):
    i = 0
    j = 0
    while (i<len(s1)):
        j = i
        tmp = []
        while (j < i + jmp): 
            tmp.append(s1[j])        
            j = j + 1
        string1.append(tmp);
        i = i + jmp
    
def editDistanceEnglish(s1, s2):
    string1 = []
    string2 = []
    jmp = 1
    makeList(string1, s1, jmp)
    makeList(string2, s2, jmp) 
    return editDistance(string1, string2)

def editDistanceBengali(s1, s2):
    string1 = []
    string2 = []
    jmp = 3;
    makeList(string1, s1, jmp)
    makeList(string2, s2, jmp)
    return editDistance(string1, string2)
