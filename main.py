
sifrelenecekMetin = 'atakandilmen'
blokBoyutuVeModAlmaSayisi = 11
yerDegistirmeBaslangicIndexi = 4
alfabekiHarfSayisi=26
alfabe = {
    "a": 1,"b": 2,"c": 3,"d":4,"e":5,"f":6,
    "g":7,"h":8,"i":9,"j":10,"k":11,
    "l":12,"m":13,"n":14,"o":15,"p":16,
    "q":17,"r":18,"s":19,"t":20,"u":21,
    "v":22,"w":23,"x":24,"y":25,"z":26,
    1: "a",2: "b",3: "c",4: "d",5: "e",6: "f",
    7: "g",8: "h",9: "i",10: "j",11: "k",
    12: "l",13: "m",14: "n",15: "o",16: "p",
    17: "q",18: "r",19: "s",20: "t",21: "u",
    22: "v",23: "w",24: "x",25: "y",26: "z",
}


metinSirasi = {}
metinSirasiIki = {}

# Yer değiştirme indexinden başlayıp +3 -1 +2 -1 +2 -1 ....
# diyerek metnin yerini değiştirmemizi sağlayacak Sözlüğü oluşturuyorum
def metinSirasiOlustur():
    global yerDegistirmeBaslangicIndexi
    global blokBoyutuVeModAlmaSayisi
    global metinSirasiIki
    global metinSirasi
    atakan = 1
    kontrol = 0
    # (Kontrol0:+2),(Kontrol1:-1),(Kontrol2:+3)
    for sira in range (blokBoyutuVeModAlmaSayisi):
        Deger = sira + 1
        sira = ((Deger + (yerDegistirmeBaslangicIndexi - 1)) % blokBoyutuVeModAlmaSayisi)
        if(sira == 0):
            sira = blokBoyutuVeModAlmaSayisi
        metinSirasi[sira] = atakan
        metinSirasiIki[atakan] = sira
        if(kontrol == 1):
            atakan += -1
            kontrol = 2
        elif(kontrol == 2):
            atakan += 3
            kontrol = 1
        else:
            atakan += 2
            kontrol = 1

# 11'li Bloklara böldüğüm için eksik kalan kısımları "?" ile doldurdum.
def metniTamamla(metin):
    print("-----")
    print("Değiştirilmemiş Metin : {}".format(metin))
    global blokBoyutuVeModAlmaSayisi
    modSonucu = len(metin) % blokBoyutuVeModAlmaSayisi
    eklenecekDeger = blokBoyutuVeModAlmaSayisi - modSonucu
    for i in range(eklenecekDeger):
        metin += "?"
    print("Blok Boyutuna Tamamlanmış Metin : {}".format(metin))
    return metin

def sifrele(metin):
    sifreliMetin = []
    sifreliMetinIki = []
    global blokBoyutuVeModAlmaSayisi
    global alfabekiHarfSayisi
    for harf in range(len(metin)):
        if(metin[harf] != "?"):
            yeniDeger = alfabe.get(metin[harf])
            islem = blokBoyutuVeModAlmaSayisi * yeniDeger
            sifreliIslem = islem % alfabekiHarfSayisi
            sifreliDeger = alfabe.get(sifreliIslem)
            sifreliMetin.append(sifreliDeger)
            sifreliMetinIki.append(sifreliDeger)
        else:
            sifreliMetin.append("?")
            sifreliMetinIki.append("?")
    print("Sifrelenmiş Metin : {}".format(sifreliMetin))
    keyler = []
    for key in metinSirasi:
        keyler.append(key)
    listeIndexi = 0
    sira = 0
    for i in range(len(sifreliMetin)):
        sifreliMetinIki[keyler[sira]+(listeIndexi*blokBoyutuVeModAlmaSayisi)-1] \
            = sifreliMetin[metinSirasi[keyler[sira]] + (listeIndexi * blokBoyutuVeModAlmaSayisi) - 1]
        sira += 1
        if(sira == blokBoyutuVeModAlmaSayisi):
            sira = 0
            listeIndexi += 1
    print("Sifrelenmiş ve Yer Değiştirilmiş Metin : {}".format(sifreliMetinIki))
    return sifreliMetinIki

def sifreyiCoz(sifreliDeger):
    modAlmaTersi = 19  # 11*19 = 1 mod26
    global alfabekiHarfSayisi
    cozulmusMetin = []
    sonListe = []
    for i in range(len(sifreliDeger)):
        cozulmusMetin.append(sifreliDeger[i])
    sira = 0
    listeIndexi = 0
    keyler = []
    for key in metinSirasiIki:
        keyler.append(key)
    for i in range(len(sifreliDeger)):
        cozulmusMetin[keyler[sira] + (listeIndexi * blokBoyutuVeModAlmaSayisi) - 1] \
            = sifreliDeger[metinSirasiIki[keyler[sira]] + (listeIndexi * blokBoyutuVeModAlmaSayisi) - 1]
        sira += 1
        if(sira == blokBoyutuVeModAlmaSayisi):
            sira = 0
            listeIndexi += 1
    print("YeriDuzeltilmişMetin: {}".format(cozulmusMetin))
    for harf in range(len(cozulmusMetin)):
        if(cozulmusMetin[harf] != "?"):
            yeniDeger = alfabe.get(cozulmusMetin[harf])
            islem = modAlmaTersi * yeniDeger
            sifreliIslem = islem % alfabekiHarfSayisi
            cozulmusDeger = alfabe.get(sifreliIslem)
            sonListe.append(cozulmusDeger)
    print("Sifrenin Cöülmüş Hali: {}".format(sonListe))

metinSirasiOlustur()
sifrelenecekMetin = metniTamamla(sifrelenecekMetin)
sifreliDeger = sifrele(sifrelenecekMetin)
sifreyiCoz(sifreliDeger)

