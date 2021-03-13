from random import randint, choice
from tkinter import *
import pandas as pd


BACKGROUND_COLOR = "#B1DDC6"
#❌ ✅

#----------------DATA ---------------#

current_card = {}
to_learn = {}

try:
# Read data from csv
    data_file = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records") 




def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    # Parses dictionary to find a random French word
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

#----------------Cards ---------------#

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)

    next_card()



#----------------UI-----------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text=" ", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text=" ", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#----------------UBUTTONS----------------#

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)


right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=known)
right_button.grid(column=1, row=1)


window.after(0, next_card())

window.mainloop()
