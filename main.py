# recolter l'age de la personne "Quel est votre age ?"
age = int(input("Quel est votre age ?"))

if age < 18:   # << si la personne est mineur -> 7€
    prix_total = 7
else:     #  << si la personne est majeur -> 12€
    prix_total = 12

# prix_total = (7, 12)[age < 18]

# souhaitez-vous du pop corn ?
pop_corn_request = input("Souhaitez-vous du pop corn ? (Oui, Non)")

if pop_corn_request == "Oui": # << si oui
    prix_total += 5

print("Vous devez payer", prix_total, "€")