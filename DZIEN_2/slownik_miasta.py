#słownik
pojazd = {
    "marka":"Ford",
    "model":"Mustang",
    "rok":2019,
    "kolor":"czarny",
    453:"pb98"
}

print(pojazd)
print(pojazd["model"])
print(pojazd[453])

miasto = {
    "Warszawa":{
        "województwo":"mazowieckie",
        "populacja":1890340,
        "powierzchnia":517.24
    },
"Kraków":{
        "województwo":"małopolskie",
        "populacja":780000,
        "powierzchnia":326.86
    },
"Łódź":{
        "województwo":"łódzkie",
        "populacja":670100,
        "powierzchnia":293.25
    },
"Wrocław":{
        "województwo":"dolnośląskie",
        "populacja":643782,
        "powierzchnia":292.82
    },
"Gdańsk":{
        "województwo":"pomorskie",
        "populacja":470900,
        "powierzchnia":262
    }
}

print(f'miasta Polski: {miasto}')
info_wawa = miasto["Warszawa"]
print(f"Informacje o Warszawie: {info_wawa}")

pop_krakow = miasto["Kraków"]["populacja"]
print(f"populacja w Krakowie: {pop_krakow}")

info_dwa = miasto["Kraków"],miasto["Gdańsk"]
print(info_dwa)

#dodawanie nowego miasta do słownika
miasto["Poznań"] = {
        "województwo":"wielkopolskie",
        "populacja":534600,
        "powierzchnia":261.98
    }

print(f'miasta Polski: {miasto}')
