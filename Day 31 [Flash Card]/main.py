import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
chosen_word = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def random_word():
    global chosen_word
    chosen_word = random.choice(words)
    french_word = chosen_word["French"]
    english_word = chosen_word["English"]
    canvas.itemconfig(canvas_image, image=old_img)
    canvas.itemconfig(language_select, text="French")
    canvas.itemconfig(display_word, text=french_word)
    window.after(3000, flip_card, english_word)


def flip_card(english_word):
    new_img = PhotoImage(file="./images/card_back.png")
    canvas.itemconfig(canvas_image, image=new_img)
    canvas.itemconfig(language_select, text="English")
    canvas.itemconfig(display_word, text=english_word)


def is_known():
    try:
        words.remove(chosen_word)
    except ValueError:
        pass
    else:
        to_learn_df = pandas.DataFrame(words)
        to_learn_df.to_csv("data/words_to_learn.csv", index=False)
    finally:
        random_word()


""""""""""""""""""
window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800)
old_img = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 264, image=old_img)
language_select = canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
display_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_word)
wrong_button.grid(column=0, row=1)

window.mainloop()
