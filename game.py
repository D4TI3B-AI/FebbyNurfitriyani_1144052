import sys
print("Langkah Benar 1-7-2-4-3-7-1\n")
print (" 1.Domba Menyeberang\n 2.Harimau Menyeberang\n 3.Gabah Menyeberang\n 4.Domba Kembali\n 5.Harimau Kembali\n 6.Gabah Kembali\n 7.Perahu Kembali")
def game():
    a = raw_input("Langkah 1 : ")
    if a == '1'    : b = raw_input("Langkah 2 : ")
    else           : print('Anda Gagal')
    if b == '7'    : c = raw_input("Langkah 3 : ")
    else           : print('Anda Gagal')
    if c == '2'    : d = raw_input("Langkah 4 : ")
    else           : print('Anda Gagal')
    if d == '4'    : e = raw_input("Langkah 5 : ")
    else           : print('Anda Gagal')
    if e == '3'    : f = raw_input("Langkah 6 : ")
    else           : print('Anda Gagal')
    if f == '7'    : g = raw_input("Langkah 7 : ")
    else           : print('Anda Gagal')
    if g == '1'    : h = raw_input("Selamat, Anda Berhasil")
game()
