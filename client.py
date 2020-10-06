import sys
import tkinter as tk
import tkinter.ttk as ttk
import platform
import powwow_main_support

py3 = True


# Starting point when module is the main routine.
def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    powwow_main_support.set_Tk_var()
    top = POWWOW(root)
    powwow_main_support.init(root, top)
    root.mainloop()


w = None


# Starting point when module is imported by another module.
# Correct form of call: 'create_POWWOW(root, *args, **kwargs)' .
def create_POWWOW(rt, *args, **kwargs):
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel(root)
    powwow_main_support.set_Tk_var()
    top = POWWOW(w)
    powwow_main_support.init(w, top, *args, **kwargs)
#    return (w, top)


def destroy_POWWOW():
    global w
    w.destroy()
    w = None


class POWWOW:
    def __init__(self, top=None):
        # This class configures and populates the toplevel window.
        # top is the toplevel containing window.
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Microsoft YaHei UI} -size 20"
        font9 = "-family {Microsoft YaHei UI} -size 18 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1600x900+160+40")
        top.minsize(196, 16)
        top.maxsize(1940, 1066)
        top.resizable(False, False)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.chat_print = ScrolledText(top)
        self.chat_print.place(relx=0.006, rely=0.011, relheight=0.88, relwidth=0.25)
        self.chat_print.configure(background="white")
        self.chat_print.configure(font="TkTextFont")
        self.chat_print.configure(foreground="black")
        self.chat_print.configure(highlightbackground="#d9d9d9")
        self.chat_print.configure(highlightcolor="black")
        self.chat_print.configure(insertbackground="black")
        self.chat_print.configure(insertborderwidth="3")
        self.chat_print.configure(selectbackground="blue")
        self.chat_print.configure(selectforeground="white")
        self.chat_print.configure(wrap="none")

        self.chat_input = tk.Entry(top)
        self.chat_input.place(relx=0.006, rely=0.9, height=74, relwidth=0.2)
        self.chat_input.configure(background="white")
        self.chat_input.configure(cursor="fleur")
        self.chat_input.configure(disabledforeground="#a3a3a3")
        self.chat_input.configure(font="TkFixedFont")
        self.chat_input.configure(foreground="#000000")
        self.chat_input.configure(highlightbackground="#d9d9d9")
        self.chat_input.configure(highlightcolor="black")
        self.chat_input.configure(insertbackground="black")
        self.chat_input.configure(selectbackground="blue")
        self.chat_input.configure(selectforeground="white")

        self.chat_submit = tk.Button(top)
        self.chat_submit.place(relx=0.213, rely=0.9, height=80, width=70)
        self.chat_submit.configure(activebackground="#ececec")
        self.chat_submit.configure(activeforeground="#000000")
        self.chat_submit.configure(background="#d9d9d9")
        self.chat_submit.configure(disabledforeground="#a3a3a3")
        self.chat_submit.configure(foreground="#000000")
        self.chat_submit.configure(highlightbackground="#d9d9d9")
        self.chat_submit.configure(highlightcolor="black")
        self.chat_submit.configure(pady="0")
        self.chat_submit.configure(text='''Send''')

        self.display_whose_turn = tk.Label(top)
        self.display_whose_turn.place(relx=0.263, rely=0.011, height=60, width=760)
        self.display_whose_turn.configure(background="#ffffff")
        self.display_whose_turn.configure(cursor="fleur")
        self.display_whose_turn.configure(disabledforeground="#a3a3a3")
        self.display_whose_turn.configure(font=font9)
        self.display_whose_turn.configure(foreground="#000000")
        self.display_whose_turn.configure(text='''player1234's turn''')

        self.guess = tk.Spinbox(top, from_=1.0, to=100.0)
        self.guess.place(relx=0.263, rely=0.767, relheight=0.111, relwidth=0.094)

        self.guess.configure(activebackground="#f9f9f9")
        self.guess.configure(background="white")
        self.guess.configure(buttonbackground="#d9d9d9")
        self.guess.configure(cursor="fleur")
        self.guess.configure(disabledforeground="#a3a3a3")
        self.guess.configure(font=font10)
        self.guess.configure(foreground="black")
        self.guess.configure(highlightbackground="black")
        self.guess.configure(highlightcolor="black")
        self.guess.configure(insertbackground="black")
        self.guess.configure(selectbackground="blue")
        self.guess.configure(selectforeground="white")
        self.guess.configure(textvariable=powwow_main_support.spinbox)

        self.game_status = tk.Label(top)
        self.game_status.place(relx=0.263, rely=0.089, height=600, width=760)
        self.game_status.configure(background="#000000")
        self.game_status.configure(disabledforeground="#a3a3a3")
        self.game_status.configure(foreground="#000000")
        self.game_status.configure(text='''current status of game''')

        self.submit_guess = tk.Button(top)
        self.submit_guess.place(relx=0.263, rely=0.889, height=90, width=150)
        self.submit_guess.configure(activebackground="#ececec")
        self.submit_guess.configure(activeforeground="#000000")
        self.submit_guess.configure(background="#d9d9d9")
        self.submit_guess.configure(cursor="fleur")
        self.submit_guess.configure(disabledforeground="#a3a3a3")
        self.submit_guess.configure(foreground="#000000")
        self.submit_guess.configure(highlightbackground="#d9d9d9")
        self.submit_guess.configure(highlightcolor="black")
        self.submit_guess.configure(pady="0")
        self.submit_guess.configure(text='''Submit Guess''')

        self.skill1 = tk.Button(top)
        self.skill1.place(relx=0.363, rely=0.767, height=150, width=100)
        self.skill1.configure(activebackground="#ececec")
        self.skill1.configure(activeforeground="#000000")
        self.skill1.configure(background="#d9d9d9")
        self.skill1.configure(cursor="fleur")
        self.skill1.configure(disabledforeground="#a3a3a3")
        self.skill1.configure(foreground="#000000")
        self.skill1.configure(highlightbackground="#d9d9d9")
        self.skill1.configure(highlightcolor="black")
        self.skill1.configure(pady="0")
        self.skill1.configure(text='''skill1''')

        self.skill2 = tk.Button(top)
        self.skill2.place(relx=0.431, rely=0.767, height=150, width=100)
        self.skill2.configure(activebackground="#ececec")
        self.skill2.configure(activeforeground="#000000")
        self.skill2.configure(background="#d9d9d9")
        self.skill2.configure(disabledforeground="#a3a3a3")
        self.skill2.configure(foreground="#000000")
        self.skill2.configure(highlightbackground="#d9d9d9")
        self.skill2.configure(highlightcolor="black")
        self.skill2.configure(pady="0")
        self.skill2.configure(text='''skill2''')

        self.skill3 = tk.Button(top)
        self.skill3.place(relx=0.5, rely=0.767, height=150, width=101)
        self.skill3.configure(activebackground="#ececec")
        self.skill3.configure(activeforeground="#000000")
        self.skill3.configure(background="#d9d9d9")
        self.skill3.configure(disabledforeground="#a3a3a3")
        self.skill3.configure(foreground="#000000")
        self.skill3.configure(highlightbackground="#d9d9d9")
        self.skill3.configure(highlightcolor="black")
        self.skill3.configure(pady="0")
        self.skill3.configure(text='''skill3''')

        self.score = tk.Label(top)
        self.score.place(relx=0.569, rely=0.767, height=200, width=271)
        self.score.configure(background="#d9d9d9")
        self.score.configure(disabledforeground="#a3a3a3")
        self.score.configure(foreground="#000000")
        self.score.configure(text='''Score''')

        self.reminder_skill = tk.Label(top)
        self.reminder_skill.place(relx=0.363, rely=0.944, height=38, width=320)
        self.reminder_skill.configure(activebackground="#f9f9f9")
        self.reminder_skill.configure(activeforeground="black")
        self.reminder_skill.configure(background="#d9d9d9")
        self.reminder_skill.configure(disabledforeground="#a3a3a3")
        self.reminder_skill.configure(foreground="#000000")
        self.reminder_skill.configure(highlightbackground="#d9d9d9")
        self.reminder_skill.configure(highlightcolor="black")
        self.reminder_skill.configure(text='''You can only use 1 skill / turn''')

        self.player1pic = tk.Label(top)
        self.player1pic.place(relx=0.744, rely=0.011, height=375, width=400)
        self.player1pic.configure(background="#ffffff")
        self.player1pic.configure(disabledforeground="#a3a3a3")
        self.player1pic.configure(foreground="#000000")
        self.player1pic.configure(text='''player1pic''')

        self.player1info = tk.Label(top)
        self.player1info.place(relx=0.744, rely=0.439, height=51, width=400)
        self.player1info.configure(background="#d9d9d9")
        self.player1info.configure(cursor="fleur")
        self.player1info.configure(disabledforeground="#a3a3a3")
        self.player1info.configure(foreground="#000000")
        self.player1info.configure(text='''player1info''')

        self.player2pic = tk.Label(top)
        self.player2pic.place(relx=0.744, rely=0.506, height=377, width=400)
        self.player2pic.configure(background="#ffffff")
        self.player2pic.configure(cursor="fleur")
        self.player2pic.configure(disabledforeground="#a3a3a3")
        self.player2pic.configure(foreground="#000000")
        self.player2pic.configure(text='''player2pic''')

        self.player2info = tk.Label(top)
        self.player2info.place(relx=0.744, rely=0.933, height=50, width=400)
        self.player2info.configure(background="#d9d9d9")
        self.player2info.configure(disabledforeground="#a3a3a3")
        self.player2info.configure(foreground="#000000")
        self.player2info.configure(text='''player2info''')


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


# Creates a ttk Frame with a given master, and use this new frame to
# place the scrollbars and the widget.
def _create_container(func):
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


# A standard Tkinter Text widget with scrollbars that will
# automatically show/hide as needed.
class ScrolledText(AutoScroll, tk.Text):
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
