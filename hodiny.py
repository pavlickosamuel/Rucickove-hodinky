import math, tkinter as tk, datetime as dt

win = tk.Tk()
win.title("Hodiny")
canvas = tk.Canvas(win, width=800, height=800, bg="white")
canvas.pack()

s1, s2 = 400, 400
kratka_ruc = 90
dlha_ruc = 150
hrubka_h = 3
hrubka_s = 1

canvas.create_oval(s1-200, s2-200, s1+200, s2+200, outline="black", width=3)
for i in range(1, 13):
    uhol = math.radians(i * 30 - 90)
    x = s1 + 175 * math.cos(uhol)
    y = s2 + 175 * math.sin(uhol)
    canvas.create_text(x, y, text=str(i), font=("Arial", 16, "bold"))

rucicka_minuta  = canvas.create_line(s1, s2, s1, s2 - dlha_ruc,  width=hrubka_h, fill="black")
rucicka_hodina  = canvas.create_line(s1, s2, s1, s2 - kratka_ruc, width=hrubka_h, fill="black")
rucicka_sekunda = canvas.create_line(s1, s2, s1, s2 - dlha_ruc,  width=hrubka_s, fill="red")

def draw():
    cas = dt.datetime.now()

    uhol_m = math.radians(cas.minute * 6 - 90)
    canvas.coords(rucicka_minuta, s1, s2, s1 + dlha_ruc * math.cos(uhol_m), s2 + dlha_ruc * math.sin(uhol_m))

    uhol_h = math.radians(cas.hour * 30 + cas.minute * 0.5 - 90)
    canvas.coords(rucicka_hodina, s1, s2, s1 + kratka_ruc * math.cos(uhol_h), s2 + kratka_ruc * math.sin(uhol_h))

    uhol_s = math.radians(cas.second * 6 - 90)
    canvas.coords(rucicka_sekunda, s1, s2, s1 + dlha_ruc * math.cos(uhol_s), s2 + dlha_ruc * math.sin(uhol_s))
    
    canvas.after(1000, draw)

draw()
win.mainloop()