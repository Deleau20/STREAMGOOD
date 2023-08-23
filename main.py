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

import random

def random_number():
    return random.randint(1, 2)
print(random_number())


def convert(heure_str):
    heures, minutes = map(int, heure_str.split(':'))
    return heures + minutes / 60

def determine_repas(heure_convertie):
    if 7 <= heure_convertie < 8:
        return "petit-déjeuner"
    elif 12 <= heure_convertie < 13:
        return "déjeuner"
    elif 18 <= heure_convertie < 19:
        return "dîner"
    else:
        return None

heure_utilisateur = input("Veuillez entrer l'heure au format HH:MM : ")
if len(heure_utilisateur) != 5 or heure_utilisateur[2] != ':':
    print("Format d'heure incorrect. Utilisez le format HH:MM.")
else:
    try:
        heure_convertie = convert(heure_utilisateur)
        repas = determine_repas(heure_convertie)
        
        if repas:
            print(f"C'est l'heure du {repas}.")
        else:
            print("Ce n'est pas l'heure d'un repas.")
    except ValueError:
        print("Format d'heure incorrect. Utilisez le format HH:MM.")