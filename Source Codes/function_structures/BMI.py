def body_mass_index(weight,height):
    bmi = float(weight / (height*height))
    #You can also use return return weight / math.pow(height,2)
    return bmi

def classify_bmi(bmi):
    if bmi > 40 :
        return "obésité morbide"
    elif bmi >= 35 and bmi <= 40 :
        return "obésité sévère"
    elif bmi >= 30 and bmi < 35:
        return "obésité modérée"
    elif bmi >= 25 and bmi < 30:
        return "surpoids"
    elif bmi >= 18.5 and bmi < 25:
        return "corpulence normale"
    elif bmi >= 16.5 and bmi < 18.5:
        return "maigreur"
    else:
        return "famine"

if __name__ == "__main__":
    family_informations = [(1.70,53),(1.77,92),(1.83,78),(1.59,54)]
    #Oops forgot an extra member !
    family_informations.append((1.92,140))

    #We have a list of TUPLES
    #Each tuple has 2 informations : weight and height
    #We use a foor loop to get these informations in two variables this way
    for hght,wght in family_informations:
        #sending the informations to our function
        bmi = body_mass_index(wght,hght)
        #classifying the bmi
        verdict = classify_bmi(bmi)
        print("Avec un poids de : ",wght," KG et une taille de : ",hght," M vous êtes en état de : ",verdict)
