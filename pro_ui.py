from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import os


filename = ''
def author():
    showinfo('作者信息','由aixj制作完成')

def about():
    showinfo('版权信息&copyright','本软件归属于aixj')

def openfile():
    global filename
    filename = askopenfilename(defaultextension = '.text')
    if filename == '':
        filename = None
    else:
        root.title('FileName:' + os.path.basename(filename))
        textpad.delete(1.0,END)
        f = open(filename, 'r')
        textpad.insert(1.0, f.read())
        f.close()

def new():
    global filename
    root.title('为命名文件')
    filename = None
    textpad.delete(1.0,END)
def save():
    global filename
    try:
        f = open(filename,'w')
        msg = textpad.get(1.0,END)
        f.write(msg)
        f.close()
    except:
        saveas()
def saveas():
    f = askopenfilename(initialfile='未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    fh = open(f, 'w')
    msg = textpad.get(1.0,END)
    fh.write(msg)
    fh.close()
    root.title('FileName:'+ os.path.basename(f))

def cut():
    textpad.event_generate('<<Cut>>')

def copy():
    textpad.event_generate('<<Copy>>')

def past():
    textpad.event_generate('<<Paste>>')

def redo():
    textpad.event_generate('<<Redo>>')

def undo():
    textpad.event_generate('<<Undo>>')

def selectall():
    textpad.tag_add('sel','1.0', END)

def search():
    topsearch = Toplevel(root)
    topsearch.geometry('300x250+100+250')
    label1 = Label(topsearch, text='Find')
    label1.grid(row=0, column=0, padx=5)
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找',command=lambda:gsearch())
    button1.grid(row=0, column=2)
    def gsearch():
        openfile()
root = Tk()
root.title('Always')
root.geometry('800x500+100+100')

menubar = Menu(root)
root.config(menu = menubar)

filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N',command=new)
filemenu.add_command(label='打开', accelerator='Ctrl + O',command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=saveas)
menubar.add_cascade(label='文件', menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z',command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + Y',command=redo)
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl + X',command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl + C',command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl + V',command=past)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl + F',command=search)
editmenu.add_command(label='全选', accelerator='Ctrl + A',command=selectall)
menubar.add_cascade(label='编辑',menu = editmenu)

aboutmenu = Menu(menubar)
aboutmenu.add_command(label='Author', command=author)
aboutmenu.add_command(label='Copyright', command=about)
menubar.add_cascade(label='About',menu=aboutmenu)

toolbar = Frame(root, height=25, bg='#777777')
shortButton = Button(toolbar, text='打开',command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)

shortButton = Button(toolbar, text='保存',command=save)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO,fill=X)

status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

#linenumbel&text
lnlabel = Label(root, width=2, bg='antique white')
lnlabel.pack(side=LEFT, fill=Y)

textpad = Text(root, undo=True)
textpad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textpad)
textpad.config(yscrollcommand=scroll.set)
scroll.config(command=textpad.yview)
scroll.pack(side=RIGHT, fill=Y)
root.mainloop()