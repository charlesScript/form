import random


# générer des nombres aléatoires
NOMBRE_MIN = random.randrange(1, 10)
NOMBRE_MAX = random.randrange(50, 60)
NOMBRE_MAGIQUE = random.randrange(NOMBRE_MIN, NOMBRE_MAX)


# foction permettant de demander un nombre à l'utilisateur
def demander_nombre(nb_min, nb_max):
    nb_int = 0
    while nb_int == 0:
        nb_str = input(f"Quel est le nombre entre {NOMBRE_MIN} et {NOMBRE_MAX} ? ")
        try:
            nb_int = int(nb_str)
        except ValueError:
            print("ERREUR!")
        else:
            if nb_int < nb_min or nb_int > nb_max:
                print(f"ATTENTION! Entrer un nombre entre {NOMBRE_MIN} et {NOMBRE_MAX}!")
                nb_int = 0

    return nb_int


# Conditions qui testent les entrées de l'utilisateur
nombre = 0
vie = 4
while not nombre == NOMBRE_MAGIQUE and vie > 0:
    print(f"Il vous reste {vie} vie(s)!")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre < NOMBRE_MAGIQUE:
        print("Le nombre magique est plus grand!")
        vie -= 1
    elif nombre > NOMBRE_MAGIQUE:
        print("Le nombre magique est plus petit!")
        vie -= 1
    else:
        print("Bravo!")
        print("Le nombre était bien " + str(NOMBRE_MAGIQUE))
if vie == 0:
    print(f"Vous n'avez plus de vie! Le nomber magique était {NOMBRE_MAGIQUE}")
