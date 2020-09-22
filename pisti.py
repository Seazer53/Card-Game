import random
import os


def kart_dagitma():
    random.shuffle(iskambil_kartlari)

    for x in range(0, 4):
        yerdeki_kagitlar.append(iskambil_kartlari.pop(x))


def oyuncu_seçim(secim):
    if len(oyuncunun_eli) >= secim:
        if secim == 1:
            yerdeki_kagitlar.append(oyuncunun_eli.pop(0))

        elif secim == 2:
            yerdeki_kagitlar.append(oyuncunun_eli.pop(1))

        elif secim == 3:
            yerdeki_kagitlar.append(oyuncunun_eli.pop(2))

        elif secim == 4:
            yerdeki_kagitlar.append(oyuncunun_eli.pop(3))


def kontrol_oyuncu(opuan, kontrol):
    if len(yerdeki_kagitlar) >= 2:
        if yerdeki_kagitlar[-1][-1:] == "j":
            print("--------------------------------------------")
            print("Oyuncu vale attı! Oyuncu yerdeki kartları aldı!")
            kontrol = True

            if yerdeki_kagitlar[-1][-1:] == yerdeki_kagitlar[-2][-1:] and len(yerdeki_kagitlar) == 2:
                print("--------------------------------------------")
                print("Oyuncu vale ile pişti yaptı!")
                print("--------------------------------------------")
                print("+20 Puan")
                opuan += 20

            oyuncunun_aldigi_kartlar.extend(yerdeki_kagitlar)
            yerdeki_kagitlar.clear()

        elif yerdeki_kagitlar[-2][-2:] == yerdeki_kagitlar[-1][-2:]:
            if len(yerdeki_kagitlar) == 2:
                print("Oyuncu ", yerdeki_kagitlar[-1] , " atarak pişti yaptı! Oyuncu yerdeki kağıtları aldı!")
                print("--------------------------------------------")
                print("+10 Puan")
                opuan += 10
                kontrol = True
            else:
                print("--------------------------------------------")
                print("Oyuncu ", yerdeki_kagitlar[-1], " attı! Oyuncu yerdeki kağıtları aldı!")
                kontrol = True

            oyuncunun_aldigi_kartlar.extend(yerdeki_kagitlar)
            yerdeki_kagitlar.clear()

    return opuan, kontrol


def kontrol_bilgisayar(bpuan, kontrol):
    kart_atildi = False

    for x in bilgisayarin_eli:
        if len(yerdeki_kagitlar) == 0 and kart_atildi is False:
            rastgele_kart = bilgisayarin_eli[0]

            if rastgele_kart[-1] != "j":
                yerdeki_kagitlar.append(rastgele_kart)
                bilgisayarin_eli.remove(rastgele_kart)
                kart_atildi = True

            else:
                if len(bilgisayarin_eli) > 1:
                    yerdeki_kagitlar.append(bilgisayarin_eli.pop(bilgisayarin_eli.index(rastgele_kart) + 1))
                    kart_atildi = True

                else:
                    yerdeki_kagitlar.append(rastgele_kart)
                    bilgisayarin_eli.remove(rastgele_kart)
                    kart_atildi = True

        elif kart_atildi is False and yerdeki_kagitlar[-1][-2:] == x[-2:]:
            yerdeki_kagitlar.append(x)
            bilgisayarin_eli.remove(x)
            kart_atildi = True

        elif kart_atildi is False and x[-1][:-1] == "j":
            if len(yerdeki_kagitlar) == 1 and yerdeki_kagitlar[-1][-1:] == "j":
                yerdeki_kagitlar.append(x)
                bilgisayarin_eli.remove(x)
                kart_atildi = True

            if len(yerdeki_kagitlar) >= 6 and len(bilgisayarin_eli) != 1:
                yerdeki_kagitlar.append(x)
                bilgisayarin_eli.remove(x)
                kart_atildi = True

    if kart_atildi is False:
        yerdeki_kagitlar.append(bilgisayarin_eli.pop(bilgisayarin_eli.index(random.choice(bilgisayarin_eli))))

    if len(yerdeki_kagitlar) >= 2:
        if yerdeki_kagitlar[-1][-1:] == "j":
            print("--------------------------------------------")
            print("Bilgisayar vale attı! Bilgisayar yerdeki kartları aldı!")
            kontrol = True

            if yerdeki_kagitlar[-1][-1:] == yerdeki_kagitlar[-2][-1:] and len(yerdeki_kagitlar) == 2:
                print("--------------------------------------------")
                print("Bilgisayar vale ile pişti yaptı!")
                print("--------------------------------------------")
                print("+20 Puan")
                bpuan += 20

            bilgisayarin_aldigi_kartlar.extend(yerdeki_kagitlar)
            yerdeki_kagitlar.clear()

        elif yerdeki_kagitlar[-2][-2:] == yerdeki_kagitlar[-1][-2:]:
            if len(yerdeki_kagitlar) == 2:
                print("Bilgisayar ", yerdeki_kagitlar[-1], " atarak pişti yaptı! Bilgisayar yerdeki kağıtları aldı!")
                print("--------------------------------------------")
                print("+10 Puan")
                bpuan += 10
                kontrol = True
            else:
                print("--------------------------------------------")
                print("Bilgisayar ", yerdeki_kagitlar[-1], " attı! Bilgisayar yerdeki kağıtları aldı!")
                kontrol = True

            bilgisayarin_aldigi_kartlar.extend(yerdeki_kagitlar)
            yerdeki_kagitlar.clear()

    return bpuan, kontrol


def oyun(kart_dagit):
    oyuncunun_puani = 0
    bilgisayarin_puani = 0
    son_alan = ""
    kart_alma = False
    print(
        "Pişti oyununa hoş geldiniz! 1.5 Güncellemesi ile performans ve yapay zekada iyileştirilmeler yapıldı! Oyunumuz "
        "başlıyor! İyi şanslar!")

    if os.path.isfile('sonuc.txt') is False:
        sonuclar = open("sonuc.txt", "w")
        sonuclar.close()
    else:
        sonuclar = open("sonuc.txt", "r")
        skorlar = sonuclar.readlines()
        oyuncunun_kazanma_sayisi = int(skorlar[1])
        bilgisayarin_kazanma_sayisi = int(skorlar[-1])
        sonuclar.close()
        sonuclar = open("sonuc.txt", "r")
        kazananlar = sonuclar.read()
        print("Önceki oyun sonuçları: ")
        print(kazananlar)
        sonuclar.close()

        istatistik_sifirlama = input("İstatistikler sıfırlansın mı?: ")

        if istatistik_sifirlama == "evet":
            sonuclar = open("sonuc.txt", "w")
            sonuclar.write("Oyuncunun kazanma sayisi:\n")
            sonuclar.write("0\n")
            sonuclar.write("Bilgisayarın kazanma sayisi:\n")
            sonuclar.write("0")
            sonuclar.close()

    print("                     ")

    kural = input("Kuralları biliyor musunuz?(evet,hayır): ")

    print("                     ")

    if kural == "hayır":
        print(
            "Pişti oyunu 52 adet iskambil kağıdıyla oynanır. Oyundaki amaç rakam değeri aynı kartları atarak kartları "
            "toplamaktır.")
        print(
            "Pişti eğer yerde 1 kart varsa mesela sinek 2 sizde karo 2 atarsanız o zaman pişti yapmış olursunuz ve 10 "
            "puan kazanırsınız.")
        print("Yerde sadece vale var ve siz de vale atarsanız bu piştiden 20 puan alırsınız.")
        print("Puanlama: ")
        print("As = 1")
        print("J = 1")
        print("Karo 10 = 3")
        print("Sinek 2 = 2")
        print("Oyun bittiğinde yerde hala kart kalmışsa en son yerden kartları toplayan kimse ona verilir. Oyun "
              "sonunda kim daha fazla kart almışsa 3 puan alır.")
        print("--------------------------------------------")

    while len(iskambil_kartlari) != 0 or (len(oyuncunun_eli) != 0 and len(bilgisayarin_eli) != 0):
        if kart_dagit is False:
            if len(oyuncunun_eli) != 4:
                oyuncunun_eli.append(iskambil_kartlari.pop(0))

            else:
                bilgisayarin_eli.append(iskambil_kartlari.pop(0))

            if len(oyuncunun_eli) == 4 and len(bilgisayarin_eli) == 4:
                kart_dagit = True

        if len(oyuncunun_eli) == 0 and len(bilgisayarin_eli) == 0:
            kart_dagit = False

        if kart_dagit is True:
            print("--------------------------------------------")
            if len(yerdeki_kagitlar) == 0:
                print("Yer temizlendi, yerde toplam ", len(yerdeki_kagitlar), " kart var")

            else:
                print("Yerde en üstteki kağıt ", yerdeki_kagitlar[-1], " ve yerde toplam ", len(yerdeki_kagitlar), " kart var")

            print("                     ")
            print("Oyuncunun kartları:", oyuncunun_eli)
            print("                     ")

            secim = int(input("Hangi kartı atacaksınız?: "))
            print("                     ")
            oyuncu_seçim(secim)
            (puan, kart_alma) = kontrol_oyuncu(0, False)

            if kart_alma == True:
                son_alan = "Oyuncu"

            (puan2, kart_alma) = kontrol_bilgisayar(0, False)

            oyuncunun_puani += puan
            bilgisayarin_puani += puan2

            if kart_alma == True:
                son_alan = "Bilgisayar"

    if son_alan == "Oyuncu":
        oyuncunun_aldigi_kartlar.extend(yerdeki_kagitlar)
        yerdeki_kagitlar.clear()

    elif son_alan == "Bilgisayar":
        bilgisayarin_aldigi_kartlar.extend(yerdeki_kagitlar)
        yerdeki_kagitlar.clear()

    if len(oyuncunun_aldigi_kartlar) > len(bilgisayarin_aldigi_kartlar):
        oyuncunun_puani += 3

    else:
        bilgisayarin_puani += 3

    for x in oyuncunun_aldigi_kartlar:
        if x[-2:] == "as":
            oyuncunun_puani += 1

        if x == "karo 10":
            oyuncunun_puani += 3

        if x == "sinek 2":
            oyuncunun_puani += 2

        if x[-1:] == "j":
            oyuncunun_puani += 1

    for y in bilgisayarin_aldigi_kartlar:
        if y[-2:] == "as":
            bilgisayarin_puani += 1

        if y == "karo 10":
            bilgisayarin_puani += 3

        if y == "sinek 2":
            bilgisayarin_puani += 2

        if y[-1:] == "j":
            bilgisayarin_puani += 1

    if oyuncunun_puani > bilgisayarin_puani:
        print("--------------------------------------------")
        print("Kart kalmadı! Oyun bitti!", "Oyuncu Kazandı!", "Puanlar şöyle; Oyuncunun puanı: ", str(oyuncunun_puani),
              "Bilgisayarın puanı", str(bilgisayarin_puani))
        oyuncunun_kazanma_sayisi += 1
        sonuclar = open("sonuc.txt", "w")
        sonuclar.write("Oyuncunun kazanma sayisi:\n")
        sonuclar.write(str(oyuncunun_kazanma_sayisi))
        sonuclar.write("\n")
        sonuclar.write("Bilgisayarın kazanma sayisi:\n")
        sonuclar.write(str(bilgisayarin_kazanma_sayisi))
        sonuclar.close()

    elif oyuncunun_puani < bilgisayarin_puani:
        print("--------------------------------------------")
        print("Kart kalmadı! Oyun bitti!", "Bilgisayar Kazandı!", "Puanlar şöyle; Oyuncunun puanı: ",
              str(oyuncunun_puani), "Bilgisayarın puanı", str(bilgisayarin_puani))
        bilgisayarin_kazanma_sayisi += 1
        sonuclar = open("sonuc.txt", "w")
        sonuclar.write("Oyuncunun kazanma sayisi:\n")
        sonuclar.write(str(oyuncunun_kazanma_sayisi))
        sonuclar.write("\n")
        sonuclar.write("Bilgisayarın kazanma sayisi:\n")
        sonuclar.write(str(bilgisayarin_kazanma_sayisi))
        sonuclar.close()

    else:
        print("--------------------------------------------")
        print("Kart kalmadı! Oyun bitti!", "Berabere!", "Puanlar şöyle; Oyuncunun puanı: ", str(oyuncunun_puani),
              "Bilgisayarın puanı", str(bilgisayarin_puani))


iskambil_kartlari = ["sinek as", "sinek 2", "sinek 3", "sinek 4", "sinek 5", "sinek 6", "sinek 7", "sinek 8", "sinek 9",
                     "sinek 10", "sinek j", "sinek  q", "sinek k", "karo as", "karo 2", "karo 3", "karo 4", "karo 5",
                     "karo 6", "karo 7", "karo 8", "karo 9", "karo 10", "karo j", "karo  q", "karo k", "kupa as",
                     "kupa 2", "kupa 3", "kupa 4", "kupa 5", "kupa 6", "kupa 7", "kupa 8", "kupa 9", "kupa 10",
                     "kupa j", "kupa  q", "kupa k", "maça as", "maça 2", "maça 3", "maça 4", "maça 5", "maça 6",
                     "maça 7", "maça 8", "maça 9", "maça 10", "maça j", "maça  q", "maça k"]
oyuncunun_eli = []
bilgisayarin_eli = []
yerdeki_kagitlar = []
oyuncunun_aldigi_kartlar = []
bilgisayarin_aldigi_kartlar = []
kart_dagit = False

kart_dagitma()
oyun(kart_dagit)
