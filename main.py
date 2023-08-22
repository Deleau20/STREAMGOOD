def evaluer(expression):
    try:
        x, operator, y = expression.split(" ")
        x = int(x)
        y = int(y)
        if operator == "+":
            result = x + y
        elif operator == "-":
            result = x - y
        elif operator == "*":
            result = x * y
        elif operator == "/":
            result = x / y
        return(f"Le résultat est : {result: .1f}")
    except ValueError:
        return("Les données entrées sont incorrect.")

print(evaluer("1 + 1"))
chaine = "1+1"
print(eval(chaine))

# retourne snake_case si l'utilisateur entre camelCase
def snake_case(text):
    result = ""
    for i in text:
        if i.isupper():
            result += ('_' + i.lower())
        else:
            result += i
    # result_string = ''.join(result).lstrip('_')
    return result


print(snake_case("camelCaseDeFred"))

