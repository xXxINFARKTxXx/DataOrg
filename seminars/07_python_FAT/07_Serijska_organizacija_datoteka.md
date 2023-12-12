 ## Fakultet tehničkih nauka, DRA, Novi Sad

## Predmet:

## Organizacija podataka

##### dr Vladimir Ivančević

##### Nikola Todorović

##### Vladimir Jovanović


# Serijska organizacija datoteka


# Serijska datoteka

## • Osnovna struktura

- slogovi smešteni jedan za drugim
    - u sukcesivne memorijske lokacije
- fizička struktura ne sadrži informacije o

#### vezama između slogova logičke strukture

#### datoteke

- ne postoji veza između vrednosti ključa sloga

#### i adrese lokacije u koju je smešten


# Serijska datoteka

## • Osnovna struktura

- redosled memorisanja slogova najčešće

#### prema hronološkom redosledu njihovog

#### nastanka

- slogovi mogu, a i ne moraju, biti blokirani


# Serijska datoteka

## • Primer serijske

## datoteke


# Zadatak 1

- Napisati C/C++ program koji će omogućiti rad sa

### podacima o evidentiranim prispećima zatvorenika

### u Gradski zatvor. Za svaki dolazak novog

### zatvorenika u neblokiranoj serijskoj datoteci

### beleži se:

- evidencioni broj (do 8 cifara)
- šifra zatvorenika (tačno 7 karaktera)
- datum i vreme dolaska
- oznaka ćelije u koju će zatvorenik biti smešten (tačno 5
    karaktera)
- dužina kazne u mesecima (do 480 meseci)


# Zadatak 1

- Omogućiti
    - odabir datoteke
    - formiranje datoteke
    - pretragu datoteke
    - unos novog sloga
    - ispis svih slogova
    - ažuriranje sloga
       - direktna obrada serijske datoteke
    - brisanje sloga
       - Logičko brisanje


# Zadatak 2

## • Implementirati fizičko brisanje nad

## prethodnom datotekom


# Zadatak 3

## • Implementirati blokiranu serijsku datoteku

## nad istim slogom.

- Sa svim operacijama


