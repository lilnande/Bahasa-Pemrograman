from tkinter import *
window = Tk()
window.title("Aplikasi Kalkulator GUI Di Python")
''
lbl = Label(window, text="Masukan Nilai Pertama : ",anchor="e",width=20)
lbl.grid(column=0, row=0)
nilail = Entry(window,width=10)
nilail.grid(column=1,row=0)
lb12 = Label(window, text="Masukan Nilai Kedua : ",anchor="e",width=20)
lb12.grid(column=0, row=1)
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=1)
lb13 = Label(window, text="Hasil : ",anchor="e",width=20)
lb13.grid(column=0, row=2)
hasil = Label(window, text="0",anchor="w",width=10)
hasil.grid(column=1, row=2)
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))

def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))

def kali():
    hasil.configure(text=(int(nilail.get())*int(nilai2.get())))

def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))

btn = Button(window, text="Tambah", command=tambah)
btn.grid(column=0, row=3)

btn = Button(window, text="Kurang", command=kurang)
btn.grid(column=1, row=3)

btn = Button(window, text="Kali", command=kali)
btn.grid(column=0, row=4)

btn = Button(window, text="Bagi", command=bagi)
btn.grid(column=1, row=4)

window.mainloop()