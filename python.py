skorPemain1 = 0
skorPemain2 = 0
for babak in range(1, 3 + 1, 1):
    print("Babak " + str(babak))
    print("Algian, pilih salah satu: Batu, Gunting, Kertas")
    pemain1 = input()
    print("Hibban, pilih salah satu: Batu, Gunting, Kertas")
    pemain2 = input()
    if pemain1 == pemain2:
        print("Seri")
    else:
        if pemain1 == "Batu" and pemain2 == "Gunting" or pemain1 == "Gunting" and pemain2 == "Kertas" or pemain1 == "Kertas" and pemain2 == "Batu":
            skorPemain1 = skorPemain1 + 1
            print("Pemain 1 menang")
        else:
            skorPemain2 = skorPemain2 + 1
            print("Pemain 2 menang")
print("Permainan Berakhir")
print("Skor Akhir: Pemain 1 = " + str(skorPemain1) + "  Pemain 2 = " + str(skorPemain2))
