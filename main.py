import time

for i in range(1, 101):
    print(i, flush=True)
    time.sleep(1)  # pause d'une seconde entre chaque nombre

print("Terminé !")