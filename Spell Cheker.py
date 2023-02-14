from tkinter import *
from textblob import TextBlob


def check_word(event=None):
    word = spell_check.get()
    if len(word) == 0:
        return

    last_word = word.split()[-1]
    if last_word:
        text = TextBlob(last_word)
        if text.correct() != last_word:
            spell_check.configure(fg='red')
        else:
            spell_check.configure(fg='black')


def check_spelling():
    global spell_labels
    a = TextBlob(spell_check.get())
    spell = Label(window, text="Correct Spelling:", font=("System", 15, "bold"), bg="#5dd39e")
    spell.place(x=40, y=290 + (25 * len(spell_labels)))
    correct_text = Label(window, text=str(a.correct()), font=("Georgia", 15, "bold"), bg="#ebebeb")
    correct_text.place(x=190, y=290 + (25 * len(spell_labels)))
    spell_labels.append(spell)
    spell_labels.append(correct_text)


def clear_output():
    spell_check.delete(0, 'end')
    spell_check.configure(fg='black')
    for label in spell_labels:
        label.place_forget()
    spell_labels.clear()


window = Tk()
window.title("Spelling Checker")
window.geometry("800x600")
window.config(background="#ebebeb")

text_heading = Label(window, text="Spelling Checker", font=("Georgia", 40, "bold italic"), bg="#3a6ea5", fg="white", padx="20", pady="20")
text_heading.pack(pady=30)

text_check = Label(window, text="Enter the word: ", font=("System", 15, "bold"), bg="#ebebeb")
text_check.place(x=40, y=190)

spell_check = Entry(window, font=("Georgia", 31, "bold"), bg="#c0c0c0")
spell_check.place(x=40, y=220, width=550)
spell_check.bind('<KeyRelease>', check_word)

spell_labels = []

Check_button = Button(window, text="Check", font=("Impact", 18), fg="white", bg="#3a6ea5", command=check_spelling)
Check_button.place(x=595, y=220)

clear_button = Button(window, text="Clear", font=("Impact", 18), fg="white", bg="#3a6ea5", command=clear_output)
clear_button.place(x=685, y=220)

window.mainloop()
