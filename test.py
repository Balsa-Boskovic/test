# a = 10

# print(a)

# git add .
# git commit -m "Poruka"
# git pushgit 



filmovi = [
    {"naziv": "Avatar 1", "pozitivni_komentari": 100, "negativni_komentari": 20},
    {"naziv": "Inception", "pozitivni_komentari": 150, "negativni_komentari": 30},
    {"naziv": "Mad Max", "pozitivni_komentari": 80, "negativni_komentari": 10},
    
]


def film_sa_najvise_pozitivnih_komentara(filmovi):
    najvise_pozitivnih = 0
    najbolji_film = None
    for film in filmovi:
        if film["pozitivni_komentari"] > najvise_pozitivnih:
            najvise_pozitivnih = film["pozitivni_komentari"]
            najbolji_film = film
    return najbolji_film


def film_po_pocetnom_karateru(filmovi, karakter):
    for film in filmovi:
        if film["naziv"].startswith(karakter):
            return film
    return None


def film_sa_najboljim_odosom_komentara(filmovi):
    najbolji_odnos = 0
    najbolji_film = None
    for film in filmovi:
        odnos_komentara = film["pozitivni_komentari"] / (film["negativni_komentari"] + 1)  
        if odnos_komentara > najbolji_odnos:
            najbolji_odnos = odnos_komentara
            najbolji_film = film
    return najbolji_film


najbolji_film = film_sa_najvise_pozitivnih_komentara(filmovi)
print("Film sa najviše pozitivnih komentara je:", najbolji_film["naziv"])


karakter = input("Unesite početni karakter za pretragu: ").strip()
trazeni_film = film_po_pocetnom_karateru(filmovi, karakter)
if trazeni_film:
    print("Pronađen je film koji počinje sa karakterom '{}': {}".format(karakter, trazeni_film["naziv"]))
else:
    print("Nije pronađen film koji počinje sa karakterom '{}'.".format(karakter))


film_najbolji_odnos = film_sa_najboljim_odosom_komentara(filmovi)
print("Film sa najboljim odnosom pozitivnih i negativnih komentara je:", film_najbolji_odnos["naziv"])
