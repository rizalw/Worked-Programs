from tkinter import *
import numpy as np

root = Tk()
root.title("Program Enkripsi / Dekripsi")
#root.iconbitmap(default = "favicon.ico")
#Declaration
dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

class hillChiper2x2():
    def __init__(self, kata, kunci, dictionary):
        self.kata = str(kata)
        self.kunci = str(kunci)
        self.dictionary = dictionary
    #Untuk membuat matriks 2x1
    def matrikskata(self):
        dictionary = self.dictionary
        kata = self.kata
        mtx_group = {}
        space = " "
        if len(kata) % 2 == 1:
            kata += space 
        interval = len(kata) // 2
        for x in range(interval):
            mtx_group["mtx {}".format(x)] = np.zeros((2,1))
            for y in range(2):
                mtx_group["mtx {}".format(x)][y, 0] = dictionary.index(kata[y + ( x * 2)])
        return mtx_group
    #Untuk membuat matriks 2x2
    def matrikskunci(self):
        kunci = self.kunci
        dictionary = self.dictionary
        matriks = np.zeros((2, 2))
        for x in range(2):
            for y in range(2):
                matriks[x, y] = dictionary.index(kunci[ y + ( x * 2 ) ])
        determinan = np.linalg.det(matriks)
        if determinan == 0.0:
            raise ValueError
        else:
            return matriks.astype(int)
    #Untuk membuat matriks invers modulo 26 2x2
    def matrikskunciinvers(self):
        mtx_kunci = self.matrikskunci()
        determinan = round(np.linalg.det(mtx_kunci))
        mtx_kunci_inv_normal = np.linalg.inv(mtx_kunci)
        for x in range(26):
            if (x * determinan) % 26 == 1:
                break
        det_inv = x
        mtx_kunci_inv = (mtx_kunci_inv_normal * determinan) * det_inv
        mtx_kunci_inv = np.remainder(mtx_kunci_inv, 26)
        return mtx_kunci_inv
    #Untuk membuat hash/ kata yang telah dienkripsi
    def enkripsi(self):
        output = []
        mtx_kunci = self.matrikskunci()
        mtx_group = self.matrikskata()
        dictionary = self.dictionary
        interval = len(self.kata) // 2
        for x in range(interval):
            mtx_group["mtx {}".format(x)] = mtx_kunci.dot(mtx_group["mtx {}".format(x)])
            mtx_group["mtx {}".format(x)] = mtx_group["mtx {}".format(x)] % 26
        for key, val in mtx_group.items():
            for x in range(2):
                output.append(dictionary[int(val[x, 0])])
        hasil = output
        view_enkripsi.delete(0, END)
        view_enkripsi.insert(0, "".join(hasil))
    #Untuk membuat kata dari hash/ sandi
    def dekripsi(self):
        output = []
        mtx_kunci_inv = self.matrikskunciinvers()
        mtx_group = self.matrikskata()
        dictionary = self.dictionary
        interval = len(self.kata) // 2
        for x in range(interval):
            mtx_group["mtx {}".format(x)] = mtx_kunci_inv.dot(mtx_group["mtx {}".format(x)])
            mtx_group["mtx {}".format(x)] = mtx_group["mtx {}".format(x)] % 26
        for key, val in mtx_group.items():
            for x in range(2):
                output.append(dictionary[int(val[x, 0])])
        hasil = output
        view_dekripsi.delete(0, END)
        view_dekripsi.insert(0, "".join(hasil))
class hillChiper3x3():
    def __init__(self, kata, kunci, dictionary):
        self.kata = kata
        self.kunci = kunci
        self.dictionary = dictionary
        if len(kata) ** 2 != len(kunci):
            raise IndexError
    #Untuk membuat matriks 3x1
    def matrikskata(self):
        kata = self.kata
        dictionary = self.dictionary
        matriks = np.zeros((3,1))
        for x in range(3):
            matriks[x, 0] = dictionary.index(kata[x])
        return matriks.astype(int)
    #Untuk membuat matriks 3x3
    def matrikskunci(self):
        kunci = self.kunci
        dictionary = self.dictionary
        matriks = np.zeros((3, 3))
        for x in range(3):
            for y in range(3):
                matriks[x, y] = dictionary.index(kunci[ y + ( x * 3 ) ])
        determinan = np.linalg.det(matriks)
        if determinan == 0.0:
            raise ValueError
        else:
            return matriks.astype(int)
    #Untuk membuat matriks invers modulo 26 3x3
    def matrikskunciinvers(self):
        mtx_kunci = self.matrikskunci()
        determinan = np.linalg.det(mtx_kunci)
        for coba in range(26):
            if (coba * determinan) % 26 == 1:
                break
        det_inv = coba
        mtx_kunci_invers = (np.linalg.inv(mtx_kunci)) * determinan * det_inv
        mtx_kunci_invers = np.remainder(mtx_kunci_invers, 26)
        return mtx_kunci_invers
    #Self-explanatory
    def enkripsi(self):
        output = []
        mtx_kata = self.matrikskata()
        mtx_kunci = self.matrikskunci()
        dictionary = self.dictionary
        hasil = mtx_kunci.dot(mtx_kata)
        hasil = np.remainder(hasil, 26)
        for x in range(3):
            output.append(hasil[x, 0])
            output[x] = dictionary[output[x]]
        hasil = output
        view_enkripsi.delete(0, END)
        view_enkripsi.insert(0, "".join(hasil))
    #Self-explanatory
    def dekripsi(self):
        output = []
        mtx_kata = self.matrikskata()
        mtx_kunci_invers = self.matrikskunciinvers()
        dictionary = self.dictionary
        hasil = mtx_kunci_invers.dot(mtx_kata)
        for x in range(3):
            output.append(hasil[x, 0])
            output[x] = round(output[x])
            output[x] = int(output[x] % 26)
            output[x] = dictionary[output[x]]
        hasil = output
        view_dekripsi.delete(0, END)
        view_dekripsi.insert(0, "".join(hasil))
def enkripsi():
    if metode.get() == "0":
        hillChiper2x2(kata.get(), kunci.get(), dictionary).enkripsi()
    elif metode.get() == "1":
        hillChiper3x3(kata.get(), kunci.get(), dictionary).enkripsi()    
    view_dekripsi.delete(0, END)
def dekripsi():
    if metode.get() == "0":
        hillChiper2x2(kata.get(), kunci.get(), dictionary).dekripsi()
    elif metode.get() == "1":
        hillChiper3x3(kata.get(), kunci.get(), dictionary).dekripsi()
    view_enkripsi.delete(0, END)
def reset():
    kata.delete(0, END)
    kunci.delete(0, END)
    view_enkripsi.delete(0, END)
    view_dekripsi.delete(0, END)
jenis = {
    ("Kunci 2x2", "0"),
    ("Kunci 3x3", "1")
}
metode = StringVar()
metode.set("0")
pilihan = LabelFrame(root)
Label(pilihan, text = "Jenis kunci").pack()
kata_label = Label(root, text = "Kata\t:", anchor = W, width = 15)
kata = Entry(root, width = 40)
kunci_label = Label(root, text = "Kunci\t:", anchor = W, width = 15)
kunci = Entry(root, width = 40)
title1 = Label(root, text = "PROGRAM ENKRIPSI / DEKRIPSI\n HILL CHIPER")
tombol_enkripsi = Button(root, text = "Enkripsi", command = enkripsi)
tombol_dekripsi = Button(root, text = "Dekripsi", command = dekripsi)
reset_button = Button(root, text = "Reset", command= reset, bg = "aqua", fg = "black", padx = 10)
view_enkripsi = Entry(root)
view_dekripsi = Entry(root)
out = Button(root, text = "Quit", command = root.destroy, bg = "red", fg = "white", padx = 10)
#Radio Button
for key, val in jenis:
    Radiobutton(pilihan, text = key, variable = metode, value = val, anchor = W, width = 20).pack()
#Placement
pilihan.grid(row = 0, column = 0)
kata_label.grid(row = 1, column = 0)
kata.grid(row = 1, column = 1, padx = 5, columnspan = 2)
kunci_label.grid(row = 2, column = 0)
kunci.grid(row = 2, column = 1, padx = 5, columnspan = 2)
title1.grid(row = 0, column = 1)
tombol_enkripsi.grid(row = 3,column = 0)
tombol_dekripsi.grid(row = 3,column = 1)
reset_button.grid(row = 0, column = 2)
out.grid(row = 4, column = 2, pady = 10)
view_enkripsi.grid(row = 4, column = 0)
view_dekripsi.grid(row = 4, column = 1)
#Essensial Feature
root.mainloop()