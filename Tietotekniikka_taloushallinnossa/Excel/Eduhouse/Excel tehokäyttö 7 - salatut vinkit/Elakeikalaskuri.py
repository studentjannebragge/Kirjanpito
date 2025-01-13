from datetime import datetime, timedelta

def laske_elakepaiva(syntyma_aika, elakeika_vuotta, elakeika_kuukautta):
    """
    Laskee henkilön arvioidun eläkeikäpäivän syntymäajan ja eläkeiän perusteella.

    Parametrit:
        syntyma_aika (str): Henkilön syntymäaika muodossa 'DD.MM.YYYY'
        elakeika_vuotta (int): Eläkeiän vuodet
        elakeika_kuukautta (int): Eläkeiän kuukaudet

    Palauttaa:
        str: Arvioitu eläkeikäpäivä muodossa 'DD.MM.YYYY'
    """
    try:
        syntyma_date = datetime.strptime(syntyma_aika, "%d.%m.%Y")
        # Lisää vuodet
        elake_date = syntyma_date.replace(year=syntyma_date.year + elakeika_vuotta)
        # Lisää kuukaudet, huomioi vuoden vaihto
        elake_date = elake_date + timedelta(days=(elakeika_kuukautta * 30))
        return elake_date.strftime("%d.%m.%Y")
    except ValueError:
        return "Virheellinen syntymäaika. Käytä muotoa 'DD.MM.YYYY'."


def main():
    print("Tervetuloa yksinkertaiseen eläkeikälaskuriin!")
    syntyma_aika = input("Anna syntymäaikasi (DD.MM.YYYY): ")
    elakeika_vuotta = 64
    elakeika_kuukautta = 5

    elakepaiva = laske_elakepaiva(syntyma_aika, elakeika_vuotta, elakeika_kuukautta)
    print(f"Arvioitu eläkeikäpäiväsi on: {elakepaiva}")


if __name__ == "__main__":
    main()