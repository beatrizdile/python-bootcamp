from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#42855B"
GREENER = "#42855B"
OTHER_GREEN = "#90B77D"
REDDER = "#C21010"
OTHER_RED = "#EC7272"
BROWN = "#483838"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(bg=PINK, fg=RED, text="Timer")
    label_check.config(bg=PINK, text="")
    canvas.config(bg=PINK)
    window.config(bg=PINK)
    global REPS
    REPS = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    if REPS < 7:
        if REPS % 2 == 0:
            time_to_count = WORK_MIN * 60
            label_title.config(bg=OTHER_RED, text="Work", fg=REDDER)
            canvas.config(bg=OTHER_RED)
            window.config(bg=OTHER_RED)
            label_check.config(bg=OTHER_RED)
            REPS += 1
        else:
            time_to_count = SHORT_BREAK_MIN * 60
            label_title.config(bg=OTHER_GREEN, text="Break", fg=GREENER)
            canvas.config(bg=OTHER_GREEN)
            window.config(bg=OTHER_GREEN)
            label_check.config(bg=OTHER_GREEN)
            REPS += 1
    else:
        time_to_count = LONG_BREAK_MIN * 60
        label_title.config(bg=OTHER_GREEN, text="Big Break", fg=GREENER)
        canvas.config(bg=OTHER_GREEN)
        window.config(bg=OTHER_GREEN)
        label_check.config(bg=OTHER_GREEN)
        REPS = 0
    count_down(int(time_to_count))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if int(count_sec) == 0:
        count_sec = "00"
    elif int(count_sec) < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count >= 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check = "✔ "
        new_check = ""
        for _ in range(int(math.floor(REPS/2))):
            new_check += check
        label_check.config(text=new_check)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(width=, height=)
window.config(padx=100, pady=50, bg=PINK)

canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

label_title = Label(text="Timer", bg=PINK, fg=RED, font=(FONT_NAME, 22, "bold"))
label_title.grid(column=1, row=0)

label_check = Label(bg=PINK, fg=GREEN, font=(FONT_NAME, 15, "bold"))
label_check.grid(column=1, row=3)

but_start = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=start_timer)
but_start.grid(column=0, row=2)

but_restart = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=reset_timer)
but_restart.grid(column=2, row=2)


window.mainloop()
