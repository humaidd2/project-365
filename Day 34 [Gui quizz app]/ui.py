from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_text = Label(text="Score: 0", pady=20, padx=30, bg=THEME_COLOR, fg="white")
        self.score_text.grid(column=2, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="somthing", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR, width=280)
        self.canvas.grid(column=1, row=1, columnspan=2, pady=50)

        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=1, row=2)

        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.ans_false)
        self.wrong_button.grid(column=2, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You have come to the end of the quiz")
            self.right_button.config(state="disabled")
            self.ans_false().config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def ans_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(background="green")
        else:
            self.canvas.configure(background="red")

        self.window.after(1000, self.get_next_question)
