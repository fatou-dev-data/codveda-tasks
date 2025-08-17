import random

# Génération du nombre secret entre 1 et 100
nombre_secret = random.randint(1, 100)
tentatives = 0
max_tentatives = 5

print("🎯 Bienvenue dans le jeu du Nombre Mystère !")
print("Devinez un nombre entre 1 et 100.")
print(f"Vous avez {max_tentatives} tentatives maximum.\n")

# Boucle du jeu
while tentatives < max_tentatives:
    try:
        essai = int(input("Votre proposition : "))
    except ValueError:
        print("⚠️ Veuillez entrer un nombre valide.")

        continue
    
    tentatives += 1
    
    if essai == nombre_secret:
        print(f"✅ Bravo ! Vous avez trouvé le nombre en {tentatives} tentatives.")
        break
    elif essai < nombre_secret:
        print("📉 Trop petit.")
    else:
        print("📈 Trop grand.")
else:
    print(f"❌ Vous avez épuisé vos tentatives. Le nombre était {nombre_secret}.")
