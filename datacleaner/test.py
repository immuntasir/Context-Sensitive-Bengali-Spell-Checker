od = open("valid.txt", "r")

temstr=od.read().split()
M = {}
for temstrs in temstr:
    M[str(temstrs)] = 1

od.close()

dari = '\xe0\xa5\xa4'
towrite = {}
  
def isValid(string):
    i = 0
    l = len(string)
    toprint = ''
    #print("in function", l)
    #print(string)
    while (i<l):
        #print("at",i, string[i])        
        if (string[i] == '\n'):
            break       
        elif (string[i] == ' '):
            i = i + 1            
            toprint+=(' ')            
            continue        
        elif (string[i] == ',' or string[i] == '?'):
            i = i + 1   
            continue        
        elif (ord(string[i]) < 128):
            return ''
        elif (i + 2 >= l):
            return ''
        else:
            tmp=str(temstrs[i:i+3])
            #print(tmp)            
            if (tmp == dari):
                return toprint + '\n'
            if ( (tmp in M) == False):
                return ''            
            else:
                toprint+=(tmp)
                i = i + 3 
    #print ("in function", toprint)   
    return toprint + '\n'

md = open("out.txt", "a")

class MySentences(object):
        def __init__(self, fname):
            self.fname = fname
     
        def __iter__(self):
            for line in open(self.fname):
                yield line
temstr = MySentences("in2.txt")
i = 0
for temstrs in temstr:
    if (i % 100000 == 0):
        print(i)
        #print(temstrs)    
        #print(isValid(temstrs))    
    md.write(isValid(temstrs))
    i = i + 1
md.close()
