import math

def BMI(weight, height):
    return weight / math.pow(height, 2)

def classify(weight, height):
    bmi = BMI(weight, height)
    if bmi < 20:
        return "maigre"
    elif bmi >=20 and bmi <25:
        return "poids normal"
    else:
        return "surpoids"


personnes = []

for i in range (0,4):
    weight = int(input("saisir votre poids"))
    height = float(input("saisir votre taille"))
    classification = classify(weight, height)
    info_personnes = [weight, height, classification]
    personnes.append(info_personnes)