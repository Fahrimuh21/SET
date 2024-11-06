#Nama File: set.py
#Deskripsi: berisi type dan operasi set yang menggunakan list
#Pembuat: Muhammad Fahri /24060124120037
#Tanggal: 5 november 2024

#DEFINISI DAN SPESIFIKASI TYPE
#Set adalah sebuah list dengan syarat setiap elemen harus unik # Semua konstruktor, selektor, dan operasi yang telah didefinisikan
# untuk list juga berlaku pada set

from list1 import *

#DEFINISI DAN SPESIFIKASI OPERASI LIST YANG DIPERLUKAN UNTUK HIMPUNAN


#Rember: elemen, list -> list
#Rember(x,L) menghapus sebuah elemen x dari list L
# Jika x ada di list L, maka elemen L berkurang 1.
# Jika x tidak ada di list L maka L tetap.
# List kosong tetap menjadi list kosong.

def rember(x, L):
    if IsEmpty(L):
        return []
    else :
        if FirstElmt(L)==x:
            return Tail(L)
        else :
            return Konso(FirstElmt(L), rember(x, Tail(L)))
        

# MultiRember: elemen, list -> listl
# MultiRember(x,L) menghapus semua kemunculan elemen x dari list L. 
# List baru yang dihasilkan tidak lagi memiliki elemen x. 
# List kosong tetap menjadi list kosong

def MultiRember(x, L):
    if IsEmpty(L):
        return []
    else:
        if FirstElmt(L)==x:
            return MultiRember(x, Tail(L))
        else:
            return Konso(FirstElmt(L), MultiRember(x, Tail(L)))

#DEFINISI DAN SPESIKASI KONSTRUKTOR SET DARI LIST
# MakeSet: list -> set 
# MakeSet(L) membuat set dari list L dengan menghapus semua kemunculan lebih dari satu kali
# list kosong tetap menjadi himpunan kosong

def MakeSet(L):
    if IsEmpty(L):
        return []
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return MakeSet(Tail(L))
        else:
            return Konso(FirstElmt(L),MakeSet(Tail(L)))

#DEFINISI DAN SPESIKASI KONSTRUKTOR SET 
# KonsoSet: elemen,set -> set 
# konsoSet(e,H) menambahkan sebuah elemen e sebagai elemen pertama set H 
# dengan syarat e belum ada di dalam himpunan H

def KonsoSet(e, H):
    if IsMember(e, H):
        return H
    else:
        return Konso(e, H)

#DEFINISI DAN SPESIFIKASI PREDIKAT
# IsSet: list -> boolean
# IsSet(L) mengembalikan true jika L adalah sebuah set

def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(FirstElmt(L), Tail(L)):
            return False
        else :
            return IsSet(Tail(L))

# IsSubset: 2 set -> boolean
# IsSubset(H1,H2) mengembalikan true jika H1 merupakan subset dari H2

def IsSubset(H1, H2):
    if IsEmpty(H1):
        return True
    else :
        if IsMember(FirstElmt(H1), H2):
            return IsSubset(Tail(H1), H2)
        else:
            return False

# IsEqualSet: 2 set -> boolean
# IsEqualSet(H1,H2} benar jika H1 adalah set yang sama dengan H2

def IsEqualSet(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)

# IsIntersect: 2 set -> boolean
# IsIntersect(H1,H2) benar jika H1 beririsan dengan H2

def IsIntersect(H1, H2):
    if IsOneEmlt(H1):
        if IsMember(FirstElmt(H1), H2):
            return True
        else:
            return False
    else:
        if IsMember(FirstElmt(H1), H2):
            return True
        else:
            return IsIntersect(Tail(H1), H2)

#DEFINISI DAN SPESIFIKASI OPERASI TERHADAP HIMPUNAN
# MakeIntersect: 2 set -> set
# MakeIntersect(H1,H2) menghasilkan set baru yang merupakan hasil irisan antara H1 dan H2

def MakeIntersect(H1,H2):
    if IsEmpty(H1) or IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H1), H2):
            return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
        else:
            return MakeIntersect(Tail(H1), H2)

# MakeUnion: 2 set -> set
# MakeUnion(H1,H2) menghasilkan set baru yang merupakan hasil gabungan antara H1 dan H2

def MakeUnion(H1, H2):
    if IsEmpty(H1):
        return H2
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeUnion(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), H2))

# NBIntersect: 2 set -> integer
# NBIntersect(H1,H2) menghasilkan jumlah elemen yang beririsan pada H1 dan H2
# tanpa memanfaatkan fungsi MakeIntersect(H1,H2).

def NBIntersect(H1, H2):
    if IsEmpty(H1):
        return 0
    else:
        if IsMember(FirstElmt(H1), H2):
            return 1+NBIntersect(Tail(H1), H2)
        else:
            return NBIntersect(Tail(H1), H2)

# NBUnion: 2 set -> integer
# NBUnion(H1,H2) menghasilkan jumlah elemen hasil gabungan antara H1 dan H2
# tanpa memanfaatkan fungsi MakeUnion(H1,H2).

def NBUnion(H1, H2):
    if IsEmpty(H1):
        return NbElmt(H2)
    else:
        if IsMember(FirstElmt(H1), H2):
            return NBUnion(Tail(H1), H2)
        else:
            return 1+NBUnion(Tail(H1), H2)

#APLIKASI
print(rember(2,[]))                               #--> []
print(rember(2, [3]))                             #--> [3]
print(rember(2, [3,4,5,2,3,5,7,8,2]))             #--> [3, 4, 5, 3, 5, 7, 8, 2]
print(MultiRember(2,[]))                          #--> []
print(MultiRember(2, [3]))                        #--> [3]
print(MultiRember(2, [3,4,5,2,3,5,7,8,2]))        #--> [3, 4, 5, 3, 5, 7, 8]
print(MakeSet([1, 3, 3, 4, 5, 5, 6]))             #--> [1, 3, 4, 5, 6]
print(KonsoSet(3, [2, 3, 4, 5]))                  #--> [2, 3, 4, 5]
print(IsSet([2, 3, 4, 5]))                        #--> True
print(IsSubset([2, 3, 4], [5, 6, 3, 2]))          #--> False
print(IsEqualSet([2, 3, 4], [3, 4, 5]))           #--> False
print(IsIntersect([2, 6, 7], [3, 4, 5]))          #--> False
print(MakeIntersect([2, 3, 4], [2, 3, 4, 5]))     #--> [2, 3, 4]
print(MakeUnion([1, 2, 3], [3, 4, 5]))            #--> [1, 2, 3, 4, 5]
print(NBIntersect([1, 2, 3, 4], [2, 3, 4, 5]))    #--> 3
print(NBUnion([1, 2, 3, 4], [2, 3, 4]))           #--> 4