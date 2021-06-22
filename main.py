import turtle


# fonction pour créer des escaliers
def escalier(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)

    t.forward(taille)


# fonction pour créer un carré
def carre(taille):
    for i in range(0, 4):
        t.forward(taille)
        t.left(90)


# fonction pour créer des carrrés dans un seul
def carres(taille, nb):
    for i in range(0, nb):
        for i in range(0, 4):
            t.forward(taille)
            t.left(90)
        taille += 5


# fonctio pour créer un triangle équilatérale
def triangle(taille, nb):
    for i in range(0, nb):
        t.forward(taille)
        t.left(120)
    t.forward(taille)
    t.left(120)
    t.forward(taille/2)
    t.left(90)
    t.forward(taille)


t = turtle.Turtle()

# triangle(100, 2)
# carre(20)
# carres(15, 20)
# escalier(4, 4)

turtle.done()
