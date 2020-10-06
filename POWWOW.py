from tkinter import *
from PIL import ImageTk, Image
from random import randint
import json
import subprocess
import client as clt


def open_rule_pdf():
    subprocess.Popen("./asset/PowWow Rule.pdf", shell=True)


def clicked(t1, t2, t3, btn):
    arg = [("ID", t1.get()), ("addr", t2.get()), ("port", t3.get())]
    launch_arg = json.dumps(dict(arg))
    print("Starting Client with arguments:", launch_arg)
    btn.configure(state=DISABLED)
    clt.create_POWWOW(window)
    # call client (main game)
    # set button to active after closing the client
    return 0


window = Tk()
window.title("PowWow Launcher")
window.geometry('560x360+280+180')
window.resizable(False, False)

img = ImageTk.PhotoImage(Image.open("./asset/POWWOW.png"))
title = Label(window, image=img)
title.grid(column=1, row=1)

label1 = Label(window, text="用户名：", font=("Courier", 12))
label1.grid(column=1, row=2)

text1 = Entry(window, width=16, font=("Courier", 12))
text1.grid(column=1, row=3)
text1.insert(END, 'player')
rand_int = randint(1000, 9999)
text1.insert(END, rand_int)

label2 = Label(window, text="服务器地址：", font=("Courier", 12))
label2.grid(column=1, row=4)

text2 = Entry(window, width=16, font=("Courier", 12))
text2.grid(column=1, row=5)
text2.insert(END, '192.168.0.101')

label3 = Label(window, text="服务器端口：", font=("Courier", 12))
label3.grid(column=1, row=6)

text3 = Entry(window, width=16, font=("Courier", 12))
text3.grid(column=1, row=7)
text3.insert(END, '5555')

rule_btn = Button(window, text="规则说明.pdf", font=("Courier", 12), borderwidth=0,command=open_rule_pdf)
rule_btn.grid(column=1, row=8)

btn_raw = Image.open("./asset/start.png")
btn_raw = btn_raw.resize((109, 25), Image.ANTIALIAS)

btn_img = ImageTk.PhotoImage(btn_raw)
button = Button(window, image=btn_img, borderwidth=0,
                command=lambda: clicked(text1, text2, text3, button))
button.grid(column=1, row=10)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(9, weight=1)
window.grid_rowconfigure(11, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(2, weight=1)

window.mainloop()