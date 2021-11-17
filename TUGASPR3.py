print("Program Batu, Gunting, Kertas")

import random
bot = ["gunting,", "batu", "kertas"]

sistem = random.choise(bot)
pilihan = input("masukkan pilihanmu : ")

print("===kode hasil seri===")
if pilihan.lower() == sistem:
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan bot adalah", sistem.capitalize())
    print("Hasil Seri")

print("===kode hasil jika menang===")
elif pilihan.lower() == "gunting" and sistem == "kertas":
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan adalah", sistem.capitalize())
    print("Kamu Menang")
elif pilihan.lower() == "batu" and sistem == "gunting":
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan adalah", sistem.capitalize())
    print("Kamu Menang")
elif pilihan.lower() == "kertas" and sistem == "batu":
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan adalah", sistem.capitalize())
    print("Kamu menang")

print("---kode hasil jika kalah---")
elif pilihan.lower() == "gunting" and sistem == "batu":
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan adalah", sistem.capitalize())
    print("Kamu kalah")
elif pilihan.lower() == "batu" and sistem == "kertas":
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan adalah", sistem.capitalize())
    print("Kamu kalah")
elif pilihan.lower() == "kertas" and sistem == "gunting":
    print("pilihanmu adalah", pilihan.capitalize())
    print("pilihan lawan adalah", sistem.capitalize())
    print("Kamu kalah")

