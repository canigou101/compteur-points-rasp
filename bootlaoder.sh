#!/bin/bash 
echo "" > bin.txt

REPO_URL="https://github.com/canigou101/compteur-points-rasp"


dest="/home/pi/Desktop/app"

sleep 15

if [ping 8.8.8.8]then
	echo "j'ai de la co" >> bin.txt
	if [pgrep -f "&dest"]then
		git pull origin main
	else
		git clone "&source"	
	fi
else 
  echo "j'ai pas de co" >> bin.txt

fi

cd "$dest"
python3 "$dest/main.py"