#!/bin/bash

echo "" > bin.txt

REPO_URL="https://github.com/canigou101/compteur-points-rasp"
dest="/home/pi/Desktop/app"

sleep 15

# Verification de la connexion Internet (-c 1 envoie 1 seul paquet)
if ping -c 1 8.8.8.8 > /dev/null 2>&1; then
    echo "j'ai de la co" >> bin.txt

    # Verification si le dossier de destination existe deja
    if [ -d "$dest" ]; then
        cd "$dest" || exit 1
        git pull origin main
    else
        git clone "$REPO_URL" "$dest"
    fi
else
    echo "j'ai pas de co" >> bin.txt
fi

sleep 15

# Lancement du script Python (seulement s'il n'est pas deja lance)
if [ -d "$dest" ]; then
    if pgrep -f "$dest/main.py" > /dev/null; then
        echo "main.py est deja lance, pas de nouveau lancement" >> bin.txt
    else
        cd "$dest" || exit 1
        python3 "$dest/main.py"
    fi
else
    echo "Erreur : le dossier de l'application n'existe pas." >> bin.txt
fi