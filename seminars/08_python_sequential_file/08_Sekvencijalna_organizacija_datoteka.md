## Fakultet tehničkih nauka, DRA, Novi Sad

## Predmet:

## Organizacija podataka

```
dr Vladimir Ivančević
Nikola Todorović
Vladimir Jovanović
```

# Sekvencijalna organizacija

# datoteka


# Sekvencijalna datoteka

- Osnovna struktura
    - slogovi su smešteni sukcesivno jedan za drugim
    - logički susedni slogovi smeštaju se u fizički
       susedne lokacije
          - postoji informacija o vezama između slogova logičke
             strukture podataka datoteke, ugrađena u fizičku
             strukturu
          - realizovana kao linearna logička struktura podataka
             - smeštanjem sloga sa većom vrednošću ključa u lokaciju sa
                većom adresom


# Sekvencijalna datoteka

- Osnovna struktura
    - logički susedni slogovi smeštaju se u fizički
       susedne lokacije
          - rastuće uređenje po vrednostima ključa -> slog sa
             najmanjom vrednošću ključa smešta se u prvu
             lokaciju
    - naziva se i fizički sekvencijalnom organizacijom


# Sekvencijalna datoteka

- Osnovna struktura
    - veza između memorisanih vrednosti ključa
       k(S) i adresa lokacija
          - nije ugrađena u strukturu datoteke
          - ne predstavlja bilo kakvu matematičku funkciju
    - slogovi se smeštaju u blokovima od po _f_ slogova
       - poželjno da faktor blokiranja _f_ bude što veći


# Sekvencijalna datoteka

- Osnovna struktura
    - savremeni OS ( _Unix_ ) i programski jezici ( _C_ , _C++_ ,
       _Java_ ) podržavaju samo sekvencijalni način
       pristupa
          - korisnicima je ostavljeno da naprave svoje sopstvene
             sekvencijalne metode pristupa


# Sekvencijalna datoteka

- Primer sekvencijalne

### datoteke


# Zadatak 1

- Napisati program koji će omogućiti rad sa

#### podacima o evidentiranim prispećima zatvorenika

#### u Gradski zatvor. Za svaki dolazak novog

#### zatvorenika u sekvencijalnoj datoteci sa faktorom

#### blokiranja f = 4 beleži se:

- evidencioni broj (do 8 cifara)
- šifra zatvorenika (tačno 7 karaktera)
- datum i vreme dolaska
- oznaka ćelije u koju će zatvorenik biti smešten (tačno 5
    karaktera)
- dužina kazne u mesecima (do 480 meseci)


# Zadatak 1

- Implementirati:
    - formiranje datoteke
    - unos novog sloga
    - ažuriranje sloga
    - brisanje sloga
       - logičko
    - pretraga po ključu
    - reorganizacija datoteke
    - ispis svih slogova


# Zadatak 2

- Implementirati sekvencijalnu datoteku kod

### koje se slogovi unose pomoću serijske

### datoteke izmena.

- Sve greške koje se pojave tokom funkcionisanja
    programa treba da budu smeštene u serijsku
    datoteku grešaka


# Zadatak 3

- Implementirati sekvencijalnu datoteku čiji

### parametri (faktor blokiranja, postojanje

### serijske datoteke izmena, putanje do

### datoteka) se zadaju putem posebnog

### programa. Nakon zadavanja ovih parametara,

### sekvencijalna datoteka treba da automatski

### funkcioniše sa zadatim parametrima.


