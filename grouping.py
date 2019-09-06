#!/usr/bin/python
import os, sys
def toString(x):
    ret = "00"
    ret = str(x/10)+str(x%10)
    ## print    (ret)
    return ret
M={}
V=[]
md = open("./res/psg.txt", "r")
temstr=md.read().splitlines()
topush=''
cnt = 0
for temstrs in temstr:
    if str(temstrs) is "#":
        cnt+=1
        ## print    ("what")
    else :
        topush=''
        topush=str(temstrs)
        
        V.append(topush)
        M[topush] = cnt
        # print    (topush, M[topush])


id = open("./res/dict.txt", "r")
tmp=''
dirname = "69"
filename = "./69/inpy.txt"
for i in range(0,cnt):
    dirname= './res/groups/' + toString(i)
    if (os.path.isdir(dirname) == False):
        os.mkdir(dirname, 0755)
    filename= "./res/groups/"+toString(i)+"/inpy.txt"
    od = open(filename, "w")
    od.write("")
    od.close()
temstr = id.read().splitlines()
for temstrs in temstr:
    flag = 1
    for i in temstrs:
        if (ord(i) < 128) :
            flag = 0
    if (flag == 0):
        continue
    tmp=''
    tmp=str(temstrs[0:3])
    ## print    (tmp, M[tmp])
    filename = "./res/groups/"+toString(M[tmp])+"/inpy.txt"
    od = open(filename, "a")
    od.write(temstrs + '\n')
    od.close()



