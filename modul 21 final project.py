from tkinter import *
from tkinter import messagebox, filedialog
import random




# ----------------- FUNKCIJE POJEDINAČNIH APLIKACIJA -----------------

def open_calculator():
    calc = Toplevel(root)
    calc.title('Kalkulator')
    calc.geometry('350x400')
    calc.config(bg='#2e2e2e')

    entry = Entry(calc, width=16, font=('Arial', 24), bd=10, relief=RIDGE, justify=RIGHT)
    entry.grid(row=0, column=0, columnspan=4, pady=10)

    def klik(t):
        entry.insert(END, t)

    def izracunaj():
        try:
            rezultat = eval(entry.get())
            entry.delete(0, END)
            entry.insert(0, str(rezultat))
        except:
            entry.delete(0, END)
            entry.insert(0, 'Greška')

    def obrisi():
        entry.delete(0, END)

    dugmad = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '=', '+')
    ]

    for i in range(4):
        for j in range(4):
            text = dugmad[i][j]
            if text == "=":
                btn = Button(calc, text=text, width=5, height=2, font=("Arial", 18), command=izracunaj)
            else:
                btn = Button(calc, text=text, width=5, height=2, command=lambda t=text: klik(t), font=("Arial", 18))
            btn.grid(row=i+1, column=j, padx=5, pady=5)

    Button(calc, text='C', width=22, height=2, command=obrisi, font=("Arial", 14)).grid(row=5, column=0, columnspan=4, pady=10)

def open_hangman():
    hang = Toplevel(root)
    hang.title("Hangman")
    hang.geometry("400x300")
    hang.config(bg="#2b2b2b")

    rijeci = ["python", "banana", "hangman", "program", "skola", "igra", "telefon", "racunar"]
    tajna_rijec = random.choice(rijeci)
    pogodjeno = ["_" for slovo in tajna_rijec]
    pokusaji = [6]

    label_rijec = Label(hang, text=" ".join(pogodjeno), font=("Arial", 24), bg="#2b2b2b", fg="white")
    label_rijec.pack(pady=20)

    label_info = Label(hang, text="Unesi slovo:", font=("Arial", 14), bg="#2b2b2b", fg="white")
    label_info.pack()

    unos = Entry(hang, font=("Arial", 14), justify="center")
    unos.pack()

    rezultat = Label(hang, text=f"Pokušaji: {pokusaji[0]}", font=("Arial", 14), bg="#2b2b2b", fg="white")
    rezultat.pack(pady=10)

    def provjeri():
        slovo = unos.get().lower()
        unos.delete(0, END)

        if not slovo or len(slovo) != 1 or not slovo.isalpha():
            rezultat.config(text="Unesi jedno slovo!")
            return

        if slovo in tajna_rijec:
            for i in range(len(tajna_rijec)):
                if tajna_rijec[i] == slovo:
                    pogodjeno[i] = slovo
            label_rijec.config(text=" ".join(pogodjeno))
        else:
            pokusaji[0] -= 1
            rezultat.config(text=f"Pokušaji: {pokusaji[0]}")

        if "_" not in pogodjeno:
            rezultat.config(text="Bravo! Pogodio si riječ.")
        elif pokusaji[0] == 0:
            label_rijec.config(text=tajna_rijec)
            rezultat.config(text="Izgubio si!")
        

    dugme_provjeri = Button(hang, text="Pogodi", font=("Arial", 14), command=provjeri)
    dugme_provjeri.pack(pady=10)
   

def open_notepad():
    notes = Toplevel(root)
    notes.title("Notepad")
    notes.geometry("600x400")

    text_area = Text(notes, font=("Arial", 12))
    text_area.pack(expand=True, fill=BOTH)

    def save_file():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, END))

    btn_save = Button(notes, text="Sačuvaj", command=save_file)
    btn_save.pack()

def open_memory_game():
    mem = Toplevel(root)
    mem.title("Memory Game")
    mem.geometry("400x400")
    mem.config(bg="#1e1e2f")

    simboli = list("AABBCCDDEEFFGGHH")
    random.shuffle(simboli)
    prikazano = [False]*16
    dugmad = []
    prvi = [None]
    drugi = [None]

    def otkrij(index):
        if prikazano[index] or drugi[0] is not None:
            return
        dugmad[index].config(text=simboli[index])
        if prvi[0] is None:
            prvi[0] = index
        else:
            drugi[0] = index
            mem.after(1000, provjeri)

    def provjeri():
        if simboli[prvi[0]] == simboli[drugi[0]]:
            prikazano[prvi[0]] = True
            prikazano[drugi[0]] = True
        else:
            dugmad[prvi[0]].config(text="?")
            dugmad[drugi[0]].config(text="?")
        prvi[0] = None
        drugi[0] = None

    for i in range(16):
        btn = Button(mem, text="?", width=6, height=3,
                     command=lambda i=i: otkrij(i), font=("Arial", 14))
        btn.grid(row=i//4, column=i%4, padx=5, pady=5)
        dugmad.append(btn)

def open_quiz():
    quiz = Toplevel(root)
    quiz.title("Kviz")
    quiz.geometry("400x300")

    pitanja = [
        ("Koji je glavni grad Francuske?", "Pariz"),
        ("Koliko je 7 + 5?", "12"),
        ("Koja boja nastaje miješanjem plave i žute?", "Zelena")
    ]

    index = [0]
    score = [0]

    label = Label(quiz, text=pitanja[0][0], font=("Arial", 14))
    label.pack(pady=20)

    entry = Entry(quiz, font=("Arial", 14))
    entry.pack()

    rezultat = Label(quiz, text="", font=("Arial", 12))
    rezultat.pack(pady=10)

    def provjeri_odgovor():
        odgovor = entry.get().strip().lower()
        tacan = pitanja[index[0]][1].strip().lower()

        if odgovor == tacan:
            score[0] += 1
            rezultat.config(text="Tačno!")
        else:
            rezultat.config(text=f"Netačno. Odgovor: {pitanja[index[0]][1]}")

        index[0] += 1
        entry.delete(0, END)

        if index[0] < len(pitanja):
            label.config(text=pitanja[index[0]][0])
        else:
            label.config(text=f"Kraj kviza! Rezultat: {score[0]}/{len(pitanja)}")
            entry.destroy()

    Button(quiz, text="Dalje", command=provjeri_odgovor).pack()

def open_click_counter():
    win = Toplevel(root)
    win.title("Brojač Klikova")
    win.geometry("300x200")

    broj = [0]
    label = Label(win, text=f"Klikova: {broj[0]}", font=("Arial", 18))
    label.pack(pady=20)

    def klikni():
        broj[0] += 1
        label.config(text=f"Klikova: {broj[0]}")

    Button(win, text="Klikni me!", font=("Arial", 16), command=klikni).pack()

# ----------------- GLAVNI PROZOR -----------------

def start_main_window():
    global root
    root = Tk()
    root.title('App Center Mini')
    root.geometry('400x600')
    root.config(bg='#1e1e2f')

    dugmad = [
        ("Kalkulator", open_calculator),
        ("Hangman", open_hangman),
        ("Notepad", open_notepad),
        ("Memory Game", open_memory_game),
        ("Kviz", open_quiz),
        ("Brojač klikova", open_click_counter)
    ]

    for text, command in dugmad:
        Button(root, text=text, width=20, height=3, command=command, font=("Arial", 14)).pack(pady=10, fill=X, padx=40)

    root.mainloop()

# ----------------- SPLASH SCREEN -----------------

splash = Tk()
splash.title("Dobrodošli")
splash.geometry("400x300")
splash.config(bg="#222222")

Label(splash, text="NAPRAVIO: Faruk", font=("Arial", 18), fg="white", bg="#222222").pack(pady=30)
Label(splash, text="BETA verzija 1.0", font=("Arial", 14), fg="gray", bg="#222222").pack()
Label(splash, text="Sadrži mini aplikacije i igre", font=("Arial", 12), fg="lightgray", bg="#222222").pack(pady=10)

def start_main_app():
    splash.destroy()
    start_main_window()

splash.after(3000, start_main_app)
splash.mainloop()
