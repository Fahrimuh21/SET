#Nama File : list.py
#Pembuat   : Muhammad Fahri
#NIM       : 24060124120037
#Tanggal   : 29 oktober 2024
#Deskripsi : sebuah list

#DEFINISI DAN SPESIFIKASI TYPE
#Konstruktor menambahkan elemen di awal, notasi prefix
#type List:[] atau [e o List]
#Konstruktor menambahkan elemen di akhir, notasi postfis
# type List: [] atau [List o e]

#DEFINISI DAN SPESIFIKASI KONSTRUKTOR
#Konso: elemen, List-> List
#Konso(e,L) menghasilkan sebuah list dari e dan L dengan e sebagai elemen pertama
#Realisasi
def Konso(e, L):
    return [e]+L

#Konsi: List, elemen List
#Konsi (L, e)-> menghasilkan sebah list dari L dan e dengan e sebagai elemen terakhir
#Realisasi
def Konsi(L, e):
    return L+[e]

#DEFINISI DAN SPESIFIKASI SELEKTOR
#FirstElmt: List tidak kosong -> elemen
#FirstElmt(L) Menghasilkan elemen pertama list L
#Realisasi
def FirstElmt(L):
    return L[0]

#LastElmt: List tidak kosong -> elemen
#LastElmt(L): mengembalikan elemen terakhir terakhir list L
#Realisasi
def LastElmt(L):
    return L[-1]

#Tail: List tidak kosong -> List
#Tail(L): Menghasilkan list tanpa elemen pertama list L, mungkin kosong
#Realisasi
def Tail(L):
    return L[1:]
    
#Head: List tidak kosong -> List
#Head(L): Menghasilkan list tanpa elemen terakhir list L, mungkin kosong
#Realisasi
def Head(L):
    return L[:-1]

#DEFINISI DAN SPESIFIKASI PREDIKAT
#IsEmpty : List -> boolean
#IsEmpty(L) benar jika list kosong
# Realisasi
def IsEmpty(L):
    return L == []

#IsOneElmt: List -> boolean
#IsOneElmt (L) adalah benar jika list L hanya mempunyai satu elemen
#Realisasi
def IsOneEmlt(L):
    if IsEmpty(L) :
        return False
    else :
        return Tail(L)==[] and Head(L)==[]
    
#DEFINISI DAN SPESIFIKASI FUNGSI YANG MENGOPERASIKAN LIST
#NbElmt: List -> integer
#NbElmt(L): Menghasilkan banyaknya elemen list, nol jika kosong
#Realisasi
def NbElmt(L):
    if IsEmpty(L):
        return 0
    else :
        return 1+NbElmt(Tail(L))
    
#Elmtken: integer, List -> elemen
#Elmtken (N, L): Mengirimkan elemen list yang ke N, N<=NbELmt(L) dan N>=0
def Elmtken(N, L):
    if N==1:
        return FirstElmt(L)
    else :
        return Elmtken(N-1, Tail(L))

#IsMember: elemen, List -> boolean
#IsMember (X,L) adalah benar jika X adalah elemen list L
def IsMember(X, L):
    if IsEmpty(L):
        return False
    else:
        if FirstElmt(L)==X:
            return True
        else :
            return IsMember(X, Tail(L)) 

#Copy : List -> List
#Copy(L) Menghasilkan list yang identik dengan List asal
def Copy(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(FirstElmt(L), Tail(L))

#Inverse : List -> List
#Inverse(L) Menghasilkan list L yang dibalik, yaitu yang urutan elemennya
# adalah kebalikan dari list asal
def Inverse(L):
    if IsEmpty(L):
        return []
    else:
        return Konso(LastElmt(L), Inverse(Head(L)))

#Konkat: 2 List -> List
#Konkat (L1,L2) Menghasilkan konkatenasi 2 buah list, dengan list L2 "sesudah" list L1
def Konkat(L1, L2):
    if IsEmpty(L1):
        return L2
    else:
        return Konso(FirstElmt(L1), Konkat(Tail(L1), L2))

#SumEint: List of integer -> integer
#SumElmt (L) menghasilkan jumlahan dari setiap elemen di list L
def SumElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return FirstElmt(L)+SumElmt(Tail(L))

#AvgElmt: List of integer -> real
#Avgimit (L) menghasilkan nilai rata-rata
def AvgElmt(L):
    return SumElmt(L)/NbElmt(L)


#MaxElmt (L): List of integer -> integer
#MaxElmt (L) mengembalikan elemen maksimum dari list L
def max2(a, b):
    if a>b:
        return a
    else:
        return b
    
def maxElmt(L):
    if IsEmpty(L):
        return 0
    else:
        return max2(FirstElmt(L), maxElmt(Tail(L)))

#MaxNB: List of integer -> <integer, integer>
#MaxNB(L) menghasilkan <max, countMax> list L
def Countmax(L):
    if IsEmpty(L):
        return 0
    else:
        if FirstElmt(L)==maxElmt(L):
            return 1+Countmax(Tail(L))
        else:
            return Countmax(Tail(L))

def MaxNB(L):
    return [maxElmt(L), Countmax(L)]

#AddList: 2 List of integer -> List of integer
#AddList(L1,L2) menghasilkan list baru yang setiap elemennya
# adalah hasil penjumlahan setiap elemen di L1 dan 12 pada posisi yang sama
def AddList(L1, L2):
    if NbElmt(L1)==NbElmt(L2):
        if IsEmpty(L1) and IsEmpty(L2):
            return []
        else:
            return Konso(FirstElmt(L1)+FirstElmt(L2), AddList(Tail(L1), Tail(L2)))

#IsPalindrom: List of character -> boolean
#IsPalindrom(L) benar jika L merupakan kata palindrom
#yaitu kata yang sama jika dibaca dari kiri atau kanan
#contoh: RUSAK, KASUR RUSAK, NABABAN
def IsPalindrom(L):
    if IsEmpty(L):
        return True
    else:
        if FirstElmt(L)!=LastElmt(L):
            return False
        else :
            return IsPalindrom(Tail(Head(L)))
    
#APLIKASI
# print(Konso(2,[3]))                                    #-->[2, 3]
# print(Konsi([3],2))                                    #-->[3, 2]
# print(FirstElmt([3,4,5,6,7]))                          #-->3
# print(LastElmt([3,4,5,6,7]))                           #-->7
# print(Tail([3,4,5,6,7]))                               #-->[4, 5, 6, 7]
# print(Head([3,4,5,6,7]))                               #-->[3, 4, 5, 6]
# print(IsEmpty([]))                                     #-->True
# print(IsEmpty([3,4,5,6,7]))                            #-->False
# print(IsOneEmlt([]))                                   #-->False
# print(IsOneEmlt([3]))                                  #-->True
# print(IsOneEmlt([3,4,5,6,7]))                          #-->False
# print(NbElmt([3,4,5,6,7]))                             #-->5
# print(Elmtken(3, [3, 4, 5, 5, 6]))                     #-->5
# print(IsMember(3, [1, 2, 4, 3]))                       #-->True
# print(Copy([1, 2, 4, 7]))                              #-->[1, 2, 4, 7]
# print(Inverse([3, 4, 6]))                              #-->[6, 4, 3]
# print(Konkat([1, 2, 3], [4, 5, 6]))                    #-->[1, 2, 3, 4, 5, 6]
# print(SumElmt([1, 2, 3]))                              #-->6
# print(AvgElmt([1, 2, 3]))                              #-->2.0
# print(maxElmt([1, 2, 4, 5]))                           #-->5
# print(MaxNB([1, 2, 3, 4, 4, 4]))                       #-->[4, 3]
# print(MaxNB([2, 4, 5, 5, 5]))                          #-->[5, 3]
# print(AddList([1, 2, 3], [4, 5, 6]))                   #-->[5, 7, 9]
# print(IsPalindrom(["k", "a", "t", "a", "k"]))          #-->True 


