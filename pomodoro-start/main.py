from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_run = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(timer_run)
    timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        timer.config(text="Work")
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer_run
    min_count = math.floor(count / 60)
    sec_count = count % 60
    if sec_count < 10:
        sec_count = f"0{sec_count}"
    canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}")
    if count > 0:
        timer_run = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            check = ""
            for _ in range(math.floor(reps/2)):
                check += "✔"
                check_marks.config(text=f"{check}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=206, height=300, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(103, 150, image=tomato_pic)
timer_text = canvas.create_text(103, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

timer = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
timer.place(x=55, y=0)

check_marks = Label(bg=YELLOW, highlightthickness=0, fg=GREEN)
check_marks.place(x=95, y=300)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.place(x=-25, y=300)


reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.place(x=165, y=300)


window.mainloop()