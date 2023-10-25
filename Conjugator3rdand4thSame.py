#Simulating non-linear Indicative Latin verb conjugations in the Present System
#Verborum Declinator (Haec modo temporibus Praesenti, Imperfecto, Futuro operanda, vel quibus systema Praesente utuntur.)

from tkinter import*

cType = {"a":"1st", "ē":"2nd", "e":"3rd", "i":"4th"}

phi = {
    "s": {1:"o", 2:"s", 3:"t"},
    "p": {1:"mus", 2:"tis", 3:"nt"}
    }
    
t = {"i":"ba", "f":"bi", "p":""}

vowels = ["a", "e", "i", "o", "u"]
cons = []

infin = list(input("Write an infinitive: "))
print(" ")

#check = isinstance(infin, Infinitive)
#print(check)

phiUT = input("How would you like to conjugate? (ex: Write '1st Person Singular Imperfect')").split()
print("--------------------------------------------")
phiUT.remove(phiUT[1])

cTypeU = cType[infin[-3]]
phiPers = int(phiUT[0][0])
phiNum = phiUT[1][0]
tU = phiUT[2][0].lower()

print("Conjugation type: " + cType[infin[-3]])
print(" ")


#treat 3rd w/ infin[-2] == "c" and 4th  types as the SAME. their conjugation patterns are identical in the Present system.
#3rd non-io types are the only exception. 
if infin[-4] == "c" or cTypeU == cType["i"]:
    del infin[-3:]
    infin.append("i")
    if tU != t["p"]:
        if phiPers == phi["s"][1]:
            infin.append("a")
        else:
            infin.append("e")
    else:
        infin.append(t[tU])
else:
    del infin[-2:]
infin.append(t[tU])
    
    
#phi:
root = infin
root.append(phi[phiNum][phiPers])
verb = "".join(root)
verb = list(verb)

#o->m/a_# Rule:
if verb[-1]=="o" and verb[-2] =="a":
    del verb[-1]
    verb.append("m")
    
#"-unt" rule:
if verb[-1] == "t" and verb[-2] == "n":
    if tU == "f":
        if cTypeU == "1st" or cTypeU == "2nd":
            verb[-3] = "u"
    
print("".join(verb))

###################################################

#UI

#class Window(Frame):
#    def __init__(self, master=None):
#        Frame.__init__(self, master)
#        self.master = master
#        self.init_window()
#    def init_window(self):
#        self.master.title('Richard.exe')
#        self.pack(fill=BOTH, expand=1)
#        speechButton = Button(self, text = "Send to Richard", bg = "coral",
#                              command = self.RichardTalk)
#        speechButton.place(x = 50, y = 75)

#root = Tk()
#root.geometry('230x125')
#app=Window(root)
#speechEntry = Entry(root).split()
#speechEntry.place(x = 50, y = 50)
#firstLabel = Label(root, text = "Enter an infinitive to conjugate")
#firstLabel.place(x = 50, y = 25)
#root.mainloop()
