import numpy as np

#Program ini tidak didesain untuk mendeteksi spasi, namun kata yang ditulis lebih flexible karena jumlah kata yang diolah tidak harus genap

dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]

class hillChiper():
    def __init__(self, kata, kunci, dictionary):
        self.kata = kata
        self.kunci = kunci
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
        interval = len(kata) // 2
        for x in range(interval):
            mtx_group["mtx {}".format(x)] = mtx_kunci.dot(mtx_group["mtx {}".format(x)])
            mtx_group["mtx {}".format(x)] = mtx_group["mtx {}".format(x)] % 26
        for key, val in mtx_group.items():
            for x in range(2):
                output.append(dictionary[int(val[x, 0])])
        return output
    #Untuk membuat kata dari hash/ sandi
    def dekripsi(self):
        output = []
        mtx_kunci_inv = self.matrikskunciinvers()
        mtx_group = self.matrikskata()
        dictionary = self.dictionary
        interval = len(kata) // 2
        for x in range(interval):
            mtx_group["mtx {}".format(x)] = mtx_kunci_inv.dot(mtx_group["mtx {}".format(x)])
            mtx_group["mtx {}".format(x)] = mtx_group["mtx {}".format(x)] % 26
        for key, val in mtx_group.items():
            for x in range(2):
                output.append(dictionary[int(val[x, 0])])
        return output
#Condition for eternal loop
condition = True
while condition:
    #Memilih metode 
    pilihan = input("Enkripsi / Dekripsi\t\t: ")
    if pilihan == "Enkripsi":
        kata = input("kata yang ingin dienkripsi\t: ")
        kunci = input("kunci yang digunakan\t\t: ")
        try:
            enkripsi1 = hillChiper(kata, kunci, dictionary)
            print("Kata yang telah dienkripsi\t: " , *(enkripsi1.enkripsi()), sep="")
        #jika jumlah huruf pada kunci salah, akan mentrigger hal dibawah
        except ValueError:
            print("Kunci yang digunakan salah")
        else:
            print("Program berjalan dengan baik")
        finally:
            print("Program selesai")
    elif pilihan == "Dekripsi":
        kata = input("kata yang ingin didekripsi\t: ")
        kunci = input("kunci yang digunakan\t\t: ")
        try:
            dekripsi1 = hillChiper(kata, kunci, dictionary)
            print("Kata yang telah didekripsi\t: " , *(dekripsi1.dekripsi()), sep="")
        #jika jumlah huruf pada kunci salah, akan mentrigger hal dibawah
        except ValueError:
            print("Kunci yang digunakan salah")
        else:
            print("Program berjalan dengan baik")
        finally:
            print("Program selesai")
    cek = input("Masih ingin menggunakan program (y/t) ? ")
    if cek == "t":
        condition = False