# -*- coding: utf-8 -*-

import math
import subprocess, os, sys
from tkinter import *

class p:
    pointer = 0

mframe = Tk()
zwnj = '\u200c'
space = ' '
mframe.title("تصريف کلمه فارسی رسمی و غير رسمی")
cmds = []
var = IntVar()
repvar = IntVar()
repl = str.maketrans(' كي%1234567890;“”', ' کی٪۱۲۳۴۵۶۷۸۹۰؛""')
v = IntVar()

def make_menu(w):
    global the_menu
    the_menu = Menu(w, tearoff=0)
    the_menu.add_command(label="Cut")
    the_menu.add_command(label="Copy")
    the_menu.add_command(label="Paste")

def show_menu(e):
    w = e.widget
    the_menu.entryconfigure("Cut",
    command=lambda: w.event_generate("<<Cut>>"))
    the_menu.entryconfigure("Copy",
    command=lambda: w.event_generate("<<Copy>>"))
    the_menu.entryconfigure("Paste",
    command=lambda: w.event_generate("<<Paste>>"))
    the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)

def lookup(word):
    if 'win' in sys.platform:
        os.system('chcp 65001')
    word1 = word.translate(repl)
    if var.get() == 1 and "=" not in word1:
        #print(word1)
        word1 = word1.replace(zwnj, '').replace(space, '')

    para = ''
    if "=" in word1:
        para = '-i'
    if para == "":
        lookup_line = 'echo ' + word1 + ' | flookup '
        if v.get() == 1:
            lookup_line += para + ' ./1standard.fst'
        elif v.get() == 2:
            lookup_line += para + ' ./2homophone.fst'
        elif v.get() == 3:
            lookup_line += para + ' ./3avaee.fst'
        elif v.get() == 4:
            lookup_line += para + ' ./4expressive.fst'
        elif v.get() == 5:
            lookup_line += para + ' ./5splitter.fst'
        elif v.get() == 6:
            lookup_line += ' -b' + para + ' ./6generation.fst'
    elif para == '-i':
        lookup_line += ' -b' + ' ./6generation.fst'
    result = subprocess.check_output(lookup_line, shell=True)
    result = result.decode('utf-8')
    #result = result.replace("\r", "\n")

    #print(result)
    #f2 = open('./output_text.txt', 'w+', encoding='utf-8')
    #f2.write(result)
    #f2.close()
    #textarea.insert(END, word+"\n");
    cmds.append(word)
    pointer = len(cmds)-1
    return result

def read_word(event):
	#print(var.get())
	text_contents = box.get()
	returnedresult = lookup(text_contents)
	rules = list(set(returnedresult.split("\n")))
	out = ""
	for rule in rules:
		if rule.strip() != '':
			rule = rule.replace("\t", "\t       \t")
			out += rule + "\n"
	#if repvar.get() == 1:
	if 1 == 1:
		textarea.insert(END, out+"\n", 'tag-right')
	else:
		textarea.insert(END, lookup(text_contents), 'tag-right')
	textarea.see("end")
	box.delete(0,END)
	pointer = len(cmds)-1
def history_up(event):
	#print("hi")
	if len(cmds) == 0:
		return
	if math.fabs(p.pointer) >= len(cmds):
		p.pointer = 0
	p.pointer = p.pointer - 1
	box.delete(0,END)
	box.insert(0, cmds[p.pointer])

def history_down(event):
	#print("hi")
	#print(p.pointer)
	if len(cmds) == 0:
		return
	if math.fabs(p.pointer) > (len(cmds)-1):
		p.pointer = 0
	box.delete(0,END)
	box.insert(0, cmds[p.pointer])
	p.pointer = p.pointer + 1

#topframe = Frame(mframe).grid(row=2, column=0, rowspan=6 , padx=2, pady=5, sticky=N)
#bottomframe = Frame(mframe).pack(side=BOTTOM, anchor=S)
lbl = Label(mframe, text=":ورودی", font = ('Tahoma', 10, 'bold'))#.pack(side=RIGHT)
lbl2 = Label(mframe, text="مبدل‌ها", font = ('Tahoma', 10, 'bold'))
lbl3 = Label(mframe, text="خروجی", font = ('Tahoma', 10, 'bold'))
#lbl4 = Label(mframe, text=" ghrtyrtyyryryrtyyryryryrtyf", font = ('Tahoma', 10))
box = Entry(mframe, width=60, font = ('Tahoma', 12), justify='right')
box.grid(row=0, column=0, columnspan=2, sticky=E, pady=5, padx=1)
lbl.grid(row=0, column=2)
lbl2.grid(row=1, column=2)
lbl3.grid(row=1, column=0, columnspan=2)
#lbl4.grid(row=3, column=0, columnspan=3)
#box.pack(side=TOP, expand=True, anchor=N)
box.bind('<Return>', read_word)
box.bind('<Up>', history_up)
box.bind('<Down>', history_down)
box.focus_set()
textarea = Text(mframe, font=("Tahoma", 12), width=60, height=10)#.pack(side=RIGHT)
textarea.grid(row=2, column=1, rowspan=6, pady=5, sticky=N+W)
textarea.tag_configure('tag-right', justify='right')

scrollbar = Scrollbar(mframe, orient=VERTICAL)#.pack(side=RIGHT)


checkbox = Checkbutton(
    mframe, text="حذف فاصله و نيم فاصله",
    variable=var,
    )
checkbox2 = Checkbutton(
    mframe, text="حذف قاعده هاي تکراري",
    variable=repvar,
    )



scrollbar.grid(row=2, column=0, rowspan=6, pady=5, sticky=N+S+W)
'''
checkbox.grid(row=0, column=1)
box.grid(row=0, column=0)
textarea.grid(row=1, column=0)
'''
#hsep = Separator(mframe,orient=HORIZONTAL).grid(row=1, column=0, coumnspan=2, sticky="ew")

#box.grid(row=0)
#checkbox.pack(side=TOP)
#checkbox2.pack(side=TOP)
#canvas = Canvas(mframe)
#canvas.pack(side="left", fill="both", expand=True)
#buttonframe = Frame(mframe).pack(anchor=W, side=TOP, fill='both', expand=False)

#buttonframe.grid(row=1, column=0)
standard = Radiobutton(mframe, text="استاندارد", variable=v, value=1, indicatoron=0, width=7, font = ('Tahoma', 12))#.pack(anchor=N, side=TOP)
standard.grid(row=2, column=2, pady=0, padx=4)
homophone = Radiobutton(mframe, text="همصدا", variable=v, value=2, indicatoron=0, width=7, font = ('Tahoma', 12))#.pack(anchor=N, side=TOP)
homophone.grid(row=3, column=2, pady=0, padx=4)
avaee = Radiobutton(mframe, text="آوایی", variable=v, value=3, indicatoron=0, width=7, font = ('Tahoma', 12))#.pack(anchor=N, side=TOP)
avaee.grid(row=4, column=2, pady=0, padx=4)
expressive = Radiobutton(mframe, text="بیانی", variable=v, value=4, indicatoron=0, width=7, font = ('Tahoma', 12))#.pack(anchor=N, side=TOP)
expressive.grid(row=5, column=2, pady=0, padx=4)
splitter = Radiobutton(mframe, text="تقطیع", variable=v, value=5, indicatoron=0, width=7, font = ('Tahoma', 12))#.pack(anchor=N, side=TOP)
splitter.grid(row=6, column=2, pady=0, padx=4)
generation = Radiobutton(mframe, text="تولید", variable=v, value=6, indicatoron=0, width=7, font = ('Tahoma', 12))#.pack(anchor=N, side=TOP)
generation.grid(row=7, column=2, pady=0, padx=4)
#scrollbar.pack(side=RIGHT, fill=Y)
#textarea.pack(side=BOTTOM, expand=True, fill=BOTH, anchor=S)

#font = ('times', 14, 'bold'),

textarea.configure(yscrollcommand=scrollbar.set)
scrollbar.config(command=textarea.yview)

#mframe.geometry("600x400")
var.set(0)
v.set(1)
mframe.resizable(False, False)
make_menu(mframe)
textarea.bind_class("Text", "<Button-3><ButtonRelease-3>", show_menu)
box.bind_class("Entry", "<Button-3><ButtonRelease-3>", show_menu)
mframe.mainloop()
