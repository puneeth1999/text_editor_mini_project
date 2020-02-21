import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.font as font

class Editor:

    #variables
    root = Tk()

    root.configure(background = 'black') 

    #default window width and height
    thisWidth = 300
    thisHeight = 300
    thisTextArea = Text(root, background = 'black', foreground = 'white', insertbackground = 'white')
    '''
    #Ok peaky boy, Listen up. This 'insertbackground = 'white'' is really important. 
    #Because, without that, we cannot see the blinking text pointing cursor blinking with a naked eye. Hehe.
    #PS: I have no idea why I keep writing useless comments while coding. Just like this one right here.

    #Yours lovingly,
    #Suraj S Jain &
    #Puneeth Choppanati.
    '''
    thisMenuBar   = Menu(root, background = 'black', foreground = 'white')#BTW, white background sucks.
    thisFileMenu  = Menu(thisMenuBar,tearoff=0)
    thisEditMenu  = Menu(thisMenuBar,tearoff=0) #This foreground color didn't make a difference though :(
    thisHelpMenu  = Menu(thisMenuBar,tearoff=0)
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
                self.root.wm_iconbitmap("riggers.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
                pass

        #set window size (the default is 300x300)

        try:
            self.thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.root.title("Untitled - Riggers'SystemSoftwateTextEditor")

        #center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        left = (screenWidth / 2) - (self.thisWidth / 2)
        top = (screenHeight / 2) - (self.thisHeight /2)

        self.root.geometry('%dx%d+%d+%d' % (self.thisWidth, self.thisHeight, left, top))

        #to make the textarea auto resizable
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.thisTextArea.grid(sticky=N+E+S+W)

        self.thisFileMenu.add_command(label="New",command=self.newFile)
        self.thisFileMenu.add_command(label="Open",command=self.openFile)
        self.thisFileMenu.add_command(label="Save",command=self.saveFile)
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit",command=self.quitApplication)
        self.thisMenuBar.add_cascade(label="File",menu=self.thisFileMenu)

        self.thisEditMenu.add_command(label="Cut",command=self.cut)
        self.thisEditMenu.add_command(label="Copy",command=self.copy)
        self.thisEditMenu.add_command(label="Paste",command=self.paste)
        #self.thisEditMenu.add_command(label = "Change font", command = self.changeFont)
        self.thisMenuBar.add_cascade(label="Edit",menu=self.thisEditMenu)


        self.thisHelpMenu.add_command(label="About Editor",command=self.showAbout)
        self.thisMenuBar.add_cascade(label="Help",menu=self.thisHelpMenu)

        self.root.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT,fill=Y)
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)
    
        
    def quitApplication(self):
        self.root.destroy()
        #exit()

    def showAbout(self):
        showinfo("Editor","Created by: Puneeth C and Suraj S Jain.\nFor more information, contact: pnthraj37@gmail.com or surajsjain@hotmail.com")

    def openFile(self):
        
        self.file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.file == "":
            #no file to open
            self.file = None
        else:
            #try to open the file
            #set the window title
            self.root.title(os.path.basename(self.file) + " - SystemSoftwateTextEditor")
            self.thisTextArea.delete(1.0,END)

            file = open(self.file,"r")

            self.thisTextArea.insert(1.0,file.read())

            file.close()

        
    def newFile(self):
        self.root.title("Untitled - SystemSoftwateTextEditor")
        self.file = None
        self.thisTextArea.delete(1.0,END)

    # def changeFont(self):
    #     # self.thisTextArea.tag_add("bt2")
    #     new_font = font.Font(font=self.thisTextArea.cget("times"))
    #     size = new_font.actual()["size"]
    #     new_font.configure(size=size+2)
    #     textPad.tag_config("bt2", font=new_font)
    def choose_font():
        global m, text # I hate to use global, but for simplicity

        t = tk.Toplevel(m)
        font_name = tk.Label(t, text='Font Name: ')
        font_name.grid(row=0, column=0, sticky='nsew')
        enter_font = tk.Entry(t)
        enter_font.grid(row=0, column=1, sticky='nsew')
        font_size = tk.Label(t, text='Font Size: ')
        font_size.grid(row=1, column=0, sticky='nsew')
        enter_size = tk.Entry(t)
        enter_size.grid(row=1, column=1, sticky='nsew')

        # associating a lambda with the call to text.config()
        # to change the font of text (a Text widget reference)
        ok_btn = tk.Button(t, text='Apply Changes',
                           command=lambda: text.config(font=(enter_font.get(), 
                           enter_size.get())))
        ok_btn.grid(row=2, column=1, sticky='nsew')

        # just to make strechable widgets
        # you don't strictly need this
        for i in range(2):
            t.grid_rowconfigure(i, weight=1)
            t.grid_columnconfigure(i, weight=1)
        t.grid_rowconfigure(2, weight=1)





    def saveFile(self):

        if self.file == None:
            #save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.file == "":
                self.file = None
            else:
                #try to save the file
                file = open(self.file,"w")
                file.write(self.thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.root.title(os.path.basename(self.file) + " - SystemSoftwateTextEditor")
                
            
        else:
            file = open(self.file,"w")
            file.write(self.thisTextArea.get(1.0,END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.root.mainloop()





    def choose_font():
        global m, text

        t = tkinter.Toplevel(m)
        font_name = tk.Label(t, text = 'Font Name: ')
        font_name.grid(row = 0, column = 0, sticky = 'nsew')
        enter_font = tk.Entry(t)
        enter_font.grid(row = 0, column = 1, sticky = 'nsew')
        font_size = tk.Label(t, text='Font Size: ')
        font_size.grid(row=1, column=0, sticky='nsew')
        enter_size = tk.Entry(t)
        enter_size.grid(row=1, column=1, sticky='nsew')

         # associating a lambda with the call to text.config()
        # to change the font of text (a Text widget reference)
        ok_btn = tk.Button(t, text='Apply Changes',
                       command=lambda: text.config(font=(enter_font.get(), 
                       enter_size.get())))
        ok_btn.grid(row=2, column=1, sticky='nsew')


         # just to make strechable widgets
        # you don't strictly need this
        for i in range(2):
            t.grid_rowconfigure(i, weight=1)
            t.grid_columnconfigure(i, weight=1)
        t.grid_rowconfigure(2, weight=1)







#run main application


editor = Editor(width=600,height=400)
editor.run()