from tkinter import *
from tkinter import messagebox

langas = Tk()
langas.geometry("450x260")
langas.title("Atlyginimo skačiuoklė")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

mokesciai = []
# tikriname įvestį
def tikrinti():
    try:
        ivesta = float(ivesta_ivestis.get())
        if ivesta < 0:
            messagebox.showerror("Klaida", "Atlyginimas negali būti neigiamas!")
            langas.destroy()
    except ValueError:
        messagebox.showerror("Klaida", "Klaidingai įvedėte atlyginimą")
        langas.destroy()

def gpm():
#skaičiuojam gpm įmoką, jeigu tai pagrindinė darbovietė
    ivesta = float(ivesta_ivestis.get())

    if (var1.get() == 1) & (var2.get() == 0):

        if ivesta >= 1679:
            gpm_imoka = (ivesta - (400 - 0.18 * (ivesta - 642))) * 0.2
            gpm_imoka_round = round(gpm_imoka, 2)
            mokesciai.append(gpm_imoka_round)
            result1 = Label(langas, text = f"Gyventojų pajamų mokesčio įmoka:{gpm_imoka_round} eur")
            result1.grid(row=6, columnspan=2, sticky=W)
        elif ivesta <= 1678 and ivesta >= 730:
            gpm_imoka = (ivesta - (460 - 0.26 * (ivesta - 730))) * 0.2
            gpm_imoka_round = round(gpm_imoka, 2)
            mokesciai.append(gpm_imoka_round)
            result1 = Label(langas, text=f"Gyventojų pajamų mokesčio įmoka:{gpm_imoka_round} eur")
            result1.grid(row=6, columnspan=2, sticky=W)
        elif ivesta <= 729 and ivesta >= 461:
            gpm_imoka = (ivesta - 460) * 0.2
            gpm_imoka_round = round(gpm_imoka, 2)
            mokesciai.append(gpm_imoka_round)
            result1 = Label(langas, text=f"Gyventojų pajamų mokesčio įmoka:{gpm_imoka_round} eur")
            result1.grid(row=6, columnspan=2, sticky=W)
        elif ivesta < 461:
            result1 = Label(langas, text= "Gyventojų pajamų mokesčio įmoka: 0.00 eur")
            result1.grid(row=6, columnspan=2, sticky=W)

 #skaičiuojam gpm įmoką, jeigu tai nepagrindinė darbovietė

    elif (var1.get() == 0) & (var2.get() == 1):

        gpm_imoka = ivesta  * 0.2
        gpm_imoka_round = round(gpm_imoka, 4)
        mokesciai.append(gpm_imoka_round)
        result1 = Label(langas, text=f"Gyventojų pajamų mokesčio įmoka: {gpm_imoka_round} eur")
        result1.grid(row=6, columnspan=2, sticky=W)

    else:
        messagebox.showerror("Klaida", "Suklydote pažymėdami varnelę")
        langas.destroy()

# priklausomai nuo pasirinkimo, skaičiuojame pensijų kaupimo įmoką
def pensija():
    ivesta = float(ivesta_ivestis.get())

    if (var3.get() == 1) & (var4.get() == 0) & (var5.get() == 0):
        pensiju_imoka = ivesta * 0.00
        mokesciai.append(pensiju_imoka)
        result2 = Label(langas, text=f"Papildoma įmoka pensijų kaupimui: {pensiju_imoka} eur")
        result2.grid(row=7, columnspan=2, sticky=W)


    elif (var3.get() == 0) & (var4.get() == 1) & (var5.get() == 0):
        pensiju_imoka = round(ivesta * 0.027, 2)
        mokesciai.append(pensiju_imoka)
        result2 = Label(langas, text = f"Papildoma įmoka pensijų kaupimui: {pensiju_imoka} eur")
        result2.grid(row=7, columnspan=2, sticky=W)


    elif (var3.get() == 0) & (var4.get() == 0) & (var5.get() == 1):
        pensiju_imoka = round(ivesta * 0.03, 2)
        mokesciai.append(pensiju_imoka)
        result2 = Label(langas, text=f"Papildoma įmoka pensijų kaupimui: {pensiju_imoka} eur")
        result2.grid(row=7, columnspan=2, sticky=W)

    else:
        messagebox.showerror("Klaida", "Suklydote pažymėdami varnelę")
        langas.destroy()


def sodra():
    ivesta = float(ivesta_ivestis.get())
# suskaičiuojam psd įmoką
    psd_imoka = round(ivesta * 0.0698, 2)
    mokesciai.append(psd_imoka)
    result3 = Label(langas, text=f"Privalomojo sveikatos draudimo įmoka: {psd_imoka} eur")
    result3.grid(row=4, columnspan=3, sticky=W)
# suskaičiuojam įmoką sodrai
    vsd_imoka = round(ivesta * 0.1252, 2)
    mokesciai.append(vsd_imoka)
    result4 = Label(langas, text=f"Darbuotojo įmoka sodrai: {vsd_imoka} eur")
    result4.grid(row=5, columnspan=2, sticky=W)

# į rankas išmokama suma
def i_rankas():
    ivesta = float(ivesta_ivestis.get())

    atlyginimas_i_rankas = round(ivesta - sum(mokesciai), 2)
    result5["text"]=f"Jums išmokamas atlyginimas 'į rankas' eurais: {atlyginimas_i_rankas}"
    result5.grid(row=10, columnspan=3, sticky=W)
    statusbar["text"] = "Jūsų mokesčiai suskaičiuoti"

# išvalome mokesčių listą
def clear():
    mokesciai.clear()

# uždarome programą
def uzdaryti():
    langas.destroy()

# suformuojame langą
ivesta = Label(langas, text ="Įveskite atlyginimą ant popieriaus: ")
ivesta_ivestis = Entry(langas)
ivesta2 = Label(langas, text ="Ar tai jūsų pagrindinė darbovietė: ")
ivesta3 = Label(langas, text ="Kiek kaupiate papildomai pensijai: ")
result5 = Label(langas, text="", foreground= "blue")

# suformuojame pasirinkimo galimybes
Checkbutton(langas, text="Taip", variable=var1).grid(row=1, column = 1, sticky=W)
Checkbutton(langas, text="Ne", variable=var2).grid(row=1, column = 2, sticky=W)
Checkbutton(langas, text="0.0%", variable=var3).grid(row=2, column = 1, sticky=W)
Checkbutton(langas, text="2.7%", variable=var4).grid(row=2, column = 2, sticky=W)
Checkbutton(langas, text="3.0%", variable=var5).grid(row=2, column = 3, sticky=W)

# suformuojame mygtukus
all_commands = lambda: [tikrinti(), gpm(), pensija(), sodra(), i_rankas(), clear()]
mygtukas = Button(langas, text="Patvirtinkite",  command = all_commands)
mygtukas2= Button(langas, text="Išeiti",  command = uzdaryti)

# status juosta
statusbar = Label(langas,text="",relief=RAISED, bg ="LightSteelBlue1", fg ="#00875F")

# "sudėliojam" langą
ivesta.grid(row=0, column=0, sticky=W)
ivesta_ivestis.grid(row = 0, columnspan=3, sticky=E)
ivesta2.grid(row=1, column=0, sticky=W)
ivesta3.grid(row=2, column=0, sticky=W)
mygtukas.grid(row=3, column=1)
mygtukas2.grid(row=3, column=3)
statusbar.grid(row=11, columnspan=4, sticky=E)
statusbar.config(width="35",anchor="w")

langas.mainloop()