import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
NEED_BREAK = False
CHECK = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    global NEED_BREAK
    if not NEED_BREAK:
        countdown(WORK_MIN * 60)
        REPS += 1
        if REPS == 4:
            countdown(LONG_BREAK_MIN * 60)
        NEED_BREAK = True
    else:
        countdown(SHORT_BREAK_MIN * 60)
        NEED_BREAK = False



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):

    global CHECK
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(10, countdown, count - 1)
    else:
        if not NEED_BREAK:
            CHECK += checkmark
            check_show.config(text=CHECK)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

checkmark = "✓"

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

timer = Label(text="Timer", font=("Times New Roman", 35, "normal"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

start_button = Button(text="Start", fg="white", bg=RED, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", fg="white", bg=RED, command=reset_timer)
reset_button.grid(column=2, row=2)

check_show = Label(text="", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg=PINK)
check_show.grid(column=1, row=3)

window.mainloop()
