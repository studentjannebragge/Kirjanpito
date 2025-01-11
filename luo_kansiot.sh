#!/bin/bash

# Taloushallinnon osa-alueet
folders=(
    "Kirjanpito"
    "Palkanlaskenta"
    "Tilinpaatos"
    "Budjetointi"
    "Verotus"
    "Rahoitus"
    "Sisainen_laskenta"
    "Raportointi"
    "Saantely_ja_compliance"
    "Tietotekniikka_taloushallinnossa"
)

# Luodaan kansiot ja lisätään .gitkeep tiedosto kuhunkin
for folder in "${folders[@]}"
do
    mkdir -p "$folder"
    touch "$folder/.gitkeep"
done

# Ilmoitetaan onnistuneesta suorituksesta
echo "Kansiot on luotu ja .gitkeep tiedostot lisätty."