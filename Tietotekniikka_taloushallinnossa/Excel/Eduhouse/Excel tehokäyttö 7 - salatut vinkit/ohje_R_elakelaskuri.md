# Ohje R-koodin käyttämiseen

Tässä ohjeessa kerrotaan, miten voit käyttää R-koodia laskeaksesi arvioidun eläkeiäkäsi syntymäaikasi perusteella.

## Esivaatimukset
- **R ja RStudio**: Varmista, että sinulla on asennettuna R ja RStudio (tai muu R-ympäristö).
- **`lubridate`-kirjasto**: Tarvitset tämän kirjaston aikojen ja päivämäärien käsittelyyn. Asenna se seuraavalla komennolla:
  ```R
  install.packages("lubridate")
  ```

## Koodin suorittaminen

1. **Avaa RStudio**:
   - Avaa RStudio ja luo uusi skriptitiedosto (`File > New File > R Script`).

2. **Liitä koodi**:
   - Kopioi seuraava koodi skriptitiedostoon:

     ```R
     library(lubridate)

     laske_elakepaiva <- function(syntyma_aika, elakeika_vuotta, elakeika_kuukautta) {
       # Muunna syntymäaika päivämääräksi
       syntyma_date <- as.Date(syntyma_aika, format = "%d.%m.%Y")
       
       if (is.na(syntyma_date)) {
         return("Virheellinen syntymäaika. Käytä muotoa 'DD.MM.YYYY'.")
       }

       # Lisää vuodet ja kuukaudet
       elake_date <- syntyma_date %m+% years(elakeika_vuotta) %m+% months(elakeika_kuukautta)
       return(format(elake_date, "%d.%m.%Y"))
     }

     # Esimerkki koodin suorittamisesta
     syntyma_aika <- "16.12.1959"
     elakeika_vuotta <- 64
     elakeika_kuukautta <- 5

     elakepaiva <- laske_elakepaiva(syntyma_aika, elakeika_vuotta, elakeika_kuukautta)
     print(elakepaiva)
     ```

3. **Suorita koodi**:
   - Tallenna tiedosto ja suorita se painamalla `Ctrl + Enter` (Windows/Linux) tai `Cmd + Enter` (Mac).

4. **Syötteet ja tulosteet**:
   - Voit muuttaa muuttujia `syntyma_aika`, `elakeika_vuotta` ja `elakeika_kuukautta` haluamillesi arvoille. Tulosteeksi saat arvioidun eläkeiän päivämäärän.

## Esimerkki

### Syöte:
```R
syntyma_aika <- "16.12.1959"
elakeika_vuotta <- 64
elakeika_kuukautta <- 5
```

### Tuloste:
```
[1] "16.05.2024"
```

## Mahdolliset virheet
- **Virheellinen päivämäärä**: Jos syötät päivämäärän väärässä muodossa (esim. "16/12/1959"), ohjelma palauttaa virheilmoituksen: `Virheellinen syntymäaika. Käytä muotoa 'DD.MM.YYYY'.`

Jos kohtaat ongelmia, tarkista, että `lubridate`-kirjasto on asennettu ja syötät päivämäärät oikeassa muodossa.

