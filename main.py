# def evaluer(expression):
#     try:
#         x, operator, y = expression.split(" ")
#         x = int(x)
#         y = int(y)
#         if operator == "+":
#             result = x + y
#         elif operator == "-":
#             result = x - y
#         elif operator == "*":
#             result = x * y
#         elif operator == "/":
#             result = x / y
#         return(f"Le résultat est : {result: .1f}")
#     except ValueError:
#         return("Les données entrées sont incorrect.")

# print(evaluer("1 + 1"))
# chaine = "1+1"
# print(eval(chaine))

# # retourne snake_case si l'utilisateur entre camelCase
# def snake_case(text):
#     result = ""
#     for i in text:
#         if i.isupper():
#             result += ('_' + i.lower())
#         else:
#             result += i
#     # result_string = ''.join(result).lstrip('_')
#     return result


# print(snake_case("camelCaseDeFred"))

# import random

# def random_number():
#     return random.randint(1, 2)
# print(random_number())


# def convert(heure_str):
#     heures, minutes = map(int, heure_str.split(':'))
#     return heures + minutes / 60

# def determine_repas(heure_convertie):
#     if 7 <= heure_convertie < 8:
#         return "petit-déjeuner"
#     elif 12 <= heure_convertie < 13:
#         return "déjeuner"
#     elif 18 <= heure_convertie < 19:
#         return "dîner"
#     else:
#         return None

# heure_utilisateur = input("Veuillez entrer l'heure au format HH:MM : ")
# if len(heure_utilisateur) != 5 or heure_utilisateur[2] != ':':
#     print("Format d'heure incorrect. Utilisez le format HH:MM.")
# else:
#     try:
#         heure_convertie = convert(heure_utilisateur)
#         repas = determine_repas(heure_convertie)
        
#         if repas:
#             print(f"C'est l'heure du {repas}.")
#         else:
#             print("Ce n'est pas l'heure d'un repas.")
#     except ValueError:
#         print("Format d'heure incorrect. Utilisez le format HH:MM.")


# def maxi(liste):
#     maxim = liste[0]
#     for i in liste:
#         if i > maxim:
#             maxim = i
#     return maxim
# print(maxi([1,2,34,5,678,99,87,654,32,1]))

# def mini(liste):
#     mini = liste[0]
#     for i in liste:
#         if i < mini:
#             mini = i
#     return mini
# print(mini([1,2,34,5,678,99,87,654,32,1]))

# #fonction qui retoune le max et le min d'une liste dans un tableau
# def max_min(liste):
#     return [maxi(liste), mini(liste)]

# print(max_min([1,2,34,5,678,99,87,654,32,1]))



# def inscription():
#     nom = input("Quel est votre nom : ")
#     prenom = input("Quel est votre prénom : ")
#     age = input("Quel est votre age : ")
#     email = input("Quel est votre email : ")
#     mot_de_passe = input("Quel est votre mot de passe : ")
#     informations = [nom, prenom, age, email, mot_de_passe]
#     return informations

# def enregistrement(dico={}):
#     nom, prenom, age, email, mot_de_passe = inscription()
#     dico = {"nom": nom, "prenom": prenom, "age": age, "email": email, "mot_de_passe": mot_de_passe}
#     return dico

# print(enregistrement())

# def connexion(dico):
#     email = input("Quel est votre email : ")
#     mot_de_passe = input("Quel est votre mot de passe : ")
#     if email in dico.values() and mot_de_passe in dico.values():
#         return f"Bonjour vous êtes bien inscrit"
#     else:
#         return "Ces infos n'existent pas !"
    
# print(connexion(enregistrement()))

# fonction qui retourne la somme des 1000 entiers
def somme():
    sim = 0
    num = 0
    i = 0
    while i < 1000:
        sim += num
        num += 1
        i += 1
    return sim

print(somme())

# Avec les suites
def somme2():
    n = 1000
    n //=2
    a = 1
    b = 1001
    c = a+b
    g = n*c
    return g  

print(somme2())

# Programmes qui dit si un nomme est premier ou pas
def premier(nombre):
    for i in range(2, nombre):
        if nombre % i == 0:
            return False
    return True

print(premier(6))


def delegue(fonction, liste):
    resultat = []
    for i in liste:
        resultat.append(fonction(i))
    return resultat

print(delegue(lambda x: x**2, [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))