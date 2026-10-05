#!/bin/bash

source="https://github.com/canigou101/compteur-points-rasp"
dest=""
echo "" > bin.txt

sleep 50
if [ping 8.8.8.8 ]
then
    if [ -f "&dest"];
    then 
        git pull origin main
    else
        git clone $source
    fi
else 
    echo "pas de connection internet" >> bin.txt
fi
