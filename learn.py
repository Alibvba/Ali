import random

nombre_mystère = random.randint(1,10)

print("Bienvenue dans le jeu du nombre mystère !")
deviné = False

while not deviné:
    réponse = int(input("devine le nombre :"))
    
    if réponse == nombre_mystère:
        print('Bravo tu as trouvé le nombre mystère')
        deviné = True

    elif réponse < nombre_mystère:
        print("Trop petit, Essaie encore")
    else:
        print("Trop grand")