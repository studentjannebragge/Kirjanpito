# R-koodi, joka laskee henkilön arvioidun eläkeikäpäivän

laske_elakepaiva <- function(syntyma_aika, elakeika_vuotta, elakeika_kuukautta) {
  # Muunna syntymäaika päivämääräksi
  syntyma_date <- as.Date(syntyma_aika, format = "%d.%m.%Y")
  
  if (is.na(syntyma_date)) {
    return("Virheellinen syntymäaika. Käytä muotoa 'DD.MM.YYYY'.")
  }

  # Lisää vuodet
  elake_date <- as.Date(format(syntyma_date, "%Y-%m-%d"))
  elake_date <- as.Date(format(elake_date, "%Y-%m-%d"), origin = elake_date)
  elake_date <- elake_date + lubridate::ymd(syntyma_aika)kryhbfrj"33tt"=format.iso860
