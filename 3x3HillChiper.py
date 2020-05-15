import numpy as np

dictionary = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

class hillChiper():
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
        return output
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
        return output
pilihan = input("Enkripsi / Dekripsi\t\t: ")
if pilihan == "Enkripsi":
    kata = input("Kata yang ingin dienkripsi\t: ")
    kunci = input("Kunci yang digunakan\t\t: ")
    try:
        enkripsi1 = hillChiper(kata, kunci, dictionary)
        print("Kata yang telah dienkripsi\t: ", *(enkripsi1.enkripsi()), sep="")
    except ValueError:
        print("Kunci yang dimasukkan salah")
    except IndexError:
        print("Kunci yang dimasukkan belum lengkap/salah")
    else:
        print("Program berjalan dengan baik")
    finally:
        print("Program selesai")
        input()
elif pilihan == "Dekripsi":
    kata = input("Kata yang ingin didekripsi\t: ")
    kunci = input("Kunci yang digunakan\t\t: ")
    try:
        dekripsi1 = hillChiper(kata, kunci, dictionary)
        print("Kata yang telah didekripsi\t: ", *(dekripsi1.dekripsi()), sep="")
    except ValueError:
        print("Kunci yang dimasukkan salah")
    except IndexError:
        print("Kunci yang dimasukkan belum lengkap/salah")
    else:
        print("Program berjalan dengan baik")
    finally:
        print("Program selesai")
        input()
else:
    print("Pilihan tidak tersedia")
    input()
