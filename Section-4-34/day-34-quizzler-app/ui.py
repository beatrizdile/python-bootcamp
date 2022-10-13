from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Question", width=280,
                                                     fill=THEME_COLOR, font=("Arial", 15))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        no_button_img = PhotoImage(file="images/false.png")
        self.no_button = Button(image=no_button_img, highlightthickness=0, command=self.false_answer)
        self.no_button.grid(row=2, column=1)

        yes_button_img = PhotoImage(file="images/true.png")
        self.yes_button = Button(image=yes_button_img, highlightthickness=0, command=self.true_answer)
        self.yes_button.grid(row=2, column=0)

        self.score = Label(text="Score: 0", font=("Arial", 25, "bold"), fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")

    def true_answer(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

