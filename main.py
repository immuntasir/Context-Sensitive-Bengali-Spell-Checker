#!/usr/bin/python
import Tkinter as tk
import random
import SpellChecker.editdistance as ed








class SpellCheckerBengali:
    def __init__(self, word):
        self.word = word
    def isCorrect(self):
        p = random.randint(4,101)
        return p%2
    def suggestions(self):
        sugg = []
        for i in range(3):
            sugg.append(self.word)
        return sugg

class CheckerWindow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,
                          master,
                          width=300,
                          height=200)
        self.master.title('Spell Checker 1.0.0')
        self.labels=[]
        self.pack_propagate(0)
        self.pack()
        self.recipient_var = tk.StringVar()
        self.recipient = tk.Entry(self,textvariable=self.recipient_var)
        self.recipient_var.set('Mathematics')
        self.go_button = tk.Button(self,text='Check',command=self.print_out)
        self.go_button.pack(fill=tk.X, side=tk.BOTTOM)
        self.recipient.pack(fill=tk.X, side=tk.TOP)
 
    def print_out(self):
        for label in self.labels: 
            label.destroy()
            
        bengal = SpellCheckerBengali(self.recipient_var.get())
        if bengal.isCorrect() == 1: 
            label = tk.Label(self, text= "The word "+self.recipient_var.get()+" is correctly spelled")
            label.pack()
            self.labels.append(label)
        
        else:
            suggList = bengal.suggestions()
            label = tk.Label(self, text= "The word is incorrectly spelled. Suggestions: ")
            label.pack()
            self.labels.append(label)
            for suggword in suggList:
                label = tk.Label(self, text= " - "+suggword)
                label.pack()
                self.labels.append(label)
        #print('Suggestion: %s' % (self.recipient_var.get()))
    def run(self):
        self.mainloop()
 
app = CheckerWindow(tk.Tk())
app.run()
