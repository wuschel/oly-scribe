# wuscheln@googlemail.com
# Scribe of the Ivory Tower
# Order Preprocessor for Olympia G4
# v018 

scribeversion = 18

import webbrowser
from Tkinter import * 
from tkSimpleDialog import askstring
from tkFileDialog   import asksaveasfilename
from tkFileDialog   import askopenfilename
from tkMessageBox import askokcancel
from olyG3_AutoComplete import AutoComplete
from olyG3_transcribedata import preprocessordict
from olyG3_transcribedata import reprocessordict
from olyG3_transcribedata import dictionary_version




transscriber_version = "2r1"



class ScrolledText(Frame):
    def __init__(self, parent=None, text='', file=None):
        Frame.__init__(self, parent)
        self.bind_all("<Key>", self.Auto)
        self.pack(expand=YES, fill=BOTH)               
        self.makewidgets()
        self.settext(text, file)
        # adding for hyperparser.py: Taken from idlelib/EditorWindow.py
        self.tabwidth = 8
        self.indentwidth = self.tabwidth
        self.context_use_ps1 = False
        self.num_context_lines = 50, 500, 5000000
        

    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN)
        sbar.config(command=text.yview)                  
        text.config(yscrollcommand=sbar.set)           
        sbar.pack(side=RIGHT, fill=Y)                   
        text.pack(side=LEFT, expand=YES, fill=BOTH)     
        self.text = text
    def settext(self, text='', file=None):
        if file:
            print "found file"
            text = open(file, 'r').read()
        self.text.delete('1.0', END)                   
        self.text.insert('1.0', text)                  
        self.text.mark_set(INSERT, '1.0')              
        self.text.focus()                                
    def gettext(self):                               
        return self.text.get('1.0', END+'-1c')
    def Auto(self,event):
        if event.char in "abcdefghijklmnopgrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_":
            autocomplete = AutoComplete(self)
            autocomplete.autocomplete_event(None)


  
    

    


class SimpleEditor(ScrolledText):                        
    def __init__(self, parent=None, file=None):      
        self.root = Tk()                                    
        self.root.title("Olympia SCRIBE v"+str(scribeversion)+" - "+str(dictionary_version[1]))
        # ----
        frm = Frame(parent)
        frm.pack(fill=X)
        Button(frm, text='Open', command=self.onOpen).pack(side=LEFT)
        Button(frm, text='Save',  command=self.onSave).pack(side=LEFT)
        Button(frm, text='Find',  command=self.onFind).pack(side=LEFT)
        Button(frm, text='Cut',   command=self.onCut).pack(side=LEFT)
        Button(frm, text='Copy',   command=self.onCopyAll).pack(side=LEFT)
        Button(frm, text='Paste', command=self.onPaste).pack(side=LEFT)
        #Button(frm, text='Check', bg="yellow", command=self.onCheck).pack(side=LEFT)      
        Button(frm, text='Transcribe orders', bg="green", command=self.onPreprocess).pack(side=LEFT)
        Button(frm, text='Clean Comments', bg="darkgrey", command=self.onClean).pack(side=LEFT)
        
        Button(frm, text='About',  command=self.onAbout).pack(side=LEFT)
        Button(frm, text='Rules',  command=self.onRules).pack(side=LEFT)
        Button(frm, text='Skills',  command=self.onSkills).pack(side=LEFT)
        Button(frm, text='Orders',  command=self.onOrdersRules).pack(side=LEFT)   

        ScrolledText.__init__(self, parent, file=file) 
        self.text.config(font=('courier', 8, 'normal'))

        



    # Taken from idlelib\EditorWindow.py
    # needed for AutoComplete method to work
    # ----------------------------------------------------
    def _build_char_in_string_func(self, startindex):
        def inner(offset, _startindex=startindex,
                  _icis=self.is_char_in_string):
            return _icis(_startindex + "+%dc" % offset)
        return inner

    def is_char_in_string(self, text_index):
        if self.color:
            # Return true iff colorizer hasn't (re)gotten this far
            # yet, or the character is tagged as being in a string
            return self.text.tag_prevrange("TODO", text_index) or \
                   "STRING" in self.text.tag_names(text_index)
        else:
            # The colorizer is missing: assume the worst
            return 1
    # ----------------------------------------------------



    def onOpen(self):
        filename = ""
        filename = askopenfilename()
        #print "opening file: "+filename
        if filename != "":
            with open(filename, 'r') as file:
                text = file.read()
            self.settext(text)
    def onSave(self):
        filename = asksaveasfilename()
        if filename:
            alltext = self.gettext()                      
            open(filename, 'w').write(alltext)
        #print "saving "+filename
    def onCopyAll(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)                
        self.clipboard_clear()              
        self.clipboard_append(text)
    def onCut(self):
        text = self.text.get(SEL_FIRST, SEL_LAST)        
        self.text.delete(SEL_FIRST, SEL_LAST)           
        self.clipboard_clear()              
        self.clipboard_append(text)
    def onPaste(self):                                    
        try:
            text = self.selection_get(selection='CLIPBOARD')
            self.text.insert(INSERT, text)
        except TclError:
            pass                                      
    def onFind(self):
        target = askstring('SimpleEditor', 'Search String?')
        if target:
            where = self.text.search(target, INSERT, END)  
            if where:                                    
                print where
                pastit = where + ('+%dc' % len(target))   
               #self.text.tag_remove(SEL, '1.0', END)     
                self.text.tag_add(SEL, where, pastit)     
                self.text.mark_set(INSERT, pastit)         
                self.text.see(INSERT)                    
                self.text.focus()
    def onAbout(self):
        win = Toplevel()
        # display message

        w1 = Label(win, text="\n\nSCRIBE", font=("Helvetica", 16))
        w2 = Label(win, text="for Olympia G4", fg="black")
        w3 = Label(win, text="version "+str(scribeversion), fg="red")
        w4 = Label(win, text="(c) 2011 Piotr\n\n", fg="blue")
        w5 = Label(win, text="IVORY TOWER R&D", fg="black")
        w6 = Label(win, text=manualtext, anchor=W, justify=LEFT, font=("Courier", 9))
        w1.pack()
        w2.pack()
        w3.pack()
        w6.pack()
        w4.pack()

        # quit child window and return to root highlight window
        # the button is optional here, simply use the corner x of the child <strong class="highlight">window</strong>
        Button(win, text='OK', command=win.destroy).pack()

    def onRules(self):
        webbrowser.open_new("http://www.shadowlandgames.com/olympia/rules.html")

    def onSkills(self):
        webbrowser.open_new("http://www.shadowlandgames.com/olympia/skills.html")

    def onOrdersRules(self):
        webbrowser.open_new("http://www.shadowlandgames.com/olympia/orders.html")

        


    # More complicated functions here..
    def onCheck(self):
            print "\n\n\nBwahahaah! Who needs order checking?! The IVORY TOWER shall always prevail..\n\n"


 
        
        
    def onPreprocess(self):
        """Testing text processing. Some weird workaround is needed, as print line[0] does not work
            and some really weird artifacts can be found in the code.
            This methods breaks the string into a list of lines, and the lines into a list of elements."""

        outputlinelist = []
        outputtext = ''
        

        text = self.text.get('1.0', END+'-1c')
        # splitting text into a list of lines
        linelist = text.split("\n")

        
        for line in linelist:
            # go through all lines of the orders text
            processedelementlist = []
            outputelementlist = []
            outputlinestring = ''
            elementlist = line.split(' ')
            # split the line into a list of seperate elements
            #print 
            #print " -----------------------------------"
            #print "Processing line of orders."
            #print "elementlist: ",
            #print elementlist

            # check if line is empty before the # character
            lineisempty = True
            for element in elementlist:
                if element == "#":
                    break
                if element != "":
                    lineisempty = False
                    #print "line is not empty before #."

            processfurther = True
            for element in elementlist:
                if element == "#":
                    #print "# found! No longer processing this line."
                    processfurther = False
                #print "     element {"+element+"}", 
                if element in preprocessordict.keys() and elementlist[0] != 'unit' and processfurther == True:
                    #print " ==> has been preprocessed."
                    # this element gets transcribed, for it is in the dictionary
                    outputelementlist.append(preprocessordict[element][0])
                elif element not in preprocessordict.keys() and elementlist[0] != 'unit' and processfurther == True:
                    #print " is NOT the preprocessing dictionary, but has been copied over."
                    # it is not in the dictionary, and it gets appended.
                    outputelementlist.append(element)
                    
                elif elementlist[0] != 'unit' and processfurther == False and lineisempty == False:
                    #print " will not be added, for it is a comment"
                    pass
                else:
                    #print " is NOT the preprocessing dictionary"
                    # it is not in the dictionary, and it gets appended.
                    outputelementlist.append(element)


            
            for element in outputelementlist:
                outputlinestring = outputlinestring + element + " " 
                

            outputlinelist.append(outputlinestring)
            #print "outputlinelist: ",
            #print outputlinelist

        for line in outputlinelist:
            outputtext = outputtext + line +'\n'


        self.settext(outputtext)

            

    def onClean(self):
     # see onPreprocess() for more details
        outputlinelist = []
        outputtext = ''
        text = self.text.get('1.0', END+'-1c')
        linelist = text.split("\n")
        for line in linelist:
            processedelementlist = []
            outputelementlist = []
            outputlinestring = ''
            elementlist = line.split(' ')

            # check if line is empty before the # character
            lineisempty = True
            for element in elementlist:
                if element == "#":
                    break
                if element != "":
                    lineisempty = False
                    #print "line is not empty before #."

     

            for element in elementlist:
                if lineisempty == True and elementlist[0] != 'unit':
                    pass
                else:
                    #processedelementlist.append(element)
                    outputelementlist.append(element)

            for element in outputelementlist:
                if element != '':
                    outputlinestring = outputlinestring + element + " " 
                

            outputlinelist.append(outputlinestring)

        linenr = 0
        for line in outputlinelist:
            if line != '':
                outputtext = outputtext + line +'\n'
            if linenr < len(outputlinelist)-1:
                if outputlinelist[linenr+1].find('unit') != -1:
                    outputtext = outputtext + "\n\n"
            linenr = linenr + 1
            
        self.settext(outputtext)




    

if __name__ == '__main__':
    print "\n"
    for i in dictionary_version:
        print "    "+i
    print "    _____________________________________________________"
    manualtext = """
    Deep down, in the darkest catacombs, mazes of twisty
    passages, all alike, buried under mountains of books
    and ancient scriptures, alone with zillions of
    quixotic sorting labels that had no system at all,
    lived a scribe..

    Welcome to SCRIBE, the little helper for pbem games
    based on the Olympia engine.

        Features:

        -- autocomplete drop-down window for 
        -- input of non-numerical order/item/skill commands       
           and preprocessing of pre-orders to game orders
           i.e. "study summon_demon_lord" -> "study 905"
        -- removal of game/order template comments
        -- open/save functions

        Quick and dirty manual:

        - load order template 
        - enter some game orders
        - use space, up/down arrows, pgup/pgdown button
          to choose from autocompletion menu
        - hit space to paste selected keyword into orders,
          even if theword is not finished.
        - finish orders.
        - Transcribe and remove comments (in case you use
          a tool to generate enhanced templates)
        - report any bugs :)

    Cheers!

        
    """
    print manualtext
    
    try:
        SimpleEditor(file=sys.argv[1]).mainloop()   
    except IndexError:
        SimpleEditor().mainloop()
    #pause
